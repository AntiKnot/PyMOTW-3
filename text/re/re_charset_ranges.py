#!/usr/bin/env python3
# encoding: utf-8

# re_charset_ranges.py

from re_test_patterns import test_patterns

test_patterns(
    'This is some text -- with punctuation.',
    [('[a-z]+',
      'sequences of lowercase letters'), ('[A-Z]+',
                                          'sequences of unpercase letters'),
     ('[a-zA-z]+', 'sequences of letters of either case'),
     ('[A-Z][a-z]+', 'one uppercase followed by lowercase')], )
