import $ from "jquery";

$(() => {
	if (location.pathname.includes("viewer"))
		$("input[type='checkbox']").prop("disabled", true);

	$(".morpho").click(ev => {
		$.getJSON(`/viewer/morpho/${ev.target.hash.substring(1)}/`, displayInfo);
	});

	$(".metrics").click(ev => {
		$.getJSON(`/viewer/metrics/${ev.target.hash.substring(1)}/`, displayInfo);
	});

	$(".meta").click(ev => {
		$.getJSON(`/viewer/meta/${ev.target.hash.substring(1)}/`, displayInfo);
	});

	$(".close").click(ev => {
		$(".modal").hide();
		$(ev.target).next().remove();
	});
});

function displayInfo(data: landslideMorphometrics | landslideMetrics | landslideMeta) : void {
	$("#info .modal-content").append(`<code>${JSON.stringify(data)}</code>`);
	$("#info").show();
}

interface landslideMorphometrics {
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

interface landslideMetrics {
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

interface landslideMeta {
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
