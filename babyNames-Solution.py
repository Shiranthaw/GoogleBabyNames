#!/usr/local/bin/python

# This is a sample solution to Google Baby Names excecise
# https://developers.google.com/edu/python/exercises/baby-names
# Program output is as below:
#2006
#Aaliyah 91
#Aaron 57
#Abagail 895
#Abbey 695
#Abbie 650

import sys
import re

def extract_names(filename):
    print "Processing file: ", filename
    with open(filename,'r') as f:
        year = re.findall(r'Popularity in (\d{4})', f.read())

    with open(filename,'r') as f:
        names = re.findall(r'(\d*)</td><td>(\w*)</td><td>(\w*)', f.read())

    lst = []
    for t in names:
        lst.append(t[1]+ " " + t[0])
	lst.append(t[2]+ " " + t[0])

    lst.sort(key=lambda x: x[0])
    lst.insert(0,''.join(year))
    return lst
    #del lst[:]

def main():
    filelist = ['baby2002.html','baby2004.html','baby2006.html']

    for f in filelist:
        l = extract_names(f)
        text = '\n'.join(l) + '\n'
        #del l[:]
        print text

if __name__ == '__main__':
    main()
#text = '\n'.join(mylist) + '\n'



