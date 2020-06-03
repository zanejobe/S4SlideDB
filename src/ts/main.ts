import $ from "jquery";
import * as converter from "json-2-csv";
// babel needs .ts extension to resolve imports
// ignore them so type checker doesn't complain
// @ts-ignore
import landslide from "./types.ts";
// @ts-ignore
import header from "./keys.ts";

declare global {
	interface Window {
		data: landslide[];
	}
}

$(() => {
	if (location.pathname.includes("viewer")) {
		// disable the form checkboxes while they don't do anything
		$("#selector input:checkbox").prop("disabled", true);
		// Django wraps JSON data in script tags, so unwrap them
		$("#people script").contents().unwrap();
	}

	$(".close").click(hideModal);

	// automatically select/deselect all search result rows
	$("input[value='all']").change(ev =>
		$("#people input").prop("checked", $(ev.target).prop("checked")));

	$("#map").click(ev => {
		window.data = serializeRows();
		$("#mapFrame").attr("src", "/map/");
		$("#mapModal").show();
	});

	$("#plot").click(ev => {
		window.data = serializeRows();
		$("#plotFrame").attr("src", "/plot/");
		$("#plotModal").show();
	});

	$("#dl-csv").click(ev =>
		converter.json2csv(serializeRows(), createDownload, {
			expandArrayObjects: true }));

	$("#dl-json").click(ev => {
		let downloadLink: HTMLAnchorElement = document.createElement("a");
		$(downloadLink).attr({
			"href": "data:application/json;charset=utf-8," +
				encodeURI(JSON.stringify(serializeRows(), null, "\t")),
			"download": `${createFilename()}.json`
		});
		downloadLink.click();
	});

	$("#ul-form").submit(ev => {
		ev.preventDefault();
		$("#ul-status").html("<p>Uploading, please wait...</p>");
		let file: File = (<HTMLInputElement>ev.target.childNodes[0]).files[0];
		file.text().then(text => {
			// make sure there are LF line endings
			text = text.replace(/\r\n?/g, "\n");
			converter.csv2json(text, processUpload, {
				keys: header,
				trimFieldValues: true
			});
		});
	});
});

$.ajaxSetup({
	beforeSend: function (xhr, settings) {
		if (settings.type === "POST" && !this.crossDomain) {
			xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"));
		}
	}
});

document.onkeydown = hideModal;
window.onclick = hideModal;

function hideModal(ev): void {
	if (ev.target.className.includes("modal") ||
		ev.target.className.includes("close") ||
		ev.key === "Escape")
		$(".modal").hide();
}

function serializeRows(): landslide[] {
	let slides: landslide[] = [];
	$("#people input[value!='all']:checked").each((ind, ele) => {
		let num = $(ele).attr("value");
		let sum = JSON.parse($(`#sum-${num} code`).text());
		let morpho = JSON.parse($(`#morpho-${num} code`).text());
		let metrics = JSON.parse($(`#metrics-${num} code`).text());
		let meta = JSON.parse($(`#meta-${num} code`).text());
		slides.push(new landslide(sum, morpho, metrics, meta));
	});
	return slides;
}

function createDownload(err: Error, csv: string): void {
	if (err) {
		console.log(err);
		return;
	}
	let downloadLink: HTMLAnchorElement = document.createElement("a");
	$(downloadLink).attr({
		"href": `data:text/csv;charset=utf-8,${encodeURI(csv)}`,
		"download": `${createFilename()}.csv`
	});
	downloadLink.click();
}

function createFilename(): string {
	return `s4slide-db-dump-${new Date().toISOString()}`;
}

function processUpload(err: Error, array: any[]): void {
	if (err) {
		console.log(err);
		return;
	}
	array.forEach(val => {
		let slide: landslide = new landslide(val.sum, val.morpho, val.metrics, val.meta);
		slide.removeEmpty();
	});
	$.post("/upload/", {
		data: JSON.stringify(array),
		name: sessionStorage.getItem("name"),
		email: sessionStorage.getItem("email")
	})
	.done(() => $("#ul-status").html("<p style='color:green'>Upload succeeded!</p>"))
	// TODO show more detailed error message
	.fail(() => $("#ul-status").html("<p style='color:red'>Upload failed!</p>"));
}

// https://docs.djangoproject.com/en/3.0/ref/csrf/#acquiring-the-token-if-csrf-use-sessions-and-csrf-cookie-httponly-are-false
function getCookie(name: string): string {
	let cookieValue: string = null;
	if (document.cookie && document.cookie !== '') {
		const cookies: string[] = document.cookie.split(';');
		for (let i = 0; i < cookies.length; i++) {
			let cookie: string = cookies[i].trim();
			// Does this cookie string begin with the name we want?
			if (cookie.substring(0, name.length + 1) === (name + '=')) {
				cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
				break;
			}
		}
	}
	return cookieValue;
}

