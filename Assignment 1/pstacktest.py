#!/usr/bin/env python

from pointerstack import *

#pointerstack.py tests

n = 10

print "Creating new stack, is it empty?"
stk = pointerstack()
print stk.empty()

print "Iterated insert of 10 elements into stack"
for i in range(0,n):
	stk.push(i)

print "Attempting to print top of stack, which should be 9..."
print stk.top()
print "Attempting to pop 3 elements, top should then be 6..."
stk.pop()
stk.pop()
stk.pop()
print stk.top()
print "Is stack empty now?"
print stk.empty()
print "Popping last 7 elements. Empty now?"
stk.pop()
stk.pop()
stk.pop()
stk.pop()
stk.pop()
stk.pop()
stk.pop()
print stk.empty()
print "What's the top element though?"
print stk.top()
print "Pushing a few elements, then making stack empty through makenull.."
stk.push(1)
stk.push(2)
stk.push(3)
stk.makenull()
stk.pop()
