#!/usr/bin/python3

from googlesearch import search
import sys
query = 'tutorialpoint'

for j in search(query,tld='co.in', num=5,stop=5, pause=1): 
    print(j) 

