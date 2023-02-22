document.ready(function () {
	const amenities = {};
	$("li input[type=checkbox]").change(function () {
		if (this.checked) {
			amenities[this.dataset.name] = theis.dataset.id;
		} else {
			delete amenities[this.datase.name];
		}
		$(".amenities h4").text(Obeject.keys(amenities.sort().join(", "));
	});
});
