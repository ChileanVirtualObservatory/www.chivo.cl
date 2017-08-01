// Opera 8.0+
var isOpera = (!!window.opr && !!opr.addons) || !!window.opera || navigator.userAgent.indexOf(' OPR/') >= 0;
// Firefox 1.0+
var isFirefox = typeof InstallTrigger !== 'undefined';
// Safari 3.0+ "[object HTMLElementConstructor]" 
var isSafari = Object.prototype.toString.call(window.HTMLElement).indexOf('Constructor') > 0 || (function (p) { return p.toString() === "[object SafariRemoteNotification]"; })(!window['safari'] || safari.pushNotification);
// Internet Explorer 6-11
var isIE = /*@cc_on!@*/false || !!document.documentMode;
// Edge 20+
var isEdge = !isIE && !!window.StyleMedia;
// Chrome 1+
var isChrome = !!window.chrome && !!window.chrome.webstore;
// Blink engine detection
var isBlink = (isChrome || isOpera) && !!window.CSS;

if(typeof $ !== "undefined") $(document).ready(function(){
	var a = document.body,
		e = document.documentElement,
		$s = $("section .background img");
	$(window).unbind("scroll").scroll(function(){
		//s.style.backgroundPosition = "auto " + -(Math.max(e.scrollTop, a.scrollTop) / 80) + "px";
		$s.css("margin-top",(Math.max(e.scrollTop, a.scrollTop)/6)+"px");
		//console.log("auto " + -(Math.max(e.scrollTop, a.scrollTop) / 80) + "px");
		//console.log(s.style.backgroundPosition);
	});

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

	// HEADER BACKGROUND

	if(isFirefox){
		var elem = e;
	}else{
		var elem = document.body;
	}

	var maxScrollTop = Math.round( window.innerHeight / 3 );
	var currentScollTop = elem.scrollTop;
	var percent = currentScollTop/maxScrollTop;
	if(percent > 0.9) percent = 0.9;
	var $header = $('body header');
	$header.css("background-color","rgba(0,0,0,"+percent+")");
	$(this).scroll(function(){
		currentScollTop = elem.scrollTop;
		percent = currentScollTop/maxScrollTop;
		if(percent > 0.9) percent = 0.9;
		$header.css("background-color","rgba(0,0,0,"+percent+")");
	});

	var $body = $("html,body");
	$("#home .arrow").addClass("light");
	$("#home .arrow").click(function(){
		var px = $("section#video").offset().top;
		$body.animate({scrollTop: px}, 1000);
	});
});