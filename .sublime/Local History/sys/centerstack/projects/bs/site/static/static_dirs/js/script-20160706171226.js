/*-----------------------------------------------------------------------------------

 	Script - All Custom frontend $ scripts & functions
 
-----------------------------------------------------------------------------------*/
(function(){
'use strict';

/* transform to small header function
------------------------------------------------*/
function smallHeader() {
	
	if ($(window).scrollTop() > 40) {var delDarkHeader = false;
	var addTransHeader = false;
	$('nav#main-nav > ul > li.mega-menu').on({
		mouseenter: function() {
			if ($(window).width() > 1023 && !$("header").hasClass("header-style-vertical")) {
				if ($("header").hasClass("sub-dark")) {
					if (!$("header").hasClass("header-dark")) {
						delDarkHeader = true;
						$("header").addClass('header-dark');
					}
					if (!$("header").hasClass("transparent-light")) {
						addTransHeader = true;
						$("header").addClass('transparent-light');
					}
				} else if ($("header").hasClass("header-dark") || $("header").hasClass("transparent-light")) {
					$("header").addClass('mega-hover');
				}
			}
		},
		mouseleave: function() {
			if ($(window).width() > 1023 && !$("header").hasClass("header-style-vertical")) {
				$("header").removeClass('mega-hover');
				if (delDarkHeader) { $("header").removeClass('header-dark'); }
				if (addTransHeader) { $("header").removeClass('transparent-light'); }
			}
		}
	});
		$("header").addClass("small-header");	
	} else {
		$("header").removeClass("small-header");	
	}
	
}


/* show fixed items after scroll amount function (back to top / fixed share)
------------------------------------------------*/
function showFixedItems() {
	
	if ($(window).scrollTop() > $(window).height()) {
		$( '#backtotop, #share.share-fixed' ).addClass("visible");	
	} else { 
		$( '#backtotop, #share.share-fixed' ).removeClass("visible");	
	}
	
}


/* adapt height function
------------------------------------------------*/
function adaptHeight() {
	
	/* - Columns - */
	var cols = ".column";
	if ($(window).width() < 960) { cols = ".one-half, .one-third, .two-third"; }
	$('.column-section.adapt-height').each(function() { 
		var thisEl = $(this);
		$(thisEl).children(".column").css('minHeight','inherit');
		$(thisEl).children(".column").find(".col-content").css('marginTop', '0');
						
		if ($(window).width() > 767) {
			var maxHeight = 0;
			var tallestEl = '';
			$(thisEl).children(cols).each(function() {
				var theHeight = $(this).outerHeight();
				var theBorder = parseInt($(this).css('border-top-width'), 10) + parseInt($(this).css('border-bottom-width'), 10);
				if (theHeight + theBorder > maxHeight) { maxHeight = theHeight + theBorder+1; tallestEl = $(this); }
				// +1 is hack for bordered sticky
			});
			if (maxHeight) {
				$(thisEl).children(".column").css('minHeight',maxHeight+'px');
				$(tallestEl).addClass("tallest");	
			}
			
			// apply vertical-center
			if ($(thisEl).hasClass("vertical-center")) {
				$(thisEl).children(".column:not(.tallest)").each(function() {
					if ($(this).find(".col-content").length > 0 && !$(this).find(".col-content").is(':empty')) {
						var theContent = $(this).find(".col-content");
						var elHeight = maxHeight - (parseInt($(this).css('paddingTop'), 10) + parseInt($(this).css('paddingBottom'), 10));
						var contentHeight = $(theContent).height();
						if (contentHeight < elHeight) { 
							var centerMargin = (elHeight - (contentHeight)) / 2;
							$(theContent).css('marginTop', centerMargin + 'px');
						}
					} 
				});
			}
		} // end if window > 767
	});
	
	/* - Fullheight Section - */
	if ($(".fullwidth-section.fullheight").length > 0) {
		$(".fullwidth-section.fullheight").each(function() { 
			var theContent = $(this).find(".fullwidth-content");
			var contentHeight = $(theContent).height();
			var contentPadding = parseInt($(theContent).css('paddingTop')) + parseInt($(theContent).css('paddingBottom'), 10);
			if (contentHeight+contentPadding < $(this).height()) { 
				var centerMargin = ($(this).height() - (contentHeight+contentPadding)) / 2;
				$(theContent).css('transform', 'translateY(' + centerMargin + 'px)');
			}
		});
	}
	
	/* - Hero / Pagetitle (if pagetitle is taller than hero) - */
	if ($(".hero-full #page-title").length > 0 || $(".hero-big #page-title").length > 0) { 
		var pageTitle = $("#hero #page-title").outerHeight() + parseInt($("#hero #page-title").css('marginTop'),10);
		if ($("header").hasClass("header-style-vertical")) { headerHeight = 0; }
		
		var addMargin = 0;
		if ((pageTitle + headerHeight*2) > $("#hero").outerHeight() && parseInt($("#hero #page-title").css('marginTop'),10) < 1) {
			$("#hero #page-title").addClass("title-adapt");
			addMargin = parseInt($("#hero #page-title").css('top'),10);
		} else {
			$("#hero #page-title").removeClass("title-adapt");
		}
		
		if (pageTitle+addMargin >  $("#hero").outerHeight()) {
			$("#hero").css('height',pageTitle+addMargin-2+'px'); // -2 is for prevend jumping
		} else  {
			$("#hero").css('height','auto');
		}
	} 
	
}


/* do animations if element is visible
------------------------------------------------*/
function animateOnScroll() {
	
	/* has-animation elements */
	$('.has-animation').each(function() {
		var thisItem = $(this);
		if ($(window).width() > 1024) {
			var visible = thisItem.visible(true);
			var delay = thisItem.attr("data-delay");
			if (!delay) { delay = 0; }
			if (thisItem.hasClass( "animated" )) {} 
			else if (visible) {
				thisItem.delay(delay).queue(function(){thisItem.addClass('animated');});
			}
		} else {
			thisItem.addClass('animated');	
		}
	});
	
	/* counter elements */
	$('.counter-value').each(function(){
		var counter = $(this);
		if ($(window).width() > 767 && counter.visible(true)) {		
			counter.addClass('animated');
			counter.find('.counter-animator').each(function(){
				var animator = $(this);
				var value = animator.data('value') * 10;
					animator.find('ul').css({
						'transform': 'translateY(-' + value + '%)',
						'-webkit-transform': 'translateY(-' + value + '%)',
						'-moz-transform': 'translateY(-' + value + '%)',
						'-ms-transform': 'translateY(-' + value + '%)',
						'-o-transform': 'translateY(-' + value + '%)'
					});
			});
		}
	});
	
	/* progress bar */
	$('.progress-bar-item').each(function() {
		var thisItem = $(this);
		var visible = thisItem.visible(true);
		var percent = thisItem.find('.progress-bar .progress-active ').attr('data-perc');
		if (thisItem.hasClass( "anim" )) {} 
		else if (visible) {
			var randomval = Math.floor(Math.random() * (300 - 50 + 1)) + 50;
			thisItem.addClass("anim");
			thisItem.find('.progress-bar .progress-active ').animate({'width': percent+'%',}, 2000, 'easeInOutQuart', function(){
				$(this).find('.tooltip').delay(randomval).animate({'opacity':1}, 500);	
			}).css('overflow', 'visible');
		}
	});
		
}



/* Animations Function
------------------------------------------------*/
function reorganizeIsotope() { 
	$('.isotope-grid[class*="style-modern"]').each(function(){
		var $container = $(this);
		var width = $container.find(".grid-sizer").width();
		var ratioheight = $container.data('heightratio');
		if (!ratioheight) { ratioheight = 0.8; }
		var spacing = 0; if ($container.hasClass("isotope-spaced") || $container.hasClass("isotope-spaced-mini")) { spacing = parseInt($container.find(".isotope-item").css('marginRight'),10); }
		var height = parseInt(width * ratioheight, 10);
		$container.children('.isotope-item').css({ 'height': height+'px' });
		$container.children('.isotope-item.tall, .isotope-item.wide-tall').css({ 'height': height*2+spacing+'px' });
		$container.isotope( 'layout' );

		// adapt images
		$container.children('.isotope-item').each(function() {
			var imgHeight = $(this).find("img").height();
           	var imgWidth = $(this).find("img").width();
			var imgRatio = imgWidth/imgHeight;
			var itemHeight = $(this).height();
           	var itemWidth = $(this).width();
			var itemRatio = itemWidth/itemHeight;
			var imgClass = '';
			if (imgRatio < itemRatio) { imgClass = 'wide-img'; $(this).find("img").removeClass('tall-img'); }
			else { imgClass = 'tall-img'; $(this).find("img").removeClass('wide-img'); }
			$(this).find("img").addClass(imgClass);
        });
	});
}


var headerHeight = false;
$(window).load(function() {
	
	
	/*---------------------------------------------- 
	 		 H I D E   P A G E L O A D E R
	------------------------------------------------*/
	$("body").addClass("page-is-loaded");
		
	
	/*---------------------------------------------- 
	  P S E U D O   H E A D E R (if not transparent)
	------------------------------------------------*/
	headerHeight = $("header").height();
	if (!$("header").hasClass("header-transparent") && !$("header").hasClass("header-style-floating") && !$("header").hasClass("header-style-vertical")) {
		$("body").append('<div id="pseudo-header" style="height:'+headerHeight+'px;position:absolute;z-index:-1;"></div>');
	}
	
	
	/*---------------------------------------------- 
	  P R E P A R E   A D A P T   H E I G H T
	------------------------------------------------*/
	$('.column-section.adapt-height').each(function() {
		$(this).children('.column').each(function() {
			if (!$.trim($(this).html())) {
				$(this).addClass("empty-content");
			} else {
				if ($(this).children('.col-content').length < 1) {  $(this).wrapInner('<div class="col-content"></div>'); }	
			}
		});
	});
	

	/*---------------------------------------------- 
			O P E N / C L O S E   S E A R C H
	------------------------------------------------*/
	$('#show-search').on("click", function() { $(".header-search-content").addClass("search-visible"); return false; });
	$('.header-search-content .search-outer').on("click", function() { $(".header-search-content").removeClass("search-visible"); return false; });
	$('#close-search').on("click", function() { $(".header-search-content").removeClass("search-visible"); return false; });
	
	
	
	/*---------------------------------------------- 
			I S O T O P E  /  M A S O N R Y 
	------------------------------------------------*/
	if( $().isotope ) {
		
		/* Call Isotope  
		------------------------------------------------*/	
		$('.isotope-grid').each(function(){
			var $container = $(this);
			$(this).prepend('<div class="grid-sizer"></div>');
			if (!$container.hasClass("fitrows")) { 
				$container.imagesLoaded( function(){
					$container.isotope({
						layoutMode: 'masonry',
						itemSelector : '.isotope-item',
						masonry: { columnWidth: '.grid-sizer' }
					});	
				});
			} else {
				$container.imagesLoaded( function(){
					$container.isotope({
						layoutMode: 'fitRows',
						itemSelector : '.isotope-item',
						masonry: { columnWidth: '.grid-sizer' }
					});	
				});
			}
		});
			
		
		/* Filter isotope
		------------------------------------------------*/
		$('.filter').on("click", "li a", function() { 
			var thisItem = $(this);
			var parentul = thisItem.parents('ul.filter').data('related-grid');
			
			if (!parentul) {
				alert('Please specify the dala-related-grid');
			} else {
				thisItem.parents('ul.filter').find('li').removeClass('active');
				thisItem.parent('li').addClass('active');
				var selector = thisItem.attr('data-filter');
				$('#'+parentul).isotope({ filter: selector }, function(){ });
			}
			
			return false;
		});


		var btn_map = $("#toggles button.on")
		var btn_grid = $("#toggles button.off")
		var grid = $("#grid")
		var map = $("#map")
		grid.toggleClass('hidden', true);

		btn_grid.click(function() {
			btn_map.toggleClass('on', false);
			btn_map.toggleClass('off', true);
			btn_grid.toggleClass('on', true);
			btn_grid.toggleClass('off', false);
			map.toggleClass('hidden', true);
			grid.toggleClass('hidden', false);
			reorganizeIsotope();

		});

		btn_map.click(function() {
			btn_map.toggleClass('off', false);
			btn_map.toggleClass('on', true);
			btn_grid.toggleClass('on', false);
			btn_grid.toggleClass('off', true);
			map.toggleClass('hidden', false);
			grid.toggleClass('hidden', true);
		});

		
		reorganizeIsotope();
		
	}
	
	
	/*---------------------------------------------- 
		  M E G A M E N U   (color dependecies)
	------------------------------------------------*/
	var delDarkHeader = false;
	var addTransHeader = false;
	$('nav#main-nav > ul > li.mega-menu').on({
		mouseenter: function() {
			if ($(window).width() > 1023 && !$("header").hasClass("header-style-vertical")) {
				if ($("header").hasClass("sub-dark")) {
					if (!$("header").hasClass("header-dark")) {
						delDarkHeader = true;
						$("header").addClass('header-dark');
					}
					if (!$("header").hasClass("transparent-light")) {
						addTransHeader = true;
						$("header").addClass('transparent-light');
					}
				} else if ($("header").hasClass("header-dark") || $("header").hasClass("transparent-light")) {
					$("header").addClass('mega-hover');
				}
			}
		},
		mouseleave: function() {
			if ($(window).width() > 1023 && !$("header").hasClass("header-style-vertical")) {
				$("header").removeClass('mega-hover');
				if (delDarkHeader) { $("header").removeClass('header-dark'); }
				if (addTransHeader) { $("header").removeClass('transparent-light'); }
			}
		}
	});
	
	
	
	/*---------------------------------------------- 
		  S U B M E N U   (Add gap for submenu if too close to border)
	------------------------------------------------*/
	$('nav#main-nav > ul > li:last-child').prev('li').andSelf().each(function() {
        if ($(this).children('ul.submenu').length > 0) {
			var pageRight = parseInt($(window).width() - ($("#page-content").offset().left + $("#page-content").outerWidth()), 10);
			var elRight = parseInt( ($(window).width() - ($(this).offset().left + $(this).outerWidth())) - pageRight, 10);
			if (elRight < 150) { $(this).children('ul.submenu').addClass('add-gap'); }	
		}
    });
	
	
	
	/*---------------------------------------------- 
			R E S P O N S I V E   N A V
	------------------------------------------------*/
	$('header').on("click", ".responsive-nav-toggle", function() { 
		$('#menu').toggleClass('menu-is-open'); 
		return false;
	});
	
	$('#main-nav').on("click", "li > a", function() {
		var thisItem = $(this); 
		var thisParent = $(this).parent('li'); 
		if (thisItem.siblings('ul').length > 0 && thisItem.siblings('ul').css('display') === 'none') {
			thisItem.siblings('ul').slideDown(400);
			thisParent.siblings('li').children('ul').slideUp(400);
			thisParent.siblings('li').find('.mega-menu-content').slideUp(400);  
			thisParent.siblings('li').find('.mega-menu-content ul li > ul').slideUp(400);  
			return false;	
		} else if (thisItem.siblings('.mega-menu-content').length > 0 && thisItem.siblings('.mega-menu-content').css('display') === 'none') { 
			thisItem.siblings('.mega-menu-content').slideDown(400);
			thisParent.siblings('li').find('.mega-menu-content').slideUp(400);
			thisParent.siblings('li').find('.mega-menu-content ul li > ul').slideUp(400);  
			thisParent.siblings('li').children('ul').slideUp(400);    
			return false;	
		}
	});
	
	$('header').on("click", ".show-language", function() { 
		$('#header-language > .header-language-content').toggleClass('show'); 
		return false;
	});
	
	
	/*---------------------------------------------- 
			R E V O L U T I O N   S L I D E R
	------------------------------------------------*/
	if($().revolution) {
		$("#hero .revolution-slider").revolution({
			sliderType:"standard",
			sliderLayout:"fullscreen",
			fullScreenAutoWidth:"on",
			fullScreenOffsetContainer:"#pseudo-header",
			delay:9000,
			disableProgressBar:'on',
			navigation: {
				arrows:{ 
					enable:true, 
					style:"sudo-nav",
					left:{ h_offset: 0 },
					right:{  h_offset: 0 } 
				},
				bullets:{ 
					enable:false, 
					style:"sudo-bullets",
					h_align:"center",
					v_align:"bottom",
					h_offset:0,
					v_offset:20,
					space:8,  
				},
				touch:{
				 	touchenabled:"on",
				 	swipe_treshold : 75,
				 	swipe_min_touches : 1,
				 	drag_block_vertical:false,
				 	swipe_direction:"horizontal"
				}				
			},
			responsiveLevels:[2048,1024,778,480],			
			gridwidth:[1024,778,480,400],
			gridheight:[700,550,550,450],
			lazyType: 'smart'
		});
		
		$("#hero .revolution-slider").bind("revolution.slide.onchange",function (e,data) {
			if (data.currentslide.hasClass('text-light')) {
				if ($("header").hasClass("header-transparent")) { $("header").addClass("transparent-light").removeClass("transparent-dark"); }
				if ($("#hero #scroll-down").length > 0) { $("#hero #scroll-down").addClass("text-light"); }
				$("#hero .revolution-slider .sudo-bullets").addClass("sudo-light").removeClass("sudo-dark");
			} else {
				if ($("header").hasClass("header-transparent")) { $("header").addClass("transparent-dark").removeClass("transparent-light"); }
				if ($("#hero #scroll-down").length > 0) { $("#hero #scroll-down").removeClass("text-light"); }
				$("#hero .revolution-slider .sudo-bullets").addClass("sudo-dark").removeClass("sudo-light");
			}
		});		
		
	}
	
	
	/*---------------------------------------------- 
				   S C R O L L   T O (back to top, scroll down, scroll to section)
	------------------------------------------------*/
	$('body').on('click', '#backtotop,#scroll-down,.scroll-to', function() {
		var topPos = 0;
		if ($(this).attr("id") === "scroll-down") { topPos = $("#page-body").offset().top; }
		if ($(this).hasClass("scroll-to")) { 
			var href = $(this).attr('href');
			var target = $(this).attr('data-target');
			if (href.charAt(0) === '#') { target = href;  }
			topPos = $(target).offset().top; 
		}
		$('html,body').animate({ scrollTop: topPos}, 1000, 'easeInOutQuart');
		return false;
	});
	
	
	
	/*---------------------------------------------- 
				   	 P A R A L L A X
	------------------------------------------------*/
	if($().parallax) { 
		$('.parallax-section').parallax();
	}
	
	
	
	
	/*---------------------------------------------- 
			    I N L I N E   V I D E O
	------------------------------------------------*/
	$('body').on("click", ".inline-video", function() { 
		var el = $(this);
		var type = el.data('type');
		var video = el.data('videoid');
				
		if (type === 'youtube') { 
		var iframe='<iframe src="http://www.youtube.com/embed/'+video+'?autoplay=1" width="100%" height="100%" frameborder="0" allowfullscreen ></iframe>';
		} else if (type === 'vimeo') {
		var iframe='<iframe src="https://player.vimeo.com/video/'+video+'?autoplay=1" width="100%" height="100%" frameborder="0" allowfullscreen></iframe>';
		}
		
		el.append('<div class="inline-iframe-container"></div>');
		el.find(".inline-iframe-container").html(iframe+'<div class="close-inline-video"></div>');
		
		setTimeout(function() {
			el.addClass('active');
		}, 1000);
		
		return false;
	});
	
	$('body').on("click", ".close-inline-video", function() { 
		var thisItem = $(this); 
		thisItem.parents( ".inline-video" ).removeClass('active');
		thisItem.parent( ".inline-iframe-container" ).remove();
		return false;
	});
	
	
	
	
	/*---------------------------------------------- 
				   	L I G H T C A S E
	------------------------------------------------*/
	if($().lightcase) { 
		$('a[data-rel^=lightcase]').lightcase({ 
			showSequenceInfo: false, 
			swipe: true, 
			showCaption:false,
			overlayOpacity:0.95,
			maxWidth: 1300,
			maxHeight: 1100,
			shrinkFactor: 1,
			video: {
				width : 780,
				height : 420
				}
		});
	}
	
	
	
	/*---------------------------------------------- 
				   F I T   V I D E O S
	------------------------------------------------*/
	if($().fitVids) { 
		$("body").fitVids();
	}
	
	
	
	/*---------------------------------------------- 
		O W L   S L I D E R & C A R O U S E L
	------------------------------------------------*/
	if($().owlCarousel) {
		
		$(".owl-slider").owlCarousel({
			items:1,
			stopOnHover : true,
			nav: false,
			navText:false,
			dots: true,
			smartSpeed : 600,			
			singleItem : true,
			autoHeight : true,
			loop: false,
			autoplay: true,
			navRewind: false
		});
		
		$(".owl-carousel").owlCarousel({
			items : 4,
			itemsDesktop:false,
			responsive: { //shop related items
			  480: { items: 1 },
			  768: { items: 2 },
			  },
			autoplay: false,
			autoHeight : true,
			nav: true,
			navText:false,
			dots: true,
			loop: false
		});
				
	}
	
	
	
	/*---------------------------------------------- 
			 P R E P A R E   C O U N T E R
	------------------------------------------------*/
	$('.counter-value').each(function(){
		var thisEl = $(this);
		var thisVal = thisEl.text();
		
		// put digits in a span
		var digits = thisVal.toString().replace(/(\d)/g, '<span class="digit"><span class="digit-value">$1</span></span>');
		thisEl.html(digits+'<div class="main">'+thisVal+'</span>');
		
		// add the ul list
		thisEl.find('.digit').each(function(){
			var digit = $(this);
			var digitValue = digit.find('.digit-value').text();
			digit.append(
				'<div class="counter-animator" data-value="' + digitValue + '">' +
					'<ul>' +
						'<li>0</li>' +
						'<li>1</li>' +
						'<li>2</li>' +
						'<li>3</li>' +
						'<li>4</li>' +
						'<li>5</li>' +
						'<li>6</li>' +
						'<li>7</li>' +
						'<li>8</li>' +
						'<li>9</li>' +
					'</ul>'+
				'</div>'
			);
		});
		
	});
	
	
	
	/*---------------------------------------------- 
				        T A B S 
	------------------------------------------------*/	
	$(".tabs").each(function() {
		var thisItem = $(this); 
		thisItem.find('.tab-content').removeClass('active');
		var rel = thisItem.find('.active a').attr('href');
		thisItem.find('.'+rel).addClass('active');
	});
	
	$(".tab-nav").on("click", "a", function() { 
		var thisItem = $(this); 
		var parentdiv = thisItem.parents('li').parent('ul').parent('div');
		var rel = thisItem.attr('href');
		
		$(parentdiv).find(".tab-nav li").removeClass("active");
		thisItem.parents('li').addClass("active");
		
		$(parentdiv).find(".tab-container .tab-content").hide().removeClass('active');
		$(parentdiv).find(".tab-container ."+rel).fadeIn(500).addClass('active');
		
		return false;
		
	});
	
	
	/*---------------------------------------------- 
			T O G G L E  &  A C C O R D I O N
	------------------------------------------------*/		
	$(".toggle-item").each(function() {
		$(this).find('.toggle-active').siblings('.toggle-inner').slideDown(300);							
	});
	
	$(".toggle-item").on("click", ".toggle-title", function() { 
		var thisItem = $(this); 
		var parentdiv = thisItem.parent('div').parent('div');
		var active = thisItem.parent('div').find('.toggle-inner').css('display');
		
		if ($(parentdiv).attr('class') === 'accordion') {
			if (active !== 'none' ) { 
				$(parentdiv).find('.toggle-item .toggle-inner').slideUp(300);
				thisItem.toggleClass('toggle-active');
			} else {
				$(parentdiv).find('.toggle-item .toggle-inner').slideUp(300);
				$(parentdiv).find('.toggle-item .toggle-title').removeClass('toggle-active');
				
				thisItem.toggleClass('toggle-active');
				thisItem.siblings('.toggle-inner').slideDown(300);
			}
		} else {
			thisItem.toggleClass('toggle-active');
			thisItem.siblings('.toggle-inner').slideToggle(300);
		}
		
		return false;
	});
	


	/*---------------------------------------------- 
	 S E L F H O S T E D   A U D I O   +   V I D E O
	------------------------------------------------*/
	if($().mediaelementplayer) {
		$('audio,video').mediaelementplayer();
	}
	
	
	
	/*---------------------------------------------- 
				   	 V I D E O   B G
	------------------------------------------------*/
	if($().bgVideo) { 
		$('.videobg-section').bgVideo();
	}


	/*	Hide Isotope
	========================================= */
	


	
	adaptHeight();
	smallHeader();
	showFixedItems();
	animateOnScroll(); 


	
	
});


$(window).scroll(function() { 
	smallHeader(); 
	showFixedItems();
	animateOnScroll(); 
});


$(window).resize(function() { 
	adaptHeight();
	if( $().isotope ) { reorganizeIsotope(); }
	if ($(window).width() > 1023) { $('#menu').removeClass('menu-is-open'); }
});


/* Call Feeds */
$(document).ready(function() { 
	
	/*---------------------------------------------- 
				I N S T A G R A M   F E E D
	------------------------------------------------*/
	if( $(".instagram-widget").length > 0  && $().spectragram){
		$.fn.spectragram.accessData = {
			accessToken: '36286274.b9e559e.4824cbc1d0c94c23827dc4a2267a9f6b',
			clientID: 'b9e559ec7c284375bf41e9a9fb72ae01'
		};
		
		$('.instagram-widget').each(function(){
			var $theFeed = $(this);
			var instaType = $theFeed.data('type');
			var instaUser = $theFeed.data('user');
			var instaTag = $theFeed.data('tag');
			var instaCount = $theFeed.data('count');
			
			if (instaType === 'user') {
				$theFeed.spectragram('getUserFeed', {
					query: instaUser, 
					max: Number(instaCount),
					size: 'medium',
					wrapEachWith: "<div></div>"
				});
			} else if (instaType === 'tag') {
				$theFeed.spectragram('getRecentTagged',{
					query: instaTag,
					max: Number(instaCount),
					size: 'medium',
					wrapEachWith: "<div></div>"
				});
			}
		});
	}
	
	/*---------------------------------------------- 
				F L I C K R   F E E D
	------------------------------------------------*/
	if( $(".flickr-widget").length > 0  && $().jflickrfeed){
		$('.flickr-widget').each(function(index){
			var $theFeed = $(this);
			var flickrId = $theFeed.data('id');
			var flickrCount = $theFeed.data('count');
			
			$theFeed.jflickrfeed({
				limit: Number(flickrCount),
				qstrings: {
					id: flickrId
				},
				itemTemplate: '<div><a href="{{image_b}}" data-rel="lightcase:flickr'+index+'"><img src="{{image_s}}" alt="{{title}}"/></a></div>'
			});
		});
	}
	
	
	/*---------------------------------------------- 
			   D R I B B B L E   F E E D
	------------------------------------------------*/
	if( $(".dribbble-widget").length > 0 ){
		$('.dribbble-widget').each(function(){
			var $theFeed = $(this);
			var dribbbleUser = $theFeed.data('user');
			var dribbbleCount = $theFeed.data('count');
		
			$.jribbble.setToken('YOURACESSTOKEN');
			
			$.jribbble.users(dribbbleUser).shots({'per_page': Number(dribbbleCount)}).then(function(res) {
			  	var html = [];
			  	res.forEach(function(shot) {
					html.push('<div class="shot">');
					html.push('<a href="' + shot.html_url + '" target="_blank">');
					html.push('<img src="' + shot.images.normal + '">');
					html.push('</a></div>');
			  	});
			  	$theFeed.html(html.join(''));
			});
			
		});
	}


});

})($);