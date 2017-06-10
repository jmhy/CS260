#!/usr/bin/env python

#it is recommended to pipe the output to a file for easier reading

from arraylist import *

n = 1000

#arraylist tests

print "arraylist.py tests"
print
print "iterated head insertion:"
test = arraylist()
for i in range(0,n):
	test.insert(i, 0)
print test.elements
print "iterated head deletion:"
for i in range(0,n):
	test.delete(0)
print test.elements[0:test.end()]

print "iterated tail insertion:"
test.makenull()
for i in range(0,n):
	test.insert(i,test.end())
print test.elements

print "first element index:"
print test.first()
print "last element index:"
print test.end()

test.makenull()
test.insert("a",0)
test.insert("b",1)
test.insert("b",2)
test.insert("c",3)
test.insert("d",4)
print "List: a, b, b, c, d"
print "list length, or last:"
print test.last
print "retrieve element at index 3, should be 'c'"
print test.retrieve(3)
print "locate first index of 'b', should be 1"
print test.locate("b")
print "next element after 'd':"
print test.next_cell(4)
print "previous of 'd' index:"
print test.previous(test.locate("d"))

