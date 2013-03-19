from datetime import date
from boundaryservice import utils


SHAPEFILES = {
    'Counties (2012)': {
        'file': 'counties/2012/counties.shp',
        'singular': 'County',
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
    }
}
