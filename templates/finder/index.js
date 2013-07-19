// Pull in the bbox
var bbox_string = finder_settings.EXAMPLE_PLACE_BBOX.split(',');
var minY = parseFloat(bbox_string[1]);
var maxY = parseFloat(bbox_string[3]);
var minX = parseFloat(bbox_string[0]);
var maxX = parseFloat(bbox_string[2]);

// In Leaflet
var southwest_limit = new L.LatLng(minX, minY);
var northeast_limit = new L.LatLng(maxX, maxY);
var bounding_box = new L.LatLngBounds(southwest_limit, northeast_limit);

// Pull in the center
var example_string = finder_settings.EXAMPLE_PLACE_LAT_LNG.split(',');
var default_lat = parseFloat(example_string[0]);
var default_lon = parseFloat(example_string[1]);

// Pull in the default place
var place = finder_settings.EXAMPLE_PLACE;

// More globals
var geocoder = new google.maps.Geocoder();
var map = null;
var user_marker = null;
var displayed_slug = null;
var displayed_polygon = null;
var boundaries = new Array();

// Bootstrap the map
function init_map(lat, lng) {
    if (map == null) {
        var ll = new L.LatLng(lat, lng);
        map = new L.Map('map-canvas', {
            zoom: 14,
            center: ll,
            maxZoom: 16,
            minZoom:9
        });
        tiles = new L.TileLayer("http://{s}.latimes.com/quiet-la-0.3.0/{z}/{x}/{y}.png", {
            attribution: "Map data (c) <a href='http://www.openstreetmap.org/'>OpenStreetMap</a> contributors, <a href='http://creativecommons.org/licenses/by-sa/2.0/'>CC-BY-SA</a>",
            subdomains: [
                'tiles1',
                'tiles2',
                'tiles3',
                'tiles4'
            ]
        });
        map.addLayer(tiles);
    }
    var center = new L.LatLng(lat, lng);
    map.panTo(center);
    resize_listener(center);
}

function show_user_marker(lat, lng) {
    var ll = new L.LatLng(lat, lng);
    if (user_marker != null) {
        map.removeLayer(user_marker);
        user_marker = null;
    }
    user_marker = new L.Marker(ll, { draggable: true });
    map.addLayer(user_marker);
    user_marker.on('dragend', function() {
        ll = user_marker.getLatLng();
        geocode(ll)
    });
}

function geocode(query) {
    if (typeof(query) == 'string') {
        gr = { 'address': query };
    } else {
        gr = { 'location': new google.maps.LatLng(query.lat, query.lng) };
    }
    geocoder.geocode(gr, handle_geocode);
}

function handle_geocode(results, status) {
    lat = results[0].geometry.location.lat();
    lng = results[0].geometry.location.lng();
    normalized_address = results[0].formatted_address;
    $('#location-form #address').val(normalized_address);
    process_location(lat, lng);
}

function process_location(lat, lng) {
    lat = Math.round(lat*10000)/10000;
    lng = Math.round(lng*10000)/10000;
    $('#resultinfo').html(
        _.template($("#search_template").html(), {
            lat: lat,
            lng: lng
        })
    );
    init_map(lat, lng);
    show_user_marker(lat, lng);
    get_boundaries(lat, lng);
}

// Use boundary service to lookup what areas the location falls within
function get_boundaries(lat, lng) {
    var query_url = '/1.0/boundary/?limit=100&contains=' + lat + ',' + lng + '';
    displayed_kind = null;
    for_display = null;
    if (displayed_polygon != null) {
        // Hide old polygon
        displayed_kind = boundaries[displayed_slug].kind;
        map.removeLayer(displayed_polygon);
        displayed_polygon = null;
        displayed_slug = null;
    }
    // Put in a spinner.
    $("#area-lookup").html('<center><img src="{{ STATIC_URL }}img/ajax-loader.gif"></center>');
    // Clear old boundaries
    boundaries.length = 0;
    $.getJSON(query_url, function(data) {
        $.each(data.objects, function(i, obj) {
            boundaries[obj.slug] = obj;
            // Try to display a new polygon of the same kind as the last shown
            if (displayed_kind != null && obj.kind == displayed_kind) {
                for_display = obj; 
            }
        });
        $('#area-lookup').html(
            _.template($("#results_template").html(), {
                data: data
            })
        );
        if (for_display != null) {
            display_boundary(for_display.slug, true);
        }
    });
}

function display_boundary(slug, no_fit) {
    // Clear old polygons
    $("#boundaries .info").removeClass("info");
    if (displayed_polygon != null) {
        map.removeLayer(displayed_polygon);
        displayed_polygon = null;
        displayed_slug = null;
    }
    // Construct new polygons
    var coords = boundaries[slug]["simple_shape"].coordinates;
    var paths = [];
    var bounds = null;
    $.each(coords, function(i, n){
        $.each(n, function(j, o){
            var path = [];
            $.each(o, function(k,p){
                var ll = new L.LatLng(p[1], p[0]);
                path.push(ll);
                if (bounds === null) {
                    bounds = new L.LatLngBounds(ll, ll);
                } else {
                    bounds.extend(ll);
                }
            });
            paths.push(path);
        });
    });
    displayed_polygon = new L.Polygon(paths, {
        color: "#244f79",
        opacity: 0.8,
        weight: 3,
        fill: true,
        fillColor: "#2262CC",
        fillOpacity: 0.2
    });
    displayed_slug = slug;
    map.addLayer(displayed_polygon);
    $("#boundaries #" + slug).addClass("info");
    if (!no_fit) {
        map.fitBounds(bounds);
    }
}

/* DOM EVENT HANDLERS */
function resize_listener(center) {
    $(this).bind('resize_end', function(){ 
        if (map) {
            map.panTo(center);
        }
    });
}

function resize_end_trigger() {
    $(window).resize(function() {
        if (this.resizeto) { 
            clearTimeout(this.resizeto) 
        };
        this.resizeto = setTimeout(function() { 
            $(this).trigger('resize_end'); 
        }, 500);
    });
}

function use_default_location() {
    process_location(default_lat, default_lon);
}

function address_search() {
    geocode($("#location-form #address").val());
    return false;
}

$(document).ready(function() {
    $('#use-default-location').click(use_default_location);
    $('#location-form').geocodify({
        onSelect: function (result) { 
            var location = result.geometry.location;
            $('#resultwarning').hide();
            process_location(location.lat(), location.lng());
        },
        initialText: "Enter an address in Southern California",
        regionBias: 'US',
        viewportBias: new google.maps.LatLngBounds(
            new google.maps.LatLng(minX, minY),
            new google.maps.LatLng(maxX, maxY)
        ),
        filterResults: function(results) {
         var filteredResults =[];
         $.each(results, function(i,val) {
             var location = val.geometry.location;
             if (location.lng() > minY && location.lng() < maxY) {
                 if (location.lat() > minX && location.lat() < maxX) {
                     filteredResults.push(val);
                }
             }
         });
         return filteredResults;
        }
    });
    resize_end_trigger(); 
    use_default_location();
});
