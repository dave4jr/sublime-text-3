$(document).ready(function() {
	'use strict';

	if ($('#map-google').length) {
		$.ajax('assets/data/markers.json', {
			success: function(values) {
				var markers = [];
				var infos = [];

				$.each(values, function(index, value) {
						 var content = '<div id="' + value.id + '" class="map-popup-content-wrapper"><div class="map-popup-content"><div class="listing-window-image-wrapper">' +
									'<a href="properties-detail-standard.html">' +
										 '<div class="listing-window-image" style="background-image: url(' + value.image + ');"></div>' +
										 '<div class="listing-window-content">' +
											  '<div class="info">' +
													'<h2>' + value.title + '</h2>' +
													'<h3>' + value.price + '</h3>' +
											  '</div>' +
										 '</div>' +
									'</a>' +
							  '</div></div><i class="fa fa-close close"></i></div>' +
							  '<div class="map-marker">' + value.icon + '</div>';

					markers.push({
						latLng: value.center, 
						data: value.id,			
						options: {									
							content: content,
							offset: {
									x: -18,
									y: -42
								}							
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
						cluster: {
								radius: 100,
							}
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