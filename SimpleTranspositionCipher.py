#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 13:57:08 2020

@author: Ayca
"""

import random
import string
import numpy as np
#%% get arguments via terminal
import getopt

args = str(input())
args = args.split()
args = args[1:]


#Usage: simpleTranspositionCipher --m msg --n noOfCols
opts,args = getopt.getopt(args, "m,n", ['m=','n='])
u,n = opts[0][1],int(opts[1][1]) #find more efficient syn
len_org = len(u)
print(u)
print(n)
#%%
splitted_u = list(u)
while len(splitted_u) < 2*n: #2n is chosen as the minimum
    splitted_u.append(random.choice(string.ascii_letters).lower())


while len(splitted_u) %n !=0: 
    splitted_u.append(random.choice(string.ascii_letters).lower())
splitted_u = np.array(splitted_u) 
matrix = splitted_u.reshape(n,int(len(splitted_u)/n))

x=''
for i in range(0, np.size(matrix,1)):
    x += str(matrix[:,i]).translate(str.maketrans(' ', ' ', string.punctuation)).replace(" ", "")
    x += " "

print("x:",x)
