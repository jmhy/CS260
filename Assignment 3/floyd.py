#!/usr/bin/env python

#takes nxn matrix C of arc costs and produces nxn matrix A of shortest paths and P of point in the middle of each shortest path
def shortest(A,C,P):
	n = len(A)
	for i in range(n):
		for j in range(n):
			A[i][j] = C[i][j]
			P[i][j] = 0
	for i in range(n):
		A[i][i] = 0
	for k in range(n):
		for i in range(n):
			for j in range(n):
				if (A[i][k] + A[k][j]) < A[i][j]:
					A[i][j] = A[i][k] + A[k][j]
					P[i][j] = k
#prints shortest path between two nodes
def path(i,j,P):
	k = P[i][j]
	if k == 0:
		return
	path(i,k,P)
	print k
	path(k,j,P)

#begin test code

n = 6

C = [[0 for x in range(n)] for x in range(n)]
C[0][1] = 4
C[0][2] = 1
C[0][3] = 5
C[0][4] = 8
C[0][5] = 10
C[2][1] = 2
C[3][4] = 2
C[4][5] = 1

A = [[0 for x in range(n)] for x in range(n)]

P = [[0 for x in range(n)] for x in range(n)]

print "Initial Matrix C:"
for row in C:
	print row

shortest(A,C,P)

print "Matrix A:"
for row in A:
	print row
print "Matrix P:"
for row in P:
	print row

print
print "Shortest Paths:"
print "0->1"
path(0,1,P)
print
print "0->2"
path(0,2,P)
print
print "0->3"
path(0,3,P)
print
print "0->4"
path(0,4,P)
print
print "0->5"
path(0,5,P)
