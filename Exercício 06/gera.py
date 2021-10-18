#!/usr/bin/env python

import os, sys, random

N = int(sys.argv[1])
M = int(sys.argv[2])

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

print N, M

for i in range(M):
    a = random.randint(1, N)
    b = random.randint(1, N)
    if random.randint(1, 100) <= 80 and union(a-1, b-1):
        print 'F %d %d' % (a, b)
    else:
        print 'C %d %d' % (a, b)
