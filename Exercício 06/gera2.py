#!/usr/bin/env python

import os, sys, random

N = int(sys.argv[1])

pai = range(N)

def find(x):
    if pai[x] != x:
        pai[x] = find(pai[x])
    return pai[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return False
    else:
        pai[x] = y
        return True

print (N)
print (N)

for i in range(N/2):
    print 'F %d %d' % (i + 1, i + 2)

for i in range(N - N/2):
    print 'C %d %d' % (1, i + 2)
