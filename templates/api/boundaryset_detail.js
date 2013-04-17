{% load toolbox_tags %}

var sw = new L.LatLng(31.5037, -122.3272);
var ne = new L.LatLng(36.1912, -112.044);
var map = new L.Map('map-canvas', {
    zoom: 14,
    maxZoom: 15,
    minZoom:8,
    maxBounds: new L.LatLngBounds(
        new L.LatLng(36.1912, -112.044),
        new L.LatLng(31.5037, -122.3272)
    )
});
map.fitBounds(new L.LatLngBounds(sw, ne));
tiles = new L.TileLayer("http://{s}.latimes.com/quiet-la-0.2.5/{z}/{x}/{y}.png", {
    attribution: "Map data (c) <a href='http://www.openstreetmap.org/'>OpenStreetMap</a> contributors, <a href='http://creativecommons.org/licenses/by-sa/2.0/'>CC-BY-SA</a>",
    subdomains: [
        'tiles1',
        'tiles2',
        'tiles3',
        'tiles4'
    ]
});
map.addLayer(tiles);
var features = {
    "type": "FeatureCollection",
    "features": [{% for obj in boundary_list %}{
        "id": {{ obj.id }},
        "type": "Feature",
        "properties": {
            "kind": "{{ obj.kind }}",
            "external_id": "{{ obj.external_id }}",
            "name": "{{ obj.name }}",
            "display_name": "{{ obj.display_name }}",
            "slug": "{{ obj.slug }}",
            "metadata": {{ obj.metadata|jsonify|safe }}
        },
        "geometry": {{ obj.simple_shape.json|safe }}
    }{% if not forloop.last %},{% endif %}
    {% endfor %}]
};

var defaultStyle = {
    weight: 1,
    color: "#2662CC",
    opacity: 0.75,
    fill: true,
    fillColor: "#2262CC",
    fillOpacity: 0.2
};

var highlightStyle = {
    weight: 3,
    color: "#244f79",
    opacity: 1,
    fill: true,
    fillColor: "#2262CC",
    fillOpacity: 0.5
};

var selected;

var onEachFeature = function(feature, layer) {
    (function(layer, feature) {
      layer.on("click", function (e) {
          if (feature.id === selected) {
            jsonLayer.resetStyle(layer);
            $('#resultinfo').html("");
            return false;
          }
          jsonLayer.eachLayer(function(l){jsonLayer.resetStyle(l);});
          layer.setStyle(highlightStyle);
          $('#resultinfo').html(
            _.template($("#boundary_template").html(), {
                obj: feature.properties
            })
          );
          selected = feature.id;
          return false;
      });
    })(layer, feature);
};

var jsonLayer = new L.geoJson(features, {
    style: defaultStyle,
    onEachFeature: onEachFeature
}).addTo(map);
