#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 19:28:56 2020

@author: Ayca
"""
import random
def str2binary(u):
    res = ''.join(format(ord(i), 'b') for i in u)
    return res, len(res)

def randKey(u):
    u2,len_u2 = str2binary(u)
    k = ""
    for i in range(len_u2):
        k+= str(random.randint(0, 1))
    return u2,k
def XOR(u):
    u2,k = randKey(u)
    res = ""
    for i in range(len(u2)):
        if u2[i]==k[i]:
            res+="0"
        else:
            res+="1"
    return u2,k,res


    


