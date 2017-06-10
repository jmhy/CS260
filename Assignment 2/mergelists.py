#!/usr/bin/env python

from arraylist import *

#Exercise 2.3, uses arraylist implementation

#sorts the elements of the specified arraylist
def insertionsort(L):
	for i in range(0, L.end()):
		j = i
		while j > 0 and L.retrieve(j) < L.retrieve(j-1):
			L.elements[j], L.elements[j-1] = L.elements[j-1], L.elements[j]
			j -= 1

def mergetwolists(L1,L2):
	merged = L1
	for i in range(0,L2.end()):
		element = L2.retrieve(i)
		merged.insert(element,merged.end())
	insertionsort(merged)
	return merged

#takes an arraylist of arraylists, merges and sorts them, then returns the result
def mergenlists(lists):
	merged = arraylist()
	i = 0
	while i < lists.end():
		l = lists.retrieve(i)
		for j in range(0,l.end()):
			element = l.retrieve(j)
			merged.insert(element,merged.end())
		i += 1
	insertionsort(merged)
	return merged

#begin test code
print "Testing merge of two sorted lists, both are [a,b,c,d,e]:"
print "Result should print a a b b c c d d e e"
test1 = arraylist()
test1.insert("a",0)
test1.insert("b",1)
test1.insert("c",2)
test1.insert("d",3)
test1.insert("e",4)
test1 = mergetwolists(test1,test1)
for i in range(0,test1.end()):
	print test1.retrieve(i),
print
print "Testing merge of n sorted lists with numbers as elements:"
print "Result should print numbers 0 thru 10 in order"
test1 = arraylist()
test1.insert(0,0)
test1.insert(2,1)
test1.insert(6,2)
test1.insert(8,3)
test2 = arraylist()
test2.insert(1,0)
test2.insert(5,1)
test2.insert(3,2)
test2.insert(9,3)
test3 = arraylist()
test3.insert(4,0)
test3.insert(10,1)
test3.insert(7,2)
tests = arraylist()
tests.insert(test1,0)
tests.insert(test2,1)
tests.insert(test3,2)
tests = mergenlists(tests)
for i in range(0,tests.end()):
	print tests.retrieve(i),

