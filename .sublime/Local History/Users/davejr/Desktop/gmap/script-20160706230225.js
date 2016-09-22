$(document).ready(function() {
	var json = [
		{	
			"id": "marker-1",
			"center": [40.761077, -73.983307],
			"icon": "<i class='fa fa-building'></i>",
			"title": "Bright Island Route",
			"price": "$ 40.000",
			"image": "assets/img/tmp/tmp-1.jpg"
		},
		{
			"id": "marker-2",
			"center": [40.725382, -73.991968],
			"icon": "<i class='fa fa-home'></i>",
			"title": "Bright Island Route",
			"price": "$ 40.000",		
			"image": "assets/img/tmp/tmp-2.jpg"	
		},
		{
			"id": "marker-3",
			"center": [40.759677, -73.917586],
			"icon": "<i class='fa fa-suitcase'></i>",
			"title": "Bright Island Route",
			"price": "$ 40.000",		
			"image": "assets/img/tmp/tmp-3.jpg"
		},
		{
			"id": "marker-4",
			"center": [40.710249, -73.951918],
			"icon": "<i class='fa fa-shield'></i>",
			"title": "Bright Island Route",
			"price": "$ 40.000",		
			"image": "assets/img/tmp/tmp-4.jpg"
		},
		{
			"id": "marker-5",
			"center": [40.732106, -73.857161],
			"icon": "<i class='fa fa-star'></i>",
			"title": "Bright Island Route",
			"price": "$ 40.000",		
			"image": "assets/img/tmp/tmp-5.jpg"
		},
		{
			"id": "marker-6",
			"center": [40.782558, -73.970457],
			"icon": "<i class='fa fa-building'></i>",
			"title": "Bright Island Route",
			"price": "$ 40.000",		
			"image": "assets/img/tmp/tmp-1.jpg"
		},
		{
			"id": "marker-7",
			"center": [40.739390, -74.038435],
			"icon": "<i class='fa fa-home'></i>",
			"title": "Bright Island Route",
			"price": "$ 40.000",		
			"image": "assets/img/tmp/tmp-1.jpg"
		},
		{
			"id": "marker-8",
			"center": [40.770079, -73.874327],
			"icon": "<i class='fa fa-suitcase'></i>",
			"title": "Bright Island Route",
			"price": "$ 40.000",		
			"image": "assets/img/tmp/tmp-8.jpg"
		},
		{
			"id": "marker-9",
			"center": [40.710065, -73.892044],
			"icon": "<i class='fa fa-home'></i>",
			"title": "Bright Island Route",
			"price": "$ 40.000",		
			"image": "assets/img/tmp/tmp-10.jpg"
		},
		{
			"id": "marker-10",
			"center": [40.731922, -73.825783],
			"icon": "<i class='fa fa-building'></i>",
			"title": "Bright Island Route",
			"price": "$ 40.000",		
			"image": "assets/img/tmp/tmp-11.jpg"
		},
		{
			"id": "marker-11",
			"center": [40.703168, -73.797115],
			"icon": "<i class='fa fa-star'></i>",
			"title": "Bright Island Route",
			"price": "$ 40.000",		
			"image": "assets/img/tmp/tmp-1.jpg"
		},
		{
			"id": "marker-12",
			"center": [40.810119, -73.882946],
			"icon": "<i class='fa fa-star'></i>",
			"title": "Bright Island Route",
			"price": "$ 40.000",		
			"image": "assets/img/tmp/tmp-12.jpg"
		},
		{
			"id": "marker-13",
			"center": [40.812718, -73.828701],
			"icon": "<i class='fa fa-star'></i>",
			"title": "Bright Island Route",
			"price": "$ 40.000",		
			"image": "assets/img/tmp/tmp-3.jpg"
		},
		{
			"id": "marker-14",
			"center": [40.790367, -74.012722],
			"icon": "<i class='fa fa-building'></i>",
			"title": "Bright Island Route",
			"price": "$ 40.000",		
			"image": "assets/img/tmp/tmp-4.jpg"
		}	
	]

	if ($('#map-google').length) {
		$.ajax(json, {
			success: function(data) {
				var markers = [];
				var infos = [];

				$.each(data, function(index, value) {
					var content = '<div id="'+ value.id + '" class="map-popup-content-wrapper"><div class="map-popup-content"><div class="listing-window-image-wrapper">' + '<a href="properties-detail-standard.html">' + '<div class="listing-window-image"style="background-image: url(' + value.image + ');"></div>' + '<div class="listing-window-content">' + '<div class="info">' + '<h2>' + value.title + '</h2>' + '<h3>' + value.price + '</h3>' + '</div>' + '</div>' + '</a>' + '</div></div><i class="fa fa-close close"></i></div>' + '<div class="map-marker">' + value.icon + '</div>';
					markers.push({
						latLng: value.center, 
						data: value.id,			
						options: {									
							content: content,
							offset: { x: -18, y: -42 }							
						}
					});
				});

				$('#map-google').gmap3({		
					map: {									
						options:{
							styles: [{"featureType":"landscape","elementType":"all","stylers":[{"hue":"#FFBB00"},{"saturation":43.400000000000006},{"lightness":37.599999999999994},{"gamma":1}]},{"featureType":"poi","elementType":"all","stylers":[{"hue":"#00FF6A"},{"saturation":-1.0989010989011234},{"lightness":11.200000000000017},{"gamma":1}]},{"featureType":"road.highway","elementType":"all","stylers":[{"hue":"#FFC200"},{"saturation":-61.8},{"lightness":45.599999999999994},{"gamma":1}]},{"featureType":"road.arterial","elementType":"all","stylers":[{"hue":"#FF0300"},{"saturation":-100},{"lightness":51.19999999999999},{"gamma":1}]},{"featureType":"road.local","elementType":"all","stylers":[{"hue":"#FF0300"},{"saturation":-100},{"lightness":52},{"gamma":1}]},{"featureType":"water","elementType":"all","stylers":[{"hue":"#0078FF"},{"saturation":-13.200000000000003},{"lightness":2.4000000000000057},{"gamma":1}]}],
							center:[40.761077, -73.88],
							scrollwheel: false,
							zoom: 12
						}
					},
					marker: {
						cluster: { radius: 100, }
					},
					overlay: {
						values: markers,
						events: {
							click: function(marker, event, context) {															
								$('.map-popup-content-wrapper').css('display', 'none');

								if ($(event[0].target).hasClass('close')) {
									$('#' + context.data).css('display', 'none');
								} else {
									$('#' + context.data).css('display', 'block');
								}
							}
						}
					}
				});					
			}		
		});
	}
});