#!/usr/bin/env python

#NOTE: self is the first method argument for all methods as it is proper convention for python
#For "undefined" results, None is returned or error message printed

from array import *

class cell:
	def __init__(self): 
		self.element = None
		self.next = None

class pointerlist:
	def __init__(self):
		self.head = None
		self.pos = None

	#returns the first element in the list, None if list is empty
	def first(self):
		return self.head

	#returns the last element in the list, None if list is empty
	def end(self):
		if self.head is None and self.pos is None:
			return None
		else:
			c = self.head
			while c.next:
				c = c.next
			return c

	#returns the element of cell pointer p
	def retrieve(self,p):
		c = self.first()
		for i in range(0,p+1):
			if c.next is not None:
				c = c.next
		return c.element

	#returns pointer to cell holding element x in specified list, -1 if not found
	def locate(self,x):
		index = 0;
		c = self.first()
		while c:
			if c.element == x:
				return index
			index += 1
			c = c.next
		return -1

	#returns pointer to the next cell of the cell pointer p
	#None if not found
	#"next" is a reserved name in python, this is the next best thing
	def next_cell(self,c):
		return c.next

	#returns pointer to the previous cell of the cell pointer p
	#None if not found
	def previous(self,p):
		c = self.first()
		while c:
			if c.next == p:
				return c
			c = c.next
		return None

	#inserts element x into position of cell pointed by p
	def insert(self,x,p):
		if p is None:
			c = cell()
			c.element = x
			c.next = None
			self.head = c
			self.pos = self.head
		elif (p == self.first() and self.first() != self.end()) or p == 0:
			c = cell()
			c.element = x
			c.next = self.head
			self.head = c
			self.pos = self.head
		else:
			c = cell()
			c.element = x
			tmp = self.first()
			while tmp and p > 1:
				tmp = tmp.next
				p -= 1
			c.next = tmp.next
			tmp.next = c

	#deletes the element and cell holding it at cell pointed by p
	def delete(self,p):
		tmp = self.first()
		if p == 0:
			self.head = tmp.next
		elif p == self.end():
			if tmp.next == None:
				self.makenull()
			else:
				while tmp.next.next:
					tmp = tmp.next
				tmp.next = None
		else :
			while p - 1 > 0 :
				tmp = tmp.next
				p -= 1
			t1 = tmp
			t2 = tmp.next
			t1.next = t2.next
		self.pos = self.head

	#makes specified list empty
	def makenull(self):
		self.head = None
		self.pos = None

	def printlist(self):
		c = self.first()
		if c is None:
			print "Empty Pointer List"
		else:
			while c:
				print c.element
				c = c.next

