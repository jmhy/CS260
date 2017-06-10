#!/usr/bin/env python

from pointerqueue import *

print "pointerqueue.py tests"
print
print "Testing queue initialization..."
test = pointerqueue()
print "Is queue empty?", test.EMPTY()
print "Inserting one element of value '1'..."
test.ENQUEUE(1)
print "Is queue still empty?", test.EMPTY()
print "The front is", test.FRONT()
print "Testing enqueue of '2' and '3' and dequeueing once..."
test.ENQUEUE(2)
test.ENQUEUE(3)
test.DEQUEUE()
print "The front is now", test.FRONT()
print "Is queue empty?", test.EMPTY()
print "Testing dequeue of last two elements..."
test.DEQUEUE()
test.DEQUEUE()
print "Is queue empty?", test.EMPTY()
print "Front is:", test.FRONT()
print "Testing dequeueing of empty queue..."
test.DEQUEUE()
print "Testing MAKENULL on queue with chars 'a' 'b' and 'c'..."
test.ENQUEUE('a')
test.ENQUEUE('b')
test.ENQUEUE('c')
print "Front should be 'a' before MAKENULL. It is:", test.FRONT()
test.MAKENULL()
print "After MAKENULL ..."
print test.FRONT()
print "Is queue empty?", test.EMPTY()
test.DEQUEUE()
