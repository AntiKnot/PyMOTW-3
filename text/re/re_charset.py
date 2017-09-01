#!/usr/bin/env python3
# encoding: utf-8

# re_charset.py

from re_test_patterns import test_patterns

test_patterns('abbaabbba', [
    ('[ab]', 'either a or b'),
    ('a[ab]+', 'a followed by 1 or more a or b'),
    ('a[ab]+?', 'a followed by 1 or more aor b, not greedy'),
])
