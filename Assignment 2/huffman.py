#!/usr/bin/env python

import copy

#Declarations of ADTs for Huffman

#based on TREE record
class tree:
	def __init__(self,l,r,p):
		self.leftchild = l	#int
		self.rightchild = r	#int
		self.parent = p		#int
	def __str__(self):
		return str(self.leftchild)+"\t"+str(self.rightchild)+"\t"+str(self.parent)

#based on ALPHABET record
class alphabet:
	def __init__(self,s,p,l) :
		self.symbol = s		#char
		self.probability = p	#real
		self.leaf = l		#int, cursor into tree
	def __str__(self):
		return str(self.symbol)+"\t"+str(self.probability)+"\t"+str(self.leaf)

#based on FOREST record
class forest:
	def __init__(self,w,r):
		self.weight = w		#real
		self.root = r		#int, cursor into tree
	def __str__(self):
		return str(self.weight)+"\t"+str(self.root)

#Declarations of helper procedures

#based on lightones procedure
#least and second are type int, returns them as a tuple since can't pass by reference
def lightones(least,second):
	if FOREST[0].weight <= FOREST[1].weight:
		least = 0
		second = 1
	else:
		least = 1
		second = 0
	for i in range(2,len(FOREST)):
		if FOREST[i].weight < FOREST[least].weight:
			second = least
			least = i
		elif FOREST[i].weight < FOREST[second].weight:
			second = i
	return (least,second)

#based on create procedure
def create(lefttree, righttree):
	lastnode = len(TREE)
	TREE.append(tree(0, 0, 0))
	#cell for new node is TREE[lastnode]
	TREE[lastnode].leftchild = FOREST[lefttree].root
	TREE[lastnode].rightchild = FOREST[righttree].root
	#now enter parent pointers for new node and its children
	TREE[lastnode].parent = 0
	TREE[FOREST[lefttree].root].parent = lastnode
	TREE[FOREST[righttree].root].parent = lastnode
	return lastnode

def huffman():
	i = 0
	j = 0
	lasttree = len(FOREST)
	while lasttree > 1:
		i,j = lightones(i,j)
		newroot = create(i,j)
		#Now replace tree i by the tree whose root is newroot
		FOREST[i].weight = FOREST[i].weight + FOREST[j].weight
		FOREST[i].root = newroot
		#next, replace tree j, which is no longer needed by lasttree, and shrink FOREST by one
		FOREST[j] = FOREST[lasttree-1]
		del FOREST[lasttree-1]
		lasttree = lasttree - 1
	return

TREE = [tree(0,0,0), tree(0,0,0), tree(0,0,0), tree(0,0,0), tree(0,0,0), tree(0,0,0)]

ALPHABET = [alphabet('a',7,0), alphabet('b',9,1), alphabet('c',12,2), alphabet('d',22,3), alphabet('e',23,4), alphabet('f',27,5)]

FOREST = [forest(7,0), forest(9,1), forest(12,2), forest(22,3), forest(23,4), forest(27,5)]

print "Initial:"
print
print "TREE:"
for k in range(len(TREE)):
	print TREE[k]
print

print "ALPHABET:"
for k in range(len(ALPHABET)):
	print ALPHABET[k]
print

print "FOREST:"
for k in range(len(FOREST)):
	print FOREST[k]
print

huffman()

print "Final:"
print
print "TREE:"
for k in range(len(TREE)):
	print TREE[k]
print

print "ALPHABET:"
for k in range(len(ALPHABET)):
	print ALPHABET[k]
print

print "FOREST:"
for k in range(len(FOREST)):
	print FOREST[k]

