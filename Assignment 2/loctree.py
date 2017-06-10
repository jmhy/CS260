#!/usr/bin/env python

class node:
	def __init__(self):
		self.l = None
		self.children = []
		self.par = None #should be None if root

	#returns the parent of the node
	def parent(self):
		return self.par

	#returns the leftmost child of the node
	def leftmost_child(self):
		return self.children[0]

	#returns the right sibling of the node, null tree if last sib
	def right_sibling(self):
		try:
			return self.par.children[(self.par.children.index(self))+1]
		except IndexError:
			return node() # null tree

	#returns the label of the node
	def label(self):
		return self.l

	#returns the root of the tree that this node is in, or None if null tree
	def root(self):
		root = self
		while root.par != None:
			root = self.par
		return root

	#makes the specified tree null
	def makenull(self):
		self.l = None
		self.children = []
		self.par = None #should be None if root

#makes a new node with label v and gives it i children
#which are the roots of trees specified in list Ti
#limited to i=0,1,2,3 as per directions
def createi(v, Ti):
	if len(Ti) >= 4:
		raise("loctree.creati: specify no more than 3 children in 2nd arg")
	else:
		tree = node()
		tree.l = v
		for childtree in Ti:
			tree.children.append(childtree)
			childtree.par = tree
		return tree
