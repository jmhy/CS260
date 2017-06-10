#!/usr/bin/env python

from arraylist import *

#Exercise 2.4, uses arraylist implementation

#concatenates an arraylist of arraylists and returns it as another arraylist
def concat(lists):
	res = arraylist()
	i = 0
	while i < lists.end():
		l = lists.retrieve(i)
		for j in range(0,l.end()):
			element = l.retrieve(j)
			res.insert(element,res.end())
		i += 1
	return res

print "Testing concatenation of arraylists:"
print "Should print 0 2 6 8 1 5 3 9 4 10 7"
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
tests = concat(tests)
for i in range(0,tests.end()):
	print tests.retrieve(i),
