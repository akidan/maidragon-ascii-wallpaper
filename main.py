#!/usr/bin/env python
# coding=utf-8
import sys
import codecs

input="kanna.txt"
output="kanna_out.txt"
amount=3
spacing=56
maxtrim=100

amount=sys.argv[1] if len(sys.argv)>1 and sys.argv[1].isdigit() else amount
spacing=sys.argv[2] if len(sys.argv)>2 and sys.argv[2].isdigit() else spacing

with codecs.open(input,'r','utf-8') as f1:
    #print(f1.read().encode('utf-8'))
    readline=f1.readlines()
with codecs.open(output,'w','utf-8') as f2:
    f2.write("")
for i in readline:
    maxtrim = len(i)-len(i.lstrip()) if len(i)-len(i.lstrip()) > maxtrim else maxtrim
for i in readline:
  with codecs.open(output,'a','utf-8') as f2:
    i=i[0:(len(i)-1)]+maxtrim * ' ' + i[len(i)-1]
    trimlen = len(i) - len(i.lstrip())
    f2.write(trimlen*' '+i[trimlen:(trimlen+int(spacing))]*int(amount)+i[trimlen:].rstrip()+i[len(i)-1])
## todo: after LINE57, fix the hair
