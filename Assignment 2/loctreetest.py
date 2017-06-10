#!/usr/bin/env python

from loctree import *

#loctree.py tests

print "Testing creation of empty tree with label 'a':"
test_list = []
tree = createi("a",test_list)
print "Finding parent:"
print tree.parent()
print "Finding children:"
for child in tree.children:
	print child
print "No children should be found"
print
print "Testing creation of tree with three nodes, where root is labeled 'a' and nodes 'b','c','d'"
tree1 = createi("b",test_list)
tree2 = createi("c",test_list)
tree3 = createi("d",test_list)
test_list.append(tree1)
test_list.append(tree2)
test_list.append(tree3)
tree = createi("a",test_list)
print "Root is now:", tree.root(), "Label:", tree.root().label()
for child in tree.children:
	label = child.label()
	parent = child.root()
	print child, "Label:", label, "Parent label:", parent
node = tree.leftmost_child()
print "Leftmost child of 'a' is:", node, "Label:", node.label()
node = node.right_sibling()
print "Right sibling of the leftmost child is:", node, "Label:", node.label()
node = node.right_sibling()
print "Right sibling of right sibling is:", node, "Label:", node.label()
print "Reached last child, but testing right sibling once more, should return null tree:"
node = node.right_sibling()
print "Right sibling of the leftmost child is:", node, "Label:", node.label()
print "Testing makenull on tree (nothing more should print):"
tree.makenull()
for child in tree.children:
	label = child.label()
	parent = child.root()
	print child, "Label:", label, "Parent label:", parent
