#!/usr/bin/env python
# coding=utf-8
import sys
import codecs

color_prefix="\x1b[3"
color_suffix="m"
color_hash=[1,5,3,2,6,4]

input="kanna.txt"
output="kanna_color_out.txt"
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
            printline = trimlen*' '
            for j in range(0,amount):
                printline =  printline + color_prefix + str(color_hash[j%len(color_hash)]) + color_suffix + i[trimlen:(trimlen+int(spacing))]
            f2.write(printline+color_prefix + str(color_hash[amount%len(color_hash)]) + color_suffix+i[trimlen:].rstrip()+i[len(i)-1:-1]+'\x1b[0m\n')
        else:
            headno=1
            content=i[0:(len(i)-1)]+amount*len(i)*' ' + i[len(i)-1:]
            i=i.lstrip()
            color_matrix = [0] * (len(content) * headno)
            while headno <= amount:
                # create a matrix for color mapping
                print(content)
                for j in range(0,len(content)):
                    if content[j] != ' ' or (content[j] == ' ' and color_matrix[j]>0):
                        color_matrix[j] = color_matrix[j]+1

                pointer=0
                while pointer < len(i)-1:
                    if content[trimlen+headno*spacing+pointer] == ' ' and i[pointer] != ' ':
                        content=content[0:trimlen+headno*spacing+pointer-1]+i[pointer]+content[trimlen+headno*spacing+pointer:]
                    pointer+=1
                headno+=1
            #print(color_matrix[:200])
            content = content.rstrip()+i[len(i)-1:-1]
            newContent = ''
            for j in range(0,len(content)):
                if (content[j] == ' '):
                    newContent = newContent + content[j]
                else:
                    newContent = newContent + color_prefix + str(color_hash[(amount - color_matrix[j])%len(color_hash)]) + color_suffix + content[j]
            f2.write(newContent+'\x1b[0m\n')
        line+=1;