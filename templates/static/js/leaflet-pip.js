
(function(e) {
    if ("function" == typeof bootstrap) bootstrap("leafletpip", e);
    else if ("object" == typeof exports) module.exports = e();
    else if ("function" == typeof define && define.amd) define(e);
    else if ("undefined" != typeof ses) {
        if (!ses.ok()) return;
        ses.makeLeafletPip = e
    } else "undefined" != typeof window ? window.leafletPip = e() : global.leafletPip = e()
})(function() {
    return function(e, t, n) {
        function r(n, i) {
            if (!t[n]) {
                if (!e[n]) {
                    var s = "function" == typeof require && require;
                    if (!i && s) return s(n, !0);
                    throw Error("Cannot find module '" + n + "'")
                }
                var o = t[n] = {
                    exports: {}
                };
                e[n][0](function(t) {
                    var i = e[n][1][t];
                    return r(i ? i : t)
                }, o, o.exports)
            }
            return t[n].exports
        }
        for (var i = 0; n.length > i; i++) r(n[i]);
        return r
    }({
        1: [function(require, module) {
            function getLls(l) {
                for (var lls = l.getLatLngs(), o = [], i = 0; lls.length > i; i++) o[i] = [lls[i].lng, lls[i].lat];
                return o
            }
            var pip = require("point-in-polygon"),
                leafletPip = {
                    bassackwards: !1,
                    pointInLayer: function(p, layer, first) {
                        "use strict";
                        if (!(layer instanceof L.GeoJSON)) throw Error("must be L.GeoJSON");
                        p instanceof L.LatLng && (p = [p.lng, p.lat]), leafletPip.bassackwards && p.reverse();
                        var results = [];
                        return layer.eachLayer(function(l) {
                            if (!first || !results.length) {
                                var lls = [];
                                l instanceof L.MultiPolygon ? l.eachLayer(function(sub) {
                                    lls.push(getLls(sub))
                                }) : l instanceof L.Polygon && lls.push(getLls(l));
                                for (var i = 0; lls.length > i; i++) pip(p, lls[i]) && results.push(l)
                            }
                        }), results
                    }
                };
            module.exports = leafletPip
        }, {
            "point-in-polygon": 2
        }],
        2: [function(require, module) {
            module.exports = function(point, vs) {
                for (var x = point[0], y = point[1], inside = !1, i = 0, j = vs.length - 1; vs.length > i; j = i++) {
                    var xi = vs[i][0],
                        yi = vs[i][1],
                        xj = vs[j][0],
                        yj = vs[j][1],
                        intersect = yi > y != yj > y && (xj - xi) * (y - yi) / (yj - yi) + xi > x;
                    intersect && (inside = !inside)
                }
                return inside
            }
        }, {}]
    }, {}, [1])(1)
}); 
