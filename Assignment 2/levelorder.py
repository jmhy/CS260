#!/usr/bin/env python

from loctree import *
import Queue

#Exercise 3.10

#prints to console the level order representation of the specified tree
def levelorder(tree):
	current = [tree.root()]
	while current:
		next = []
		for n in current:
			print n.label(),
			for child in n.children:
				next.append(child)
		print
		current = next

#begin test code
#constructing a tree of level 2, with each node having two children
'''
This is acii representation of tree to be made

       a
   /   |   \
  b    c    d
 / \  / \   /\
e   f g  h i  j

'''
print "Testing levelorder:"
test_list = []
tree1 = createi("e",test_list)
tree2 = createi("f",test_list)
tree3 = createi("g",test_list)
tree4 = createi("h",test_list)
tree5 = createi("i",test_list)
tree6 = createi("j",test_list)

tree1 = createi("b",[tree1,tree2])
tree2 = createi("c",[tree3,tree4])
tree3 = createi("d",[tree5,tree6])
test_list.append(tree1)
test_list.append(tree2)
test_list.append(tree3)

tree = createi("a",test_list)

levelorder(tree)
