from datetime import date
from boundaryservice import utils


SHAPEFILES = {
    'LAFD First-in Districts': {
        'file': 'lafd/first-in-districts.shp',
        'singular': 'LAFD First-in District',
        'kind_first': True,
        'ider': utils.simple_namer(['FIRSTIN']),
        'namer': utils.simple_namer(['FIRSTIN']),
        'authority': 'Los Angeles Fire Department',
        'domain': 'Los Angeles City',
        'last_updated': date(2009, 1, 27),
        'href': '',
        'notes': 'The lowest level of administrative organization in the Los Angeles Fire Department',
        'encoding': '',
        'srid': '4326',
        'simplification': 0.0001,
    },
    'LAFD Battalions': {
        'file': 'lafd/battalions.shp',
        'singular': 'LAFD Battalion',
        'kind_first': True,
        'ider': utils.simple_namer(['BATTALION']),
        'namer': utils.simple_namer(['BATTALION']),
        'authority': 'Los Angeles Fire Department',
        'domain': 'Los Angeles City',
        'last_updated': date(2009, 1, 27),
        'href': '',
        'notes': 'The middle level of administrative organization in the Los Angeles Fire Department',
        'encoding': '',
        'srid': '4326',
        'simplification': 0.0001,
    },
    'LAFD Divisions': {
        'file': 'lafd/divisions.shp',
        'singular': 'LAFD Division',
        'kind_first': True,
        'ider': utils.simple_namer(['DIVISION']),
        'namer': utils.simple_namer(['DIVISION']),
        'authority': 'Los Angeles Fire Department',
        'domain': 'Los Angeles City',
        'last_updated': date(2009, 1, 27),
        'href': '',
        'notes': 'The highest level of administrative organization in the Los Angeles Fire Department',
        'encoding': '',
        'srid': '4326',
        'simplification': 0.0001,
    },
    'L.A. County Regions (V5)': {
        'file': 'neighborhoods/v5/regions.shp',
        'singular': 'L.A. County Region (V5)',
        'kind_first': False,
        'ider': utils.simple_namer(['slug']),
        'namer': utils.simple_namer(['name']),
        'authority': 'Los Angles Times',
        'domain': 'Los Angeles County',
        'last_updated': date(2010, 5, 24),
        'href': 'http://projects.latimes.com/mapping-la/about/',
        'notes': 'The fifth version of Los Angeles County regions as defined by the Los Angeles Times',
        'encoding': '',
        'srid': '4326',
        'simplification': 0.0001,
    },
    'L.A. County Municipal Regions (V5)': {
        'file': 'neighborhoods/v5/municipalregions.shp',
        'singular': 'L.A. County Municipal Region (V5)',
        'kind_first': False,
        'ider': utils.simple_namer(['slug']),
        'namer': utils.simple_namer(['name']),
        'authority': 'Los Angles Times',
        'domain': 'Los Angeles County',
        'last_updated': date(2010, 5, 24),
        'href': 'http://projects.latimes.com/mapping-la/about/',
        'notes': 'The fifth version of Los Angeles County municipal regions as defined by the Los Angeles Times',
        'encoding': '',
        'srid': '4326',
        'simplification': 0.0001,
    },
    'L.A. County Neighborhoods (V5)': {
        'file': 'neighborhoods/v5/neighborhoods.shp',
        'singular': 'L.A. County Neighborhood (V5)',
        'kind_first': False,
        'ider': utils.simple_namer(['slug']),
        'namer': utils.simple_namer(['name']),
        'authority': 'Los Angles Times',
        'domain': 'Los Angeles County',
        'last_updated': date(2010, 5, 24),
        'href': 'http://projects.latimes.com/mapping-la/about/',
        'notes': 'The fifth version of Los Angeles County neighborhoods as defined by the Los Angeles Times',
        'encoding': '',
        'srid': '4326',
        'simplification': 0.0001,
    },
#    'L.A. County Law Enforcement Reporting Districts': {
#        'file': 'law-enforcement-reporting-districts/la_county.shp',
#        'singular': 'L.A. County Law Enforcement Reporting District',
#        'kind_first': False,
#        'ider': utils.simple_namer(['OBJECTID'], normalizer=int),
#        'namer': utils.simple_namer(['LABEL', 'RD'], seperator=" #"),
#        'authority': 'State of California GeoPortal',
#        'domain': 'Los Angeles County',
#        'last_updated': date(2010, 1, 1),
#        'href': 'http://portal.gis.ca.gov/geoportal/catalog/search/resource/details.page?uuid=%7BD3790AB4-881E-4B18-9217-A4459D9E0720%7D',
#        'notes': 'Reporting Districts from cities come from early 2000\'s. Sheriff reporting districts are as of January 2010. LAPD reporting districts are as of January 2010.',
#        'encoding': '',
#        'srid': '4326',
#        'simplification': 0.0001,
#    },
    'L.A. City Council Districts (1993)': {
        'file': 'la-city-council/1993/la-city-council-1993.shp',
        'singular': 'L.A. City Council District (1993)',
        'kind_first': False,
        'ider': utils.simple_namer(['District'], normalizer=int),
        'namer': utils.simple_namer(['District'], normalizer=int),
        'authority': 'Unknown',
        'domain': 'Los Angeles',
        'last_updated': date(2013, 3, 20),
        'href': '',
        'notes': 'Acquired by former Los Angeles Times reporter Dick O\'Reilly from origins unknown.',
        'encoding': '',
        'srid': '4326',
        'simplification': 0.0001,
    },
    'L.A. City Council Districts (2002)': {
        'file': 'la-city-council/2002/la-city-council-2002.shp',
        'singular': 'L.A. City Council District (2002)',
        'kind_first': False,
        'ider': utils.simple_namer(['District'], normalizer=int),
        'namer': utils.simple_namer(['District'], normalizer=int),
        'authority': 'Los Angeles County GIS Data Portal',
        'domain': 'Los Angeles',
        'last_updated': date(2002, 4, 5),
        'href': 'http://egis3.lacounty.gov/dataportal/2011/05/02/la-city-council-districts/',
        'notes': '',
        'encoding': '',
        'srid': '4326',
        'simplification': 0.0001,
    },
    'L.A. City Council Districts (2012)': {
        'file': 'la-city-council/2012/la-city-council.shp',
        'singular': 'L.A. City Council District (2012)',
        'kind_first': False,
        'ider': utils.simple_namer(['District'], normalizer=int),
        'namer': utils.simple_namer(['District'], normalizer=int),
        'authority': 'Los Angeles City Council Redistricting Commission',
        'domain': 'Los Angeles',
        'last_updated': date(2012, 3, 16),
        'href': 'http://redistricting2011.lacity.org/LACITY/approvedMap.html',
        'notes': 'The final boundaries adopted by the City Council.',
        'encoding': '',
        'srid': '4326',
        'simplification': 0.0001,
    },
    'Counties (2012)': {
        'file': 'counties/2012/counties.shp',
        'singular': 'County (2012)',
        'kind_first': False,
        'ider': utils.simple_namer(['FIPS']),
        'namer': utils.simple_namer(['Name']),
        'authority': 'United States Census Bureau',
        'domain': 'California',
        'last_updated': date(2013, 3, 18),
        'href': 'http://www.census.gov/cgi-bin/geo/shapefiles2012/main',
        'notes': 'County boundaries clipped at the shoreline. Fields names simplified and many fields removed.',
        'encoding': '',
        'srid': '4326',
        'simplification': 0.0001,
    },
}
