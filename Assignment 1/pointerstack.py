#!/usr/bin/env python

#NOTE: self is the first method argument for all methods as it is proper convention for python
#For "undefined" results, None is returned or error message printed

class cell:
	def __init__(self):
		self.element = None
		self.next = None

class pointerstack:
	def __init__(self):
		self.head = None

	#returns the element at the top of the specified stack
	def top(self):
		if self.empty():
			print "Error retrieving top: stack is empty."
		else:
			return self.head.element

	#deletes the element at the top of the specified stack
	#does not return the element as per the book
	def pop(self):
		if self.empty():
			print "Error popping element: stack is empty."
		else:
			self.head = self.head.next

	#adds the specified element x to the top of the stack
	def push(self,x):
		if self.empty():
			new = cell()
			new.element = x
			self.head = new
		else:
			new = cell()
			new.element = self.head.element
			new.next = self.head.next
			self.head.element = x
			self.head.next = new

	#returns true if stack is empty, false otherwise
	def empty(self):
		if self.head is None:
			return True
		else:
			return False

	#makes the specified stack empty by moving the stack pointer to the top
	#skips manually deleting every element
	def makenull(self):
		self.head = None

