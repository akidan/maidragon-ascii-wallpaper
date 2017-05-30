#!/usr/bin/env python
# coding=utf-8
import sys
import codecs

input="kanna.txt"
output="kanna_out.txt"
amount=3
spacing=20
maxtrim=100

amount=int(sys.argv[1]) if len(sys.argv)>1 and sys.argv[1].isdigit() else amount
spacing=int(sys.argv[2]) if len(sys.argv)>2 and sys.argv[2].isdigit() else spacing

with codecs.open(input,'r','utf-8') as f1:
    #print(f1.read().encode('utf-8'))
    readline=f1.readlines()
with codecs.open(output,'w','utf-8') as f2:
    f2.write("")
for i in readline:
    maxtrim = len(i)-len(i.lstrip()) if len(i)-len(i.lstrip()) > maxtrim else maxtrim
line=0
hair=56
for i in readline:
    with codecs.open(output,'a','utf-8') as f2:
        i=i[0:(len(i)-1)]+maxtrim * ' ' + i[len(i)-1:]
        trimlen = len(i) - len(i.lstrip())
        if line<hair:
            f2.write(trimlen*' '+i[trimlen:(trimlen+int(spacing))]*amount+i[trimlen:].rstrip()+i[len(i)-1:])
        else:
            headno=1
            content=i[0:(len(i)-1)]+amount*len(i)*' ' + i[len(i)-1:]
            i=i.lstrip()
            while headno <= amount:
                pointer=0
                while pointer < len(i)-1:
                    if content[trimlen+headno*spacing+pointer] == ' ' and i[pointer] != ' ':
                        content=content[0:trimlen+headno*spacing+pointer-1]+i[pointer]+content[trimlen+headno*spacing+pointer:]
                    pointer+=1
                headno+=1
            f2.write(content.rstrip()+i[len(i)-1:])
        line+=1;
