// Set global variables
var finder_settings = finder_settings || {},
    finder_setting,
    southwest_limit,
    northeast_limit,
    default_lat,
    default_lon,
    place;

// Pull in the bbox
finder_setting = finder_settings.EXAMPLE_PLACE_BBOX.split(',');
southwest_limit = new L.LatLng(parseFloat(finder_setting[0]), parseFloat(finder_setting[1]));
northeast_limit = new L.LatLng(parseFloat(finder_setting[2]), parseFloat(finder_setting[3]));

// Pull in the center
finder_setting = finder_settings.EXAMPLE_PLACE_LAT_LNG.split(',');
default_lat = parseFloat(finder_setting[0]);
default_lon = parseFloat(finder_setting[1]);

// Pull in the default place
place = finder_settings.EXAMPLE_PLACE;

// More globals
var geolocate_supported = true; // until prove false
var geocoder = new google.maps.Geocoder();
var bounding_box = new L.LatLngBounds(southwest_limit, northeast_limit);
var outside = false; // until prove true
var map = null;
var user_marker = null;
var displayed_slug = null;
var displayed_polygon = null;
var boundaries = new Array();

// Bootstrap the map
function init_map(lat, lng) {
    if (map == null) {
        var ll = new L.LatLng(lat, lng);
        map = new L.Map('map_canvas', {
            zoom: 14,
            center: ll,
            maxZoom: 15,
            minZoom:8
        });
        tiles = new L.TileLayer("http://{s}.latimes.com/quiet-la-0.2.4/{z}/{x}/{y}.png", {
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
    check_for_locale(center);
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

function geolocate() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(geolocation_success, geolocation_error);
    } else {
        use_default_location();
        $('#resultinfo').prepend("Your browser does not support determining your location, so we're showing " + place + ".");
        geolocate_supported = false;
    }
}

function geolocation_success(position) {
    process_location(position.coords.latitude, position.coords.longitude)
    ll = new L.LatLng(position.coords.latitude, position.coords.longitude);
    geocode(ll);
    check_for_locale(ll);
}

function geolocation_error() {
    use_default_location();
    $('#resultinfo').prepend("Your browser does not support automatically determining your location so we're showing you " + place + ".");
}

function process_location(lat, lng) {
    lat = Math.round(lat*10000)/10000;
    lng = Math.round(lng*10000)/10000;
    $('#resultinfo').html(
        '<div class="row"><div class="span12"><h3>This search:</h3></div></div>' +
        '<div class="row"><div class="span6">' +
        '<table class="table table-bordered table-hover">' +
        '<tr><th>Latitude</th><td>' + lat + '</td>' +
        '<th>Longitude</th><td>' + lng + '</td></tr>' +
        '</table></div>' + 
        '<div class="span6"><table class="table table-bordered table-hover">' + 
        '<tr><th>API</th><td>' +
        '<a target="_blank" href="' + '/1.0/boundary/?limit=100&contains=' +
        lat + ',' + lng + '">JSON</a>, ' +
        '<a target="_blank" href="' + '/1.0/boundary/?limit=100&contains=' +
        lat + ',' + lng + '&format=jsonp">JSONP</a>' +
        '</td></tr></table></div></div>'
    );
    init_map(lat, lng);
    show_user_marker(lat, lng);
    get_boundaries(lat, lng);
}

function check_for_locale(center) {
    if (!bounding_box.contains(center)) {
        show_outside();
        outside = true;
    } else {
        hide_outside();
        outside = false;
    }
}


// Use boundary service to lookup what areas the location falls within
function get_boundaries(lat, lng) {
    var table_html = '<h3>This location is within:</h3>' +
        '<table class="table table-bordered table-hover" id="boundaries">' +
        '<thead><tr><th>Set</th><th>Boundary</th><th>API</th></tr></thead>';
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

    // Clear old boundaries
    boundaries.length = 0;

    $.getJSON(query_url, function(data) {
        $.each(data.objects, function(i, obj) {
            boundaries[obj.slug] = obj;
            table_html += '<tr id="' + obj.slug + '"><td>' + 
                obj.kind + '</td><td><a href="javascript:display_boundary(\'' 
                + obj.slug + '\');">' + obj.name + '</a></td>' + 
                '<td>' +
                '<a target="_blank" href="' + obj.resource_uri + '">JSON</a>, ' + 
                '<a target="_blank" href="' + obj.resource_uri + '?format=jsonp">JSONP</a>, ' + 
                '<a target="_blank" href="' + obj.resource_uri + '?format=geojson">GeoJSON</a>, ' + 
                '<a target="_blank" href="' + obj.resource_uri + '?format=kml">KML</a>' + 
                '</td></tr>';
            // Try to display a new polygon of the same kind as the last shown
            if (displayed_kind != null && obj.kind == displayed_kind) {
                for_display = obj; 
            }
        });
        table_html += '</table>';
        $('#area-lookup').html(table_html);

        if (for_display != null) {
            display_boundary(for_display.slug, true);
        }
    });
}

function display_boundary(slug, no_fit) {
    // Clear old polygons
    if (displayed_polygon != null) {
        map.removeLayer(displayed_polygon);
        displayed_polygon = null;
        displayed_slug = null;

        $("#boundaries .selected").removeClass("info");
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
        fillColor: "#244f79",
        fillOpacity: 0.2
    });

    displayed_slug = slug;
    map.addLayer(displayed_polygon);

    $("#boundaries #" + slug).addClass("info");

    if (!no_fit) {
        map.fitBounds(bounds);
    }
}


function switch_page(page_id) {
    if (outside) {
        show_outside();
    }

    resize_end_trigger(); 

    if (!map) {
       geolocate();
    }
}


function show_outside() {
    $('#outside').fadeIn(500);
}

function hide_outside() {
    $('#outside').fadeOut(250);
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

function not_where_i_am() {
    show_search();
}

function use_current_location() {
    geolocate();
}

function use_default_location() {
    process_location(default_lat, default_lon);
}


function search_focused() {
    if(this.value == 'Enter an address or drag the pin on the map') {
        $(this).val("");
    }
}

function address_search() {
    geocode($("#location-form #address").val());
    return false;
}

$(document).ready(function() {
    // Setup handlers
    $('#not-where-i-am').click(not_where_i_am);
    $('#use-current-location').click(use_current_location);
    $('#use-default-location').click(use_default_location);
    $('#location-form input[type=text]').focus(search_focused);
    $('#location-form').submit(address_search)
    switch_page();
});


