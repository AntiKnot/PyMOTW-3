#!/usr/bin/env python
# encoding: utf-8

# re_groups_individual.py
import re
text = "This is some text -- with punctuation."

print('Input text               :', text)

# word staring with 't' then another word
regex = re.compile(r'(\bt\w+)\W+(\w+)')
print('Pattern                  :', regex.pattern)
match = regex.search(text)
print('Entire match             :', match.group(0))
print('Word starring with "t"   :', match.group(1))
print('Word after "t"           :', match.group(2))
