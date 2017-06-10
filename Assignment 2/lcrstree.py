#!/usr/bin/env python

class node:
	def __init__(self):
		self.l = None
		self.lc = None
		self.rs = None
		self.par = None

	#returns the parent of the node
	def parent(self):
		return self.par

	#returns the leftmost child of the node
	def leftmost_child(self):
		return self.lc

	#returns the right sibling of the node, null tree if last sib
	def right_sibling(self):
		if self.rs is None:
			return node() # null tree
		else:
			return self.rs

	#returns the label of the node
	def label(self):
		return self.l

	#returns the root of the tree that this node is in, or None if null tree
	def root(self):
		root = self
		while root.par != None:
			root = root.par
		return root

	#makes the specified tree null
	def makenull(self):
		self.l = None
		self.lc = None
		self.rs = None
		self.par = None

#creates a lcrs tree from two specified child nodes and a given label
#if T1 and T2 are None, then creates a tree with specified label but no children
def create2(v, T1, T2):
	if T1 is None and T2 is None:
		tree = node()
		tree.l = v
	elif T1 is not None and T2 is not None:
		tree = node()
		tree.l = v;
		tree.lc = T1
		tree.lc.par = tree
		tree.lc.rs = T2
		tree.lc.rs.par = tree
	else:
		raise("T1 and T2 args must both be either None or a lcrstree")
	return tree


