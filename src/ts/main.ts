import $ from "jquery";
import * as converter from "json-2-csv";

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
		let ele = document.createElement("a");
		$(ele).attr({
			"href": "data:application/json;charset=utf-8," +
				encodeURI(JSON.stringify(serializeRows(), null, "\t")),
			"download": `s4slide-db-dump-${new Date().toISOString()}.json`
		});
		ele.click();
	});

	$("#ul-form").submit(ev => {
		ev.preventDefault();
		let file = ev.target.childNodes[0].files[0];
		file.text().then(text => {
			// make sure there are LF line endings
			text = text.replace(/\r\n?/g, "\n");
			converter.csv2json(text, processUpload);
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

function serializeRows(): Landslide[] {
	let landslides: Landslide[] = [];
	$("#people input[value!='all']:checked").each((ind, ele) => {
		let num = $(ele).attr("value");
		let sum: Summary = JSON.parse($(`#sum-${num} code`).text());
		let morpho: Morphometrics = JSON.parse($(`#morpho-${num} code`).text());
		let metrics: Metrics = JSON.parse($(`#metrics-${num} code`).text());
		let meta: Metadata = JSON.parse($(`#meta-${num} code`).text());
		landslides.push(new Landslide(sum, morpho, metrics, meta));
	});
	return landslides;
}

function createDownload(err: Error, csv: string): void {
	if (err) {
		console.log(err);
		return;
	}
	let ele = document.createElement("a");
	$(ele).attr({
		"href": `data:text/csv;charset=utf-8,${encodeURI(csv)}`,
		"download": `s4slide-db-dump-${new Date().toISOString()}.csv`
	});
	ele.click();
}

function processUpload(err: Error, array: any[]): void {
	if (err) {
		console.log(err);
		return;
	}
	array.forEach(val => {
		let landslide = new Landslide(val.sum, val.morpho, val.metrics, val.meta);
		landslide.removeEmpty();
	});
	$.post("/upload/", {
		data: JSON.stringify(array),
		name: sessionStorage.getItem("name"),
		email: sessionStorage.getItem("email")
	});
}

// https://docs.djangoproject.com/en/3.0/ref/csrf/#acquiring-the-token-if-csrf-use-sessions-and-csrf-cookie-httponly-are-false
function getCookie(name: string) {
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

class Landslide {
	sum: Summary;
	morpho: Morphometrics;
	metrics: Metrics;
	meta: Metadata;

	constructor(sum: Summary, morpho: Morphometrics, metrics: Metrics, meta: Metadata) {
		this.sum = sum;
		this.morpho = morpho;
		this.metrics = metrics;
		this.meta = meta;
	}

	removeEmpty(): void {
		for (let table in this) {
			for (let field in this[table]) {
				let val = this[table][field];
				if (val == "" || val == ",")
					delete this[table][field];
			}
		}
	}
}

interface Summary {
	id: number;
	pid: number;
	name: string;
	aliases: string;
	frontal_confinement: boolean;
	object_type: Type;
	ss_depth_m: number;
	ss_time_twtt: number;
	ss_depth_notes: string;
	comments: string;
	category: string;
}

enum Type {
	S = "Single",
	M = "Multiple",
}

interface Morphometrics {
	id: number;
	landslide: number;
	latitude: number;
	longitude: number;
	w_depth_min: number;
	w_depth_max: number;
	w_depth_notes: string;
	lt: number;
	ld: number;
	le: number;
	l_notes: string;
	ls: number;
	hs: number;
	he: number;
	ws: number;
	scarp_surf_nat: string;
	scarp_notes: string;
	wd: number;
	td_max_m: number;
	td_max_twtt: number;
	tu_max_m: number;
	tu_max_twtt: number;
	t_notes: string;
	dep_notes: string;
	ht: number;
	s: number;
	s_notes: string;
	ss: number;
	ss_notes: string;
	st: number;
	st_notes: string;
}

interface Metrics {
	id: number;
	landslide: number;
	attachment: boolean;
	surf_basal: string;
	surf_upper: string;
	a: number;
	a_notes: string;
	v: number;
	v_notes: string;
	age: string;
	age_error: number;
	age_notes: string;
	features: string;
}

interface Metadata {
	id: number;
	landslide: number;
	data_type: string;
	data_type_notes: string;
	data_source: string;
	data_repo: string;
	pub: string;
	contact_name: string;
	contact_email: string;
	db_notes: string;
	data_res_h: number;
	data_res_v: number;
	notes: string;
}
