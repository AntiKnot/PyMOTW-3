#!/usr/bin/env python3PATH: /one/two/three/four
PATH: /one/two/threefold
PATH: /one/two/three/

PREFIX: /one/two

Press ENTER or type command to continue
# encoding: utf-8

# ospath_commonpath.py
import os.path
paths = [
    '/one/two/three/four',
    '/one/two/threefold',
    '/one/two/three/',
]

for path in paths:
    print('PATH:', path)

print()
print('PREFIX:', os.path.commonpath(paths))
