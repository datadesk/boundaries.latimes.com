from datetime import date
from boundaryservice import utils


SHAPEFILES = {
    'Los Angeles City Council Districts (2012)': {
        'file': 'la-city-council/2012-adopted/la-city-council.shp',
        'singular': 'Los Angeles City Council District',
        'kind_first': True,
        'ider': utils.simple_namer(['District'], normalizer=int),
        'namer': utils.simple_namer(['District'], normalizer=int),
        'authority': 'Los Angeles City Council Redistricting Commission',
        'domain': 'Los Angeles',
        'last_updated': date(2012, 3, 16),
        'href': 'http://redistricting2011.lacity.org/LACITY/approvedMap.html',
        'notes': '',
        'encoding': '',
        'srid': '4326',
        'simplification': 0.0001,
    },
#    'Counties (2012)': {
#        'file': 'counties/2012/counties.shp',
#        'singular': 'County',
#        'kind_first': False,
#        'ider': utils.simple_namer(['FIPS']),
#        'namer': utils.simple_namer(['Name']),
#        'authority': 'United States Census Bureau',
#        'domain': 'California',
#        'last_updated': date(2013, 3, 18),
#        'href': 'http://www.census.gov/cgi-bin/geo/shapefiles2012/main',
#        'notes': 'County boundaries clipped at the shoreline. Fields names simplified and many fields removed.',
#        'encoding': '',
#        'srid': '4326',
#        'simplification': 0.0001,
#    },
}
