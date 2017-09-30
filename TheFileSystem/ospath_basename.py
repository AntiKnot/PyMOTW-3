#!/usr/bin/env python
# encoding: utf-8

# ospath_basename.py
import os.path
PATHS = [
    '/one/two/three',
    '/one/two/three/',
    '/one/two/three/four.txt',
    '/',
    '.',
    '',
]

for path in PATHS:
    print('{!r:>17}:{}'.format(path,os.path.basename(path)))
