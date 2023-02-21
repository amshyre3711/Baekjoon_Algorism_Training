#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#https://www.acmicpc.net/problem/10869

A, B = input().split()

def pr(A, B):
	A,B = int(A),int(B)
	print(A+B)
	print(A-B)
	print(A*B)
	print(int(A/B))
	print(A%B)

pr(A, B)

