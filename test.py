#!/usr/bin/python3
"""
This is a test file
"""

str = "create State name=California collage=none"
str_split = str.split(' ')
print(str_split)
str_split.reverse()
cs = str_split.pop()
print(cs, str_split)

new = {'name': "nae", 'yo': 'loo'}
new.update({'lo': 'ko'})
print(new.__contains__("loo"))
