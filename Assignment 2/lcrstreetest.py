#!/usr/bin/env python

from lcrstree import *
from copy import *

#lcrstree.py tests

print "Creating tree with root 'a' and children 'b' and 'c'"
tree = create2('a',create2('b',None,None),create2('c',None,None))
print "Testing label"
print tree.label()
print "Testing parent"
print tree.leftmost_child().parent(), "Label:", tree.leftmost_child().parent().label()
print "Testing leftmost_child"
print tree.leftmost_child(), "Label:", tree.leftmost_child().label()
print "Testing right_sibling"
print tree.leftmost_child().right_sibling(), "Label:", tree.leftmost_child().right_sibling().label()
print "Putting original tree twice into another one and finding root which should be 'root'"
tree2 = deepcopy(tree)
tree = create2("root",tree,tree2)
print "From first leftmost child:"
print tree.leftmost_child().root(), tree.leftmost_child().root().label()
print "From second leftmost child:"
print tree.leftmost_child().leftmost_child().root(), tree.leftmost_child().leftmost_child().root().label()
