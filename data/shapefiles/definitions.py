from datetime import date
from boundaryservice import utils


SHAPEFILES = {
    'Los Angeles City Council Districts (1993)': {
        'file': 'la-city-council/1993/la-city-council-1993.shp',
        'singular': 'Los Angeles City Council District (1993)',
        'kind_first': False,
        'ider': utils.simple_namer(['District'], normalizer=int),
        'namer': utils.simple_namer(['District'], normalizer=int),
        'authority': 'Unknown',
        'domain': 'Los Angeles',
        'last_updated': date(2013, 3, 20),
        'href': 'http://egis3.lacounty.gov/dataportal/2011/05/02/la-city-council-districts/',
        'notes': 'Acquired by former Los Angeles Times reporter Dick O\'Reilly from origins unknown.',
        'encoding': '',
        'srid': '4326',
        'simplification': 0.0001,
    },
#    'Los Angeles City Council Districts (2002)': {
#        'file': 'la-city-council/2002/la-city-council-2002.shp',
#        'singular': 'Los Angeles City Council District (2002)',
#        'kind_first': False,
#        'ider': utils.simple_namer(['District'], normalizer=int),
#        'namer': utils.simple_namer(['District'], normalizer=int),
#        'authority': 'Los Angeles County GIS Data Portal',
#        'domain': 'Los Angeles',
#        'last_updated': date(2002, 4, 5),
#        'href': 'http://egis3.lacounty.gov/dataportal/2011/05/02/la-city-council-districts/',
#        'notes': '',
#        'encoding': '',
#        'srid': '4326',
#        'simplification': 0.0001,
#    },
#    'Los Angeles City Council Districts (2012)': {
#        'file': 'la-city-council/2012-adopted/la-city-council.shp',
#        'singular': 'Los Angeles City Council District (2012)',
#        'kind_first': False,
#        'ider': utils.simple_namer(['District'], normalizer=int),
#        'namer': utils.simple_namer(['District'], normalizer=int),
#        'authority': 'Los Angeles City Council Redistricting Commission',
#        'domain': 'Los Angeles',
#        'last_updated': date(2012, 3, 16),
#        'href': 'http://redistricting2011.lacity.org/LACITY/approvedMap.html',
#        'notes': '',
#        'encoding': '',
#        'srid': '4326',
#        'simplification': 0.0001,
#    },
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
