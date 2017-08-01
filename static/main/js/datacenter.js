$(function(){
	var $images = $('section img');
	var $gallery = $("div.gallery");
	var $galleryBack = $gallery.find('header div.back');
	var $galleryThumbs = $gallery.find('.images-container');
	var $galleryImages = $galleryThumbs.find('.image');
	var $galleryView = $gallery.find('.image-viewer');
	var $galleryViewFrame = $galleryView.find('img');
	var $galleryViewPrev = $galleryView.find('.arrow.prev');
	var $galleryViewNext = $galleryView.find('.arrow.next');

	var last_index = 0;
	var current_index = 0;
	$galleryImages.each(function(index,element){
		$(element).attr("data-index",index);
		last_index = index;
	});

	var ON_VIEWER = false;

	var loadImage = function(imageName, index){
		current_index = index;
		$galleryViewPrev.show();
		$galleryViewNext.show();
		if(index == 0) $galleryViewPrev.hide();
		if(index == last_index) $galleryViewNext.hide();
		$galleryThumbs.addClass('hide');
		$galleryView.addClass('show');
		$galleryViewFrame.attr('src','/media/datacenter/'+imageName);
		ON_VIEWER = true;
	};

	$images.click(function(){
		$galleryThumbs.removeClass('hide');
		$galleryView.removeClass('show');
		if(this.dataset.image){
			var image = this.dataset.image;
			$galleryImages.each(function(index,element){
				if(element.dataset.image == image) loadImage(image, element.dataset.index);
			});
			$gallery.addClass('show');
		}else{
			$gallery.addClass('show');
		}
	});
	$galleryImages.click(function(){
		loadImage(this.dataset.image, this.dataset.index);
	});
	$galleryBack.click(function(){
		if(ON_VIEWER){
			$galleryThumbs.removeClass('hide');
			$galleryView.removeClass('show');
		}else{
			$gallery.removeClass('show');
		}
		ON_VIEWER = false;
	});
	$galleryViewPrev.click(function(){
		if(current_index > 0){
			--current_index;
			var image = $galleryImages[current_index].dataset.image;
			var index = $galleryImages[current_index].dataset.index;
			loadImage(image, index);
		}
	});
	$galleryViewNext.click(function(){
		if(current_index < last_index){
			++current_index;
			var image = $galleryImages[current_index].dataset.image;
			var index = $galleryImages[current_index].dataset.index;
			loadImage(image, index);
		}
	});
	$(document).keydown(function(event){
		if(event.keyCode == 27){
			$galleryBack.click();
		}else if(event.keyCode == 37 && ON_VIEWER){
			$galleryViewPrev.click();
		}else if(event.keyCode == 39 && ON_VIEWER){
			$galleryViewNext.click();
		}
	});
});