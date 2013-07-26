#!/usr/bin/python

import sys, codecs

first_arg = sys.argv[1]
print first_arg
print type(first_arg)

first_arg_unicode = first_arg.decode(sys.getfilesystemencoding())
print first_arg_unicode
print type(first_arg_unicode)

f = codecs.open(first_arg_unicode, 'r', 'utf-8')
unicode_text = f.read()
print type(unicode_text)
print unicode_text.encode(sys.getfilesystemencoding())