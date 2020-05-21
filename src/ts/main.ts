import $ from "jquery";

$(() => {
	if (location.pathname.includes("viewer"))
		$("input[type='checkbox']").prop("disabled", true);
});
