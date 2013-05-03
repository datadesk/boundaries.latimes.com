from datetime import date
from boundaryservice import utils


SHAPEFILES = {
    'L.A. County Sheriff Station Areas': {
        'file': 'la-county-sheriff/station-areas.shp',
        'singular': 'L.A. County Sheriff Station Area',
        'kind_first': False,
        'ider': utils.simple_namer(['name']),
        'namer': utils.simple_namer(['name']),
        'authority': 'L.A. County Sheriff',
        'domain': 'Los Angeles County',
        'last_updated': date(2011, 12, 23),
        'href': '',
        'notes': 'Administrative districts of the Los Angeles County Sheriff\'s Department',
        'encoding': '',
        'srid': '4326',
        'simplification': 0.0001,
    },
    'L.A. County Sheriff Reporting Districts': {
        'file': 'la-county-sheriff/reporting-districts.shp',
        'singular': 'L.A. County Sheriff Reporting District',
        'kind_first': False,
        'ider': utils.simple_namer(['name']),
        'namer': utils.simple_namer(['name']),
        'authority': 'L.A. County Sheriff',
        'domain': 'Los Angeles County',
        'last_updated': date(2011, 12, 23),
        'href': '',
        'notes': 'Administrative districts of the Los Angeles County Sheriff\'s Department',
        'encoding': '',
        'srid': '4326',
        'simplification': 0.0001,
    },
    'LAPD Bureaus': {
        'file': 'lapd/bureaus.shp',
        'singular': 'LAPD Bureau',
        'kind_first': False,
        'ider': utils.simple_namer(['name']),
        'namer': utils.simple_namer(['name']),
        'authority': 'Los Angeles Police Department',
        'domain': 'Los Angeles city',
        'last_updated': date(2011, 12, 23),
        'href': '',
        'notes': 'Administrative districts of the Los Angeles Police Department',
        'encoding': '',
        'srid': '4326',
        'simplification': 0.0001,
    },
    'LAPD Divisions': {
        'file': 'lapd/divisions.shp',
        'singular': 'LAPD Division',
        'kind_first': False,
        'ider': utils.simple_namer(['number']),
        'namer': utils.simple_namer(['name']),
        'authority': 'Los Angeles Police Department',
        'domain': 'Los Angeles city',
        'last_updated': date(2011, 12, 23),
        'href': '',
        'notes': 'Administrative districts of the Los Angeles Police Department',
        'encoding': '',
        'srid': '4326',
        'simplification': 0.0001,
    },
    'LAPD Basic Car Areas': {
        'file': 'lapd/basic-car-areas.shp',
        'singular': 'LAPD Basic Car Area',
        'kind_first': False,
        'ider': utils.simple_namer(['number']),
        'namer': utils.simple_namer(['number']),
        'authority': 'Los Angeles Police Department',
        'domain': 'Los Angeles city',
        'last_updated': date(2011, 12, 23),
        'href': '',
        'notes': 'Administrative districts of the Los Angeles Police Department',
        'encoding': '',
        'srid': '4326',
        'simplification': 0.0001,
    },
    'LAPD Reporting Districts': {
        'file': 'lapd/reporting-districts.shp',
        'singular': 'LAPD Reporting District',
        'kind_first': False,
        'ider': utils.simple_namer(['number']),
        'namer': utils.simple_namer(['number']),
        'authority': 'Los Angeles Police Department',
        'domain': 'Los Angeles city',
        'last_updated': date(2011, 12, 23),
        'href': '',
        'notes': 'Administrative districts of the Los Angeles Police Department',
        'encoding': '',
        'srid': '4326',
        'simplification': 0.0001,
    },
    'L.A. County Board of Supervisors Districts (1971)': {
        'file': 'la-county-supervisors/1971/districts.shp',
        'singular': 'L.A. County Board of Supervisors District (1971)',
        'kind_first': False,
        'ider': utils.simple_namer(['DISTRICT']),
        'namer': utils.simple_namer(['DISTRICT']),
        'authority': 'L.A. County GIS Data Portal',
        'domain': 'Los Angeles County',
        'last_updated': date(2011, 8, 11),
        'href': 'http://egis3.lacounty.gov/dataportal/2011/09/28/historic-la-county-supervisorial-districts-1971-1991/',
        'notes': 'Political districts for L.A. County Board of Supervisors',
        'encoding': '',
        'srid': '4326',
        'simplification': 0.0001,
    },
    'L.A. County Board of Supervisors Districts (1981)': {
        'file': 'la-county-supervisors/1981/districts.shp',
        'singular': 'L.A. County Board of Supervisors District (1981)',
        'kind_first': False,
        'ider': utils.simple_namer(['DISTRICT']),
        'namer': utils.simple_namer(['DISTRICT']),
        'authority': 'L.A. County GIS Data Portal',
        'domain': 'Los Angeles County',
        'last_updated': date(2011, 8, 11),
        'href': 'http://egis3.lacounty.gov/dataportal/2011/09/28/historic-la-county-supervisorial-districts-1971-1991/',
        'notes': 'Political districts for L.A. County Board of Supervisors',
        'encoding': '',
        'srid': '4326',
        'simplification': 0.0001,
    },
    'L.A. County Board of Supervisors Districts (1991)': {
        'file': 'la-county-supervisors/1991/districts.shp',
        'singular': 'L.A. County Board of Supervisors District (1991)',
        'kind_first': False,
        'ider': utils.simple_namer(['DISTRICT']),
        'namer': utils.simple_namer(['DISTRICT']),
        'authority': 'L.A. County GIS Data Portal',
        'domain': 'Los Angeles County',
        'last_updated': date(2003, 7, 9),
        'href': 'http://egis3.lacounty.gov/dataportal/2011/09/28/historic-la-county-supervisorial-districts-1971-1991/',
        'notes': 'Political districts for L.A. County Board of Supervisors',
        'encoding': '',
        'srid': '4326',
        'simplification': 0.0001,
    },
    'L.A. County Board of Supervisors Districts (2001)': {
        'file': 'la-county-supervisors/2001/2001.shp',
        'singular': 'L.A. County Board of Supervisors District (2001)',
        'kind_first': False,
        'ider': utils.simple_namer(['SUP_DIST']),
        'namer': utils.simple_namer(['SUP_DIST']),
        'authority': 'L.A. County GIS Data Portal',
        'domain': 'Los Angeles County',
        'last_updated': date(2011, 8, 17),
        'href': 'http://egis3.lacounty.gov/dataportal/2009/12/23/supervisorial-districts-2001/',
        'notes': 'Political districts for L.A. County Board of Supervisors',
        'encoding': '',
        'srid': '4326',
        'simplification': 0.0001,
    },
    'Service Planning Areas (2012)': {
        'file': 'spas/2012.shp',
        'singular': 'Service Planning Area (2012)',
        'kind_first': False,
        'ider': utils.simple_namer(['SPA_2012']),
        'namer': utils.simple_namer(['SPA_2012']),
        'authority': 'L.A. County GIS Data Portal',
        'domain': 'Los Angeles County',
        'last_updated': date(2012, 2, 14),
        'href': 'http://egis3.lacounty.gov/dataportal/2012/03/01/service-planning-areas-spa-2012/',
        'notes': 'Used by a number of County departments to plan and manage service delivery. Aggregated from Census tracts.',
        'encoding': '',
        'srid': '4326',
        'simplification': 0.0001,
    },
    'Service Planning Areas (2002)': {
        'file': 'spas/2002.shp',
        'singular': 'Service Planning Area (2002)',
        'kind_first': False,
        'ider': utils.simple_namer(['SPA_02']),
        'namer': utils.simple_namer(['SPA_02']),
        'authority': 'L.A. County GIS Data Portal',
        'domain': 'Los Angeles County',
        'last_updated': date(2009, 11, 07),
        'href': 'http://egis3.lacounty.gov/dataportal/2009/11/07/service-planning-areas-spa-2002/',
        'notes': 'Used by a number of County departments to plan and manage service delivery. Aggregated from Census tracts.',
        'encoding': '',
        'srid': '4326',
        'simplification': 0.0001,
    },
    'Local Emergency Medical Services Agencies': {
        'file': 'lemsas/lemsas.shp',
        'singular': 'Local Emergency Medical Services Agency',
        'kind_first': False,
        'ider': utils.simple_namer(['ABBREV']),
        'namer': utils.simple_namer(['NAME']),
        'authority': 'Los Angeles Times',
        'domain': 'California',
        'last_updated': date(2012, 12, 21),
        'href': 'http://datadesk.latimes.com/posts/2012/12/map-of-california-ems-agencies/',
        'notes': 'The regional agencies that regulate emergency medical services in California',
        'encoding': '',
        'srid': '4326',
        'simplification': 0.0001,
    },
    'L.A. County Board of Supervisors Districts (2011)': {
        'file': 'la-county-supervisors/2011/districts.shp',
        'singular': 'L.A. County Board of Supervisors District (2011)',
        'kind_first': False,
        'ider': utils.simple_namer(['DISTRICT']),
        'namer': utils.simple_namer(['DISTRICT']),
        'authority': 'L.A. County GIS Data Portal',
        'domain': 'Los Angeles County',
        'last_updated': date(2011, 9, 28),
        'href': 'http://egis3.lacounty.gov/dataportal/2011/09/28/2011-supervisorial-district-boundaries-approved-september-27-2011/l',
        'notes': 'Political districts for L.A. County Board of Supervisors',
        'encoding': '',
        'srid': '4326',
        'simplification': 0.0001,
    },
    'State Board of Equalization Districts (2011)': {
        'file': 'state-politics-2011/board-of-equalization.shp',
        'singular': 'State Board of Equalization District (2011)',
        'kind_first': False,
        'ider': utils.simple_namer(['DISTRICT']),
        'namer': utils.simple_namer(['DISTRICT']),
        'authority': 'California Citizens Redistricting Commission',
        'domain': 'California',
        'last_updated': date(2011, 8, 15),
        'href': 'http://wedrawthelines.ca.gov/maps-final-drafts.html',
        'notes': 'Political districts for California in the Board of Equalization',
        'encoding': '',
        'srid': '4326',
        'simplification': 0.0001,
    },
    'U.S. Congressional Districts (2011)': {
        'file': 'state-politics-2011/congress.shp',
        'singular': 'U.S. Congressional District (2011)',
        'kind_first': False,
        'ider': utils.simple_namer(['DISTRICT']),
        'namer': utils.simple_namer(['DISTRICT']),
        'authority': 'California Citizens Redistricting Commission',
        'domain': 'California',
        'last_updated': date(2011, 8, 15),
        'href': 'http://wedrawthelines.ca.gov/maps-final-drafts.html',
        'notes': 'Political districts for California in the U.S. Congress',
        'encoding': '',
        'srid': '4326',
        'simplification': 0.0001,
    },
    'State Senate Districts (2011)': {
        'file': 'state-politics-2011/senate.shp',
        'singular': 'State Senate District (2011)',
        'kind_first': False,
        'ider': utils.simple_namer(['DISTRICT']),
        'namer': utils.simple_namer(['DISTRICT']),
        'authority': 'California Citizens Redistricting Commission',
        'domain': 'California',
        'last_updated': date(2011, 8, 15),
        'href': 'http://wedrawthelines.ca.gov/maps-final-drafts.html',
        'notes': 'Political districts for the California State Senate',
        'encoding': '',
        'srid': '4326',
        'simplification': 0.0001,
    },
    'State Assembly Districts (2011)': {
        'file': 'state-politics-2011/assembly.shp',
        'singular': 'State Assembly District (2011)',
        'kind_first': False,
        'ider': utils.simple_namer(['DISTRICT']),
        'namer': utils.simple_namer(['DISTRICT']),
        'authority': 'California Citizens Redistricting Commission',
        'domain': 'California',
        'last_updated': date(2011, 8, 15),
        'href': 'http://wedrawthelines.ca.gov/maps-final-drafts.html',
        'notes': 'Political districts for the California State Assembly',
        'encoding': '',
        'srid': '4326',
        'simplification': 0.0001,
    },
    'County Subdivisions (2012)': {
        'file': 'census-2012/county-subdivisions.shp',
        'singular': 'County Subdivision (2012)',
        'kind_first': False,
        'ider': utils.simple_namer(['GEOID']),
        'namer': utils.simple_namer(['NAME']),
        'authority': 'U.S. Census',
        'domain': 'Southern California',
        'last_updated': date(2012, 7, 27),
        'href': '',
        'notes': 'Statisical areas defined by the Census Bureau',
        'encoding': '',
        'srid': '4326',
        'simplification': 0.0001,
    },
    'Core Based Statistical Areas (2013)': {
        'file': 'census-2013/cbsa.shp',
        'singular': 'Core Based Statistical Area (2012)',
        'kind_first': False,
        'ider': utils.simple_namer(['CBSAFP']),
        'namer': utils.simple_namer(['CBSA_Title']),
        'authority': 'U.S. Census',
        'domain': 'Southern California',
        'last_updated': date(2013, 4, 3),
        'href': '',
        'notes': 'Statisical areas defined by the Census Bureau',
        'encoding': '',
        'srid': '4326',
        'simplification': 0.0001,
    },
    'ZIP Code Tabulation Areas (2012)': {
        'file': 'census-2012/zcta.shp',
        'singular': 'ZIP Code Tabulation Area (2012)',
        'kind_first': False,
        'ider': utils.simple_namer(['GEOID10']),
        'namer': utils.simple_namer(['GEOID10']),
        'authority': 'U.S. Census',
        'domain': 'Southern California',
        'last_updated': date(2012, 7, 27),
        'href': '',
        'notes': 'Statisical areas defined by the Census Bureau',
        'encoding': '',
        'srid': '4326',
        'simplification': 0.0001,
    },
    'Census Blocks (2012)': {
        'file': 'census-2012/blocks-la-county.shp',
        'singular': 'Census Block (2012)',
        'kind_first': False,
        'ider': utils.simple_namer(['GEOID']),
        'namer': utils.simple_namer(['GEOID']),
        'authority': 'U.S. Census',
        'domain': 'Los Angeles County',
        'last_updated': date(2012, 7, 27),
        'href': '',
        'notes': 'Statisical areas defined by the Census Bureau',
        'encoding': '',
        'srid': '4326',
        'simplification': 0.0001,
    },
    'Census Block Groups (2012)': {
        'file': 'census-2012/block-groups-la-county.shp',
        'singular': 'Census Block Group (2012)',
        'kind_first': False,
        'ider': utils.simple_namer(['GEOID']),
        'namer': utils.simple_namer(['GEOID']),
        'authority': 'U.S. Census',
        'domain': 'Los Angeles County',
        'last_updated': date(2012, 7, 27),
        'href': '',
        'notes': 'Statisical areas defined by the Census Bureau',
        'encoding': '',
        'srid': '4326',
        'simplification': 0.0001,
    },
    'Census Tracts (2012)': {
        'file': 'census-2012/tracts-la-county.shp',
        'singular': 'Census Tract (2012)',
        'kind_first': False,
        'ider': utils.simple_namer(['GEOID']),
        'namer': utils.simple_namer(['GEOID']),
        'authority': 'U.S. Census',
        'domain': 'Los Angeles County',
        'last_updated': date(2012, 7, 27),
        'href': '',
        'notes': 'Statisical areas defined by the Census Bureau',
        'encoding': '',
        'srid': '4326',
        'simplification': 0.0001,
    },
    'Census Places (2012)': {
        'file': 'census-2012/places.shp',
        'singular': 'Census Place (2012)',
        'kind_first': False,
        'ider': utils.simple_namer(['NAME']),
        'namer': utils.simple_namer(['NAME']),
        'authority': 'U.S. Census',
        'domain': 'California',
        'last_updated': date(2012, 7, 27),
        'href': '',
        'notes': 'Cities and other census-defined places',
        'encoding': '',
        'srid': '4326',
        'simplification': 0.0001,
    },
    'L.A. County Fire Dept. Station Areas': {
        'file': 'la-county-fd/station-areas.shp',
        'singular': 'L.A. County Fire Dept. Station Area',
        'kind_first': True,
        'ider': utils.simple_namer(['STATID']),
        'namer': utils.simple_namer(['STATID']),
        'authority': 'Los Angeles County Fire Department',
        'domain': 'Los Angeles County',
        'last_updated': date(2011, 3, 1),
        'href': '',
        'notes': 'The administrative organization of the Los Angeles County Fire Department',
        'encoding': '',
        'srid': '4326',
        'simplification': 0.0001,
    },
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
