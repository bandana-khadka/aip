
function initMap() {
    var map;
    map = new google.maps.Map(document.getElementById('map'), {
      center: {lat: -33.8804477, lng: 151.2022338},
      zoom: 16
    });

    var service = new google.maps.places.PlacesService(map);
    console.log(service);
    service.getDetails({
      placeId: 'ChIJse6XQySuEmsRO7j5kgWBIWA'
    }, function(place, status) {
      if (status === google.maps.places.PlacesServiceStatus.OK) {
        var marker = new google.maps.Marker({
              map: map,
              position: place.geometry.location
            });
      }
    });
}


var RegisterPage = {

	init: function() {
		this.$container = $('.validate-username');
		this.render();
		this.bindEvents();
	},

	render: function() {

	},


	bindEvents: function() {
		$('#id_username', this.$container).on('change',function(){
			var username = $(this).val();

            $.ajax({
                url: '/ajax/username_exists/',
                data: {
                  'username': username
                },
                dataType: 'json',
                success: function (data) {
                  if (data.is_taken) {
                    alert(data.error_message);
                  }
                }
            });
		});

		$('#id_email', this.$container).on('change',function(){
			var email = $(this).val();

            $.ajax({
                url: '/ajax/email_exists/',
                data: {
                  'email': email
                },
                dataType: 'json',
                success: function (data) {
                  if (data.is_taken) {
                    alert(data.error_message);
                  }
                }
            });
		});
	}
};

$(document).ready(function() {
	RegisterPage.init();
});