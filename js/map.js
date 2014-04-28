    //var map = L.mapbox.map('map', 'ngr.i2he4c1d');
    var map = L.mapbox.map('map', 'ngr.i2he4c1d');
    var me;
    var geolocate = document.getElementById('geolocate');

    // This uses the HTML5 geolocation API, which is available on
    // most mobile browsers and modern browsers, but not in Internet Explorer
    //
    // See this chart of compatibility for details:
    // http://caniuse.com/#feat=geolocation
    if (!navigator.geolocation) {
        geolocate.innerHTML = 'geolocation is not available';
    } else {
        geolocate.onclick = function(e) {
            e.preventDefault();
            e.stopPropagation();
            map.locate();
        };
    }

    // Once we've got a position, zoom and center the map
    // on it, and add a single marker.
    map.on('locationfound', function(e) {
        var currentLocation = L.latLng(e.latitude, e.longitude);
        map.setZoom(16);
        map.panTo(currentLocation);
        
        if (me) {
            me.setLatLng(currentLocation);
        } else {
            var locationIcon = L.icon({
                iconUrl: './images/1398384698_591255-location2.png',
            });

            me = L.circle(currentLocation, e.accuracy, {
                color: 'red',
                fillColor: '#f03',
                fillOpacity: 0.2
            }).addTo(map);

        }
        // And hide the geolocation button
        //geolocate.parentNode.removeChild(geolocate);
    });

    // If the user chooses not to allow their location
    // to be shared, display an error message.
    map.on('locationerror', function() {
        geolocate.innerHTML = 'position could not be found';
    });
