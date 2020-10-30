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
#simpleTranspositionCipher --m meetatthreepmtodayattheusuallocation --n 6
opts,args = getopt.getopt(args, "m,n", ['m=','n='])
u,n = opts[0][1],int(opts[1][1]) #find more efficient syn
len_org = len(u)
print(u)
print(n)
#%%encryption
splitted_u = list(u)
while len(splitted_u) < 2*n: #2n is chosen as the minimum 
    splitted_u.append(random.choice(string.ascii_letters).lower())


while len(splitted_u) %n !=0: 
    splitted_u.append(random.choice(string.ascii_letters).lower())
splitted_u = np.array(splitted_u) 
matrix = splitted_u.reshape(int(len(splitted_u)/n),n)

x=''
for i in range(0, np.size(matrix,1)):
    x += str(matrix[:,i]).translate(str.maketrans(' ', ' ', string.punctuation)).replace(" ", "")
    if (i != np.size(matrix,1) -1): x += " "

print("x:",x)
#%%decryption
splitted_x = x.split(" ")

for i in range(len(splitted_x)):
    splitted_x[i] = list(splitted_x[i])

x_m = np.array(splitted_x)
x_m = np.transpose(x_m)

#u_guess = str(x_m).translate(str.maketrans(' ', ' ', string.punctuation)).replace(" ", "").replace("\n"," ")
u_guess = str(x_m).translate(str.maketrans(' ', ' ', string.punctuation)).replace(" ", "")
print(u_guess)

