$(function(){
	var $shadowbg = $('body div.shadowbg');
	var $shadowbgBack = $shadowbg.find('.back');
	var $shadowbgName = $shadowbg.find('#info-name');
	var $shadowbgPosition = $shadowbg.find('#info-position');
	var $shadowbgEmail = $shadowbg.find('#info-email');
	var $shadowbgImage = $shadowbg.find('#info-image');
	var $shadowbgLink = $shadowbg.find('#info-link');
	var $shadowbgProjects = $shadowbg.find('#info-projects');
	var $shadowbgProjectsContainer = $shadowbg.find('.projects');
	var $shadowbgBiography = $shadowbg.find('#info-biography');
	var $shadowbgBiographyContainer = $shadowbg.find('.biography');
	console.log($shadowbgImage);

	var $persons = $('section .content ul li div.person');
	$shadowbgBack.click(function(){
		$shadowbg.addClass("hide");
	});
	$shadowbg.click(function(event){
		if(event.target == this) $shadowbg.addClass("hide");
	});
	$(document).keydown(function(e){
		if (e.keyCode == 27 && !$shadowbg.hasClass("hide")) $shadowbg.addClass("hide");
	});

	$persons.click(function(){
		if($shadowbg.hasClass("hide")){
			$shadowbg.removeClass("hide");
			$shadowbgName.html(this.dataset.name);
			if(this.dataset.cargo){
				$shadowbgPosition.html(this.dataset.cargo);
			}else{
				$shadowbgPosition.html('N/A');
			}

			if(this.dataset.email){
				$shadowbgEmail.html('<a href="mailto:'+this.dataset.email+'">'+this.dataset.email+'</a>');
			}else{
				$shadowbgEmail.html('N/A');
			}

			if(this.dataset.link){
				$shadowbgLink.parent().removeClass('hide');
				$shadowbgLink.html('<a href="'+this.dataset.link+'">'+this.dataset.link+'</a>');
			}else{
				$shadowbgLink.parent().addClass('hide');
				$shadowbgLink.html('');
			}

			if(this.dataset.image){
				$shadowbgImage.attr('src',this.dataset.image);
			}

			console.log(this.dataset.projects);
			if(this.dataset.projects){
				$shadowbgProjectsContainer.removeClass('hide');
				$shadowbgProjects.html(this.dataset.projects);
			}else{
				$shadowbgProjectsContainer.addClass('hide');
				$shadowbgProjects.html('');
			}
			if(this.dataset.biography){
				$shadowbgBiographyContainer.removeClass('hide');
				$shadowbgBiography.html(this.dataset.biography);
			}else{
				$shadowbgBiographyContainer.addClass('hide');
				$shadowbgBiography.html('');
			}
		}else{
			$shadowbg.addClass("hide");
		}
	});
});