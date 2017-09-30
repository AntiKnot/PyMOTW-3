#!/usr/bin/env python
# encoding: utf-8

# ospath_commonprefix.py
import os.path
paths = [
    '/one/two/three/four',
    '/one/two/threefold',
    '/one/two/three/',
]
for path in paths:
    print('PATH:',path)

print()
print('PREFIX:',os.path.commonprefix(paths))
