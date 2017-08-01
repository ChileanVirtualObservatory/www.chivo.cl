if(typeof $ !== "undefined") $(document).ready(function(){
	var $menuAside = $("#menu-mobile aside.menu");
	var $menuClose = $menuAside.find(".close");
	var $menuShadow = $("#menu-mobile div.shadow");
	$("#menu-mobile .button-container").click(function(){
		$menuAside.addClass("show");
		$menuShadow.addClass("show");
	});
	$menuShadow.click(function(){
		$menuAside.removeClass("show");
		$menuShadow.removeClass("show");
	});
	$menuClose.click(function(){
		$menuAside.removeClass("show");
		$menuShadow.removeClass("show");
	});

	// SLIDER RATIO
	var ratio = 8/16;
	var $slider = $(".slider .images");
	var slider_width = $slider.width();
	console.log(slider_width);
	var slider_height = slider_width*ratio;
	$slider.height(slider_height);
	$(window).resize(function(){
		slider_width = $slider.width();
		console.log(slider_width);
		slider_height = slider_width*ratio;
		$slider.height(slider_height);
	});
});