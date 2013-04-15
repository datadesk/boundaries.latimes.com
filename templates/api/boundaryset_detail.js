var sw = new L.LatLng(31.5037, -122.3272);
var ne = new L.LatLng(36.1912, -112.044);
var map = new L.Map('map-canvas', {
    zoom: 14,
    maxZoom: 15,
    minZoom:8
});
map.fitBounds(new L.LatLngBounds(sw, ne));
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
