import re

ZIPCODE_REGEX = re.compile(r'^(.*)\d{5}([\-]\d{4})?(.*)$')
CHARACTERS_ONLY_REGEX = re.compile(r'[^A-Za-z]')

WHITESPACE_RE = re.compile(r'\s+', re.M)
SPACE_RE = re.compile(r'[ \t\f\v]+', re.M)
NEWLINE_RE = re.compile(r'[\n\r]+', re.M)
