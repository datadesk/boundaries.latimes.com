"""
A collection of miscellaneous string filters that we use to dress up our data.
"""
# Templatetag helpers
from django import template
from django.utils.safestring import mark_safe, SafeData
from django.template.defaultfilters import stringfilter

# Text maniuplation
import re
from django.utils.functional import allow_lazy
from django.utils.html import escape
from django.utils.encoding import force_unicode
from django.utils.text import normalize_newlines
from toolbox.regex import CHARACTERS_ONLY_REGEX, SPACE_RE
from toolbox.regex import NEWLINE_RE, WHITESPACE_RE

# Open up the templatetag registry
register = template.Library()

#
# Replacement filters
#

def collapse_whitespace(value):
    """
    Replaces multiple instances of whitespace with a single space, including newlines.
        ...    
        >>> from toolbox.templatetags.misc_tags import collapse_whitespace
        >>> collapse_whitespace('This     is a    \r\n\r\n\r\n test   \n\n  OK?')
        u'This is a test OK?'
    """
    return mark_safe(re.sub(WHITESPACE_RE, ' ', value))
collapse_whitespace.is_safe = True
collapse_whitespace = stringfilter(collapse_whitespace)
register.filter(collapse_whitespace)

def datejs(dt):
    """
    Reformats a datetime object as a JavaScript Date() object.
    """
    if hasattr(dt, 'hour') and hasattr(dt, 'minute') and hasattr(dt, 'second'):
        js = 'Date(%s, %s, %s, %s, %s, %s)' % (
            dt.year, dt.month-1, dt.day,
            dt.hour, dt.minute, dt.second,
        )
    else:
        js = 'Date(%s, %s, %s)' % (dt.year, dt.month-1, dt.day)
    return mark_safe(js)
datejs.is_safe = True
register.filter(datejs)

def truthjs(val):
    """
    Reformats a boolean object as a JavaScript object.
    """
    if val == True:
        js = 'true'
    elif val == False:
        js = 'false'
    else:
        js = 'null'
    return mark_safe(js)
truthjs.is_safe = True
register.filter(truthjs)

def emdashes(value):
    """
    Replaces '--' with an HTML &mdash;.
    """
    return mark_safe(value.replace("--", "&mdash;"))
emdashes.is_safe = True
emdashes = stringfilter(emdashes)
register.filter(emdashes)

def linebreaksp(value, autoescape=None):
    """Converts all newlines into <p>. No <br />s."""

    def _run(value, autoescape=False):
        value = re.sub(r'\r\n|\r|\n', '\n', force_unicode(value)) # normalize newlines
        value = re.sub('\n{2,}', '\n', value) # Replace multiple newlines with a single
        paras = re.split('\n', value)
        if autoescape:
            paras = [u'<p>%s</p>' % escape(p).replace('\n', '<br />') for p in paras]
        else:
            paras = [u'<p>%s</p>' % p.replace('\n', '<br />') for p in paras]
        return u'\n\n'.join(paras)
    _run = allow_lazy(_run, unicode)

    autoescape = autoescape and not isinstance(value, SafeData)
    return mark_safe(_run(value, autoescape))
linebreaksp.is_safe = True
linebreaksp.needs_autoescape = True
linebreaksp = stringfilter(linebreaksp)
register.filter(linebreaksp)

def title(value):
   """Converts a string into titlecase."""
   t = re.sub("([a-z])'([A-Z])", lambda m: m.group(0).lower(), value.title())
   return re.sub("\d([A-Z])", lambda m: m.group(0).lower(), t)
title.is_safe = True
title = stringfilter(title)

VOWELS = 'aeiou'

def anify(value, arg="n"):
    """
    Determine whether 'a' should become 'an'. Returns 'n' if true.
    """
    if value[0] in VOWELS:
        return arg
    else:
        return ''
anify.is_safe = True
register.filter(anify)

#
# Deletion filters
#

def remove_dupe_whitespace(value):
    """
    Replaces multiple instances of whitespace with a single instance.
        ...    
        >>> from toolbox.templatetags.misc_tags import remove_dupe_whitespace
        >>> remove_dupe_whitespace('This     is a    \r\n\r\n\r\n test   \n\n  OK?')
        u'This is a \n test \n OK?'
    """
    return mark_safe(re.sub(NEWLINE_RE, '\n', re.sub(SPACE_RE, ' ', value)))
remove_dupe_whitespace.is_safe = True
remove_dupe_whitespace = stringfilter(remove_dupe_whitespace)
register.filter(remove_dupe_whitespace)

def remove_newlines(text):
    """
    Removes all newline characters from a block of text.
    """
    # First normalize the newlines using Django's nifty utility
    normalized_text = normalize_newlines(text)
    # Then simply remove the newlines like so.
    return mark_safe(normalized_text.replace('\n', ' '))
remove_newlines.is_safe = True
remove_newlines = stringfilter(remove_newlines)
register.filter(remove_newlines)

def remove_nonchar(text):
    """
    Removes all non-characters from a block of text.
    """
    return mark_safe(CHARACTERS_ONLY_REGEX.sub('', text))
remove_nonchar.is_safe = True
remove_nonchar = stringfilter(remove_nonchar)
register.filter(remove_nonchar)

def remove_whitespace(value):
    """
    Removes all whitespace in the string, concatenating the remaining characters.
    """
    return mark_safe(value.replace(" ", ""))
remove_whitespace.is_safe = True
remove_whitespace = stringfilter(remove_whitespace)
register.filter(remove_whitespace)

def strip(text):
    """
    Removes all non-characters from a block of text.
    """
    return text.strip()
strip.is_safe = True
strip = stringfilter(strip)
register.filter(strip)

#
# Escaping filters
#

def escape_newlines(text):
    """
    Removes all newline characters from a block of text.
    """
    return mark_safe(text.replace('\r\n', "\\r\\n"))
escape_newlines.is_safe = True
escape_newlines = stringfilter(escape_newlines)
register.filter(escape_newlines)

_base_js_escapes = (
    ('\\', r'\u005C'),
    ('\'', r'\u0027'),
    ('"', r'\u0022'),
    ('>', r'\u003E'),
    ('<', r'\u003C'),
    ('&', r'\u0026'),
    ('=', r'\u003D'),
    ('-', r'\u002D'),
    (';', r'\u003B'),
    (u'\u2013', r'\u2013'),
    (u'\u2014', r'\u2014'),
    (u'\u2019', r'\u2019'),
    (u'\u201c', r'\u201c'),
    (u'\u201d', r'\u201d'),
    (u'\u2028', r'\u2028'),
    (u'\u2029', r'\u2029'),
    (u'\xbd', r'\xbd')
)

# Escape every ASCII character with a value less than 32.
_js_escapes = (_base_js_escapes +
               tuple([('%c' % z, '\\u%04X' % z) for z in range(32)]))

def escapejs(value):
    """
    Replaces Django's built-in escaping function with one that actually works.

    Take from "Changeset 12781":http://code.djangoproject.com/changeset/12781
    """
    for bad, good in _js_escapes:
        value = value.replace(bad, good)
    return value
escapejs = stringfilter(escapejs)
register.filter(escapejs)

#
# Truncation filters
#

def truncatesmart(value, limit=80):
    """
    Truncates a string after a given number of chars keeping whole words.
    
    Usage:
        {{ string|truncatesmart }}
        {{ string|truncatesmart:50 }}
    """
    
    try:
        limit = int(limit)
    # invalid literal for int()
    except ValueError:
        # Fail silently.
        return value
    
    # Make sure it's unicode
    value = unicode(value)
    
    # Return the string itself if length is smaller or equal to the limit
    if len(value) <= limit:
        return value
    
    # Cut the string
    value = value[:limit]
    
    # Break into words and remove the last
    words = value.split(' ')[:-1]
    
    # Join the words and return
    return ' '.join(words) + '...'

truncatesmart.is_safe = True
truncatesmart = stringfilter(truncatesmart)
register.filter(truncatesmart)

