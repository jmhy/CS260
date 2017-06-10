#!/usr/bin/env python

#NOTE: self is the first method argument for all methods as it is proper convention for python
#For "undefined" results, None is returned or error message printed

from array import *

class arraystack:
	def __init__(self):
		self.maxlength = 1000
		self.itop = self.maxlength # maxlength-1 will first element of stack
		self.elements = [None]*self.maxlength

	#returns the element at the top of the specified stack
	def top(self):
		if self.empty():
			print "Error retrieving top: stack is empty."
		else:
			return self.elements[self.itop]

	#deletes the element at the top of the specified stack
	#does not return the element as per the book
	def pop(self):
		if self.empty():
			print "Error popping element: stack is empty."
		else:
			self.itop = self.itop + 1

	#adds the specified element x to the top of the stack
	def push(self,x):
		if self.itop == 0:
			print "Error pushing element: stack is full."
		else:
			self.itop = self.itop - 1
			self.elements[self.itop] = x

	#returns true if stack is empty, false otherwise
	def empty(self):
		if(self.itop >= self.maxlength):
			return True
		else:
			return False

	#makes the specified stack empty by moving the stack pointer to the top
	#skips manually deleting every element
	def makenull(self):
		self.itop = self.maxlength
		return

