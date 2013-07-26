#!/usr/bin/python

def translate(string, chr_string=u'\u4e00\u4e8c\u4e09\u56db\u4e94\u516d\u4e03\u516b\u4e5d'):
  trans_string = ''
  for i in range(len(string)):
    trans_string += transChar(string[i], chr_string)
  return trans_string

def transChar(char, chr_string):
  if char in '123456789':
    return chr_string[int(char) - 1]
  else: return char
