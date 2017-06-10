#!/usr/bin/env python

#it is recommended to pipe the output to a file for easier reading

from pointerlist import *

#pointerlist tests

print "pointerlist.py tests"
print
print "head insertion:"
test = pointerlist()
test.insert(1,0)
test.insert(2,0)
test.insert(3,0)
test.insert(4,0)
test.insert(5,0)
print "The following list should be 5 4 3 2 1:"
test.printlist()

print "After delete, should be 4 3 2"
test.delete(0)
test.delete(test.end())
test.printlist()
print
print "Pointer to first cell and its element, 4:"
print test.first(), "element:", test.first().element
print
print "Cell with 4 points to next:"
c = test.first()
print test.next_cell(c), "element: ", test.next_cell(c).element
print
print "Pointer to last cell and its element, 2:"
print test.end(), "element:", test.end().element
print
print "2's previous is:"
c = test.end()
print test.previous(c), "element: ", test.previous(c).element
print "3 is located at index", test.locate(3)
print "At index 2, the element is", test.retrieve(2)

print "Attempting to clear list and print it..."
test.makenull()
test.printlist()
