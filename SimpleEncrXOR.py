#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 19:28:56 2020

@author: Ayca
"""
import random
#%% get arguments via terminal
import getopt

args = str(input())
args = args.split()
args = args[1:]

#Usage: simpleEncrXOR --m msg
opts,args = getopt.getopt(args, "m", ['m='])
u = opts[0][1]
len_org = len(u)
print(u)
#%%methods
def str2binary(u):
    res = ''.join(format(ord(i), 'b') for i in u)
    return res

def randKey(u):
    u2 = str2binary(u)
    k = ""
    for i in range(len(u2)):
        k+= str(random.randint(0, 1))
    return u2,k

def XOR(u,k):
    res = ""
    for i in range(len(u)):
        if u[i]==k[i]:
            res+="0"
        else:
            res+="1"
    return res
#%%encryption
u,KEY = randKey(u)
x = XOR(u,KEY)
print(KEY)
print("msg in binary: {}\nKEY: {}\nx: {}".format(u,KEY,x))
    
#%%decryption
u_dec = XOR(x,KEY)
print(u_dec)
if(u_dec ==u):
    print("OK")
#%% original message

chunks, chunk_size = len(u), int(len(u)/len_org)
org_m = [ u[i:i+chunk_size] for i in range(0, chunks, chunk_size) ]
org_m = [int(org_m[i],2) for i in range(len(org_m))]
org_m = ''.join(chr(i) for i in org_m)    
print("Orginal message was:", org_m)


