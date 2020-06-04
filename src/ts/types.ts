export default class Landslide {
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

	// remove nested properties that contain no data
	removeEmpty(): void {
		for (let table in this) {
			for (let field in this[table]) {
				let val: any = this[table][field];
				if (val === "" || val === ",")
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
	upload_date: Date;
	verified: boolean;
}
