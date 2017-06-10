#!/usr/bin/env python

#NOTE: self is the first method argument for all methods as it is proper convention for python
#For "undefined" results, None is returned or error message printed

from array import *

class arraylist:
	def __init__(self):
		self.maxlength = 1000
		self.elements = [None]*self.maxlength
		self.last = 0 #is 1 in the book, but python starts indices from 0

	#accepts a list, returns position of first element as int 0, regardless of list being empty
	#no need to return end() of list, since first position of empty array is always 0
	def first(self):
		return 0

	#accepts a list, returns position of last element of list
	def end(self):
		return self.last

	#returns the element of specified list at integer position p
	def retrieve(self,p):
		if p > self.last:
			return None
		else :
			return self.elements[p]

	#returns integer position of element x in specified list
	def locate(self,x):
		for i in range(0,self.last):
			if self.elements[i] == x:
				return i

	#returns the position (integer) that follows specified position p (integer) in list
	#None if not found
	#"next" is a reserved name in python, this is the next best thing
	def next_cell(self,p):
		if p + 1 >= self.last:
			return None
		else:
			return p + 1

	#returns the position (integer) that precedes specified position p (integer) in list
	#None if not found
	def previous(self,p):
		if p > self.last or p == 0:
			return None
		else:
			return p - 1

	#inserts element x at position p (integer) in the specified list
	def insert(self,x,p):
		if p > self.last:
			print "Cannot insert at position", p, "list at max size"
		elif p == self.last:
			self.elements[p] = x
			self.last = self.last + 1
		else:
			self.elements[p+1:self.last+1] = self.elements[p:self.last]
			self.elements[p] = x
			self.last = self.last + 1

	#delete the element at position p (integer) from the list
	def delete(self,p):
		if p <= self.last and p >= 0:
			for i in range(p,self.last):
				self.elements[i-1] = self.elements[i]
			self.last = self.last - 1
		else:
			print "Cannot delete at index", p, ", index out of range"

	#makes specified list empty
	def makenull(self):
		self.elements = [None]*self.maxlength
		self.last = 0

