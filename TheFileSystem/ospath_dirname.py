#!/usr/bin/env python
# encoding: utf-8

# ospath_dirname.py
import os.path
PATHS = [
    '/one/two/three',
    '/one/two/three/',
    '/',
    '',
]
for path in PATHS:
    print('{!r:>17}:{}'.format(path, os.path.dirname(path)))
