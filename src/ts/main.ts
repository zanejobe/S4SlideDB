import $ from "jquery";
import json2csv from "json-2-csv";

$(() => {
	if (location.pathname.includes("viewer")) {
		$("#selector input:checkbox").prop("disabled", true);
		$("script").contents().unwrap();
	}

	$(".close").click(hideModal);

	$("input[value='all']").change(ev =>
		$("#people input").prop("checked", $(ev.target).prop("checked")));

	$("#map").click(ev => {
		let landslides: Landslide[] = serializeRows();
		console.log(landslides);
	});

	$("#plot").click(ev => {
		let landslides: Landslide[] = serializeRows();
		console.log(landslides);
	});

	$("#dl").click(ev =>
		json2csv.json2csv(serializeRows(), createDownload, {
			expandArrayObjects: true }));
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

function createDownload(err, csv): void {
	if (err) return;
	let ele = document.createElement("a");
	$(ele).attr({
		"href": `data:text/csv;charset=utf-8,${encodeURI(csv)}`,
		"download": `s4slide-db-dump-${new Date().toISOString()}.csv`
	});
	ele.click();
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
