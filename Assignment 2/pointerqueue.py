#!/usr/bin/env python

#NOTE: self is the first method argument for all methods where it is used as that is proper convention for python

class cell:
	def __init__(self): 
		self.element = None
		self.next = None

class pointerqueue:
	def __init__(self):
		self.front = cell()
		self.front.next = None
		self.rear = self.front

	#returns the first element of specified queue
	#if empty queue, None is returned and warning is printed
	def FRONT(self):
		if self.EMPTY():
			print "error retrieving front: queue is empty"
		else:
			return self.front.next.element

	#inserts element x at the end of the specified queue
	def ENQUEUE(self,x):
		self.rear.next = cell()
		self.rear = self.rear.next
		self.rear.element = x
		self.rear.next = None

	#deletes the first element of the specified queue
	def DEQUEUE(self):
		if self.EMPTY():
			print "error in dequeue: queue is empty"
		else:
			self.front = self.front.next

	#returns true if and only if specified queue is empty
	def EMPTY(self):
		if self.front == self.rear:
			return True
		else:
			return False

	#makes the specified queue an empty one
	def MAKENULL(self):
		self.front = cell()
		self.front.next = None
		self.rear = self.front
