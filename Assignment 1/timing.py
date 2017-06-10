#!/usr/bin/env python

from arraylist import *
from pointerlist import *
from arraystack import *
from pointerstack import *
from timeit import Timer

# list head insertions
def lib_head():
	lst = [0]*n
	for i in range(0, n):
		lst.insert(0, 1)

def array_head():
	lst = arraylist()
	for i in range(0, n):
		lst.insert(1, 0)

def p_head():
	lst = pointerlist()
	for i in range(0,n):
		lst.insert(1,0)

# list tail insertions
def lib_tail():
	lst = [0]*n
	for i in range(0, n):
		lst.append(1)

def array_tail():
	lst = arraylist()
	for i in range(0,n):
		lst.insert(1,lst.end())

def p_tail():
	lst = pointerlist()
	for i in range(0,n):
		lst.insert(1,lst.end())
	
# list traversals
def lib_traversal():
	lst = [0]*n
	for i in range(len(lst)):
		x = lst[i]

def array_traversal():
	lst = arraylist()
	for i in range(0,n):
		lst.insert(1, lst.end())
	p = lst.first()
	while p:
		p = lst.next(p)

def p_traversal():
	lst = pointerlist()
	for i in range(0,n):
		lst.insert(1,lst.end())
	c = lst.first()
	while c:
		c = lst.next_cell(c)

# head deletion
def lib_del_head():
	lst = [0]*n
	for i in range(0, n):
		del lst[0]

def array_del_head():
	lst = arraylist()
	for i in range(0,n):
		lst.insert(1,lst.end())
	for i in range(0,n):
		lst.delete(0)

def p_del_head():
	lst = pointerlist()
	for i in range(0,n):
		lst.insert(1,lst.first())
	for i in range(0,n):
		lst.delete(0)

# tail deletion
def lib_del_tail():
	lst = [0]*n
	for i in range(0, n):
		del lst[-1]

def array_del_tail():
	lst = arraylist()
	for i in range(0,n):
		lst.insert(1,lst.end())
	for i in range(0,n):
		lst.delete(lst.end())

def p_del_tail():
	lst = pointerlist()
	for i in range(0,n):
		lst.insert(1,lst.end())
	for i in range(0,n):
		lst.delete(lst.end())

#iterated stack insertions
def lib_stack_insert():
	stk = []
	for i in range(0,n):
		stk.append(1)

def a_stack_insert():
	stk = arraystack()
	for i in range(0,n):
		stk.push(1)

def p_stack_insert():
	stk = pointerstack()
	for i in range(0,n):
		stk.push(1)

#iterated stack deletions
def lib_stack_del():
	stk = []
	for i in range(0,n):
		stk.append(1)
	for i in range(0,n):
		stk.pop()

def a_stack_del():
	stk = arraystack()
	for i in range(0,n):
		stk.push(1)
	for i in range(0,n):
		stk.pop()

def p_stack_del():
	stk = pointerstack()
	for i in range(0,n):
		stk.push(1)
	for i in range(0,n):
		stk.pop()

# control time for creating test data
def lib_assign():
	lst = [0]*n

def array_assign():
	lst = arraylist()

def p_assign():
	lst = pointerlist()

def lib_stk_assign():
	stk = []

def a_stk_assign():
	stk = arraystack()

def p_stk_assign():
	stk = pointerstack()

#begin tests
trials = 100
n = 1000

print "n = ", n

t = Timer("lib_assign()", "from __main__ import lib_assign")
lib_assign_t = t.timeit(trials)/(trials*n)

t = Timer("array_assign()", "from __main__ import array_assign")
array_assign_t = t.timeit(trials)/(trials*n)

t = Timer("p_assign()", "from __main__ import p_assign")
p_assign_t = t.timeit(trials)/(trials*n)

t = Timer("lib_stk_assign()", "from __main__ import lib_stk_assign")
lib_stk_assign_t = t.timeit(trials)/(trials*n)

t = Timer("a_stk_assign()", "from __main__ import a_stk_assign")
a_stk_assign_t = t.timeit(trials)/(trials*n)

t = Timer("p_stk_assign()", "from __main__ import p_stk_assign")
p_stk_assign_t = t.timeit(trials)/(trials*n)


t = Timer("lib_head()", "from __main__ import lib_head")
lib_head_time = t.timeit(trials)/(trials*n)
print "lib list head insertion time: \t", lib_head_time-lib_assign_t

t = Timer("array_head()", "from __main__ import array_head")
array_head_time = t.timeit(trials)/(trials*n)
print "array list head insertion time: \t", array_head_time-array_assign_t

t = Timer("p_head()", "from __main__ import p_head")
p_head_time = t.timeit(trials)/(trials*n)
print "pointer list head insertion time: \t", p_head_time-p_assign_t


t = Timer("lib_tail()", "from __main__ import lib_tail")
lib_tail_time = t.timeit(trials)/(trials*n)
print "lib list tail insertion time: \t", lib_tail_time-lib_assign_t

t = Timer("array_tail()", "from __main__ import array_tail")
array_tail_time = t.timeit(trials)/(trials*n)
print "array list tail insertion time: \t", array_tail_time-array_assign_t

t = Timer("p_tail()", "from __main__ import p_tail")
p_tail_time = t.timeit(trials)/(trials*n)
print "pointer list tail insertion time: \t", p_tail_time-p_assign_t


t = Timer("lib_traversal()", "from __main__ import lib_traversal")
lib_traversal_time = t.timeit(trials)/(trials*n)
print "lib list traversal time: \t\t", lib_traversal_time-lib_assign_t

t = Timer("array_traversal()", "from __main__ import array_traversal")
array_traversal_time = t.timeit(trials)/(trials*n)
print "array list traversal time: \t\t", array_traversal_time-array_assign_t

t = Timer("p_traversal()", "from __main__ import p_traversal")
p_traversal_time = t.timeit(trials)/(trials*n)
print "pointer list traversal time: \t\t", p_traversal_time-p_assign_t


t = Timer("lib_del_head()", "from __main__ import lib_del_head")
lib_del_head_time = t.timeit(trials)/(trials*n)
print "lib list head deletion time: \t", lib_del_head_time-lib_assign_t

t = Timer("array_del_head()", "from __main__ import array_del_head")
array_del_head_time = t.timeit(trials)/(trials*n)
print "array list head deletion time: \t", array_del_head_time-array_assign_t

t = Timer("p_del_head()", "from __main__ import p_del_head")
p_del_head_time = t.timeit(trials)/(trials*n)
print "pointer list head deletion time: \t", p_del_head_time-p_assign_t


t = Timer("lib_del_tail()", "from __main__ import lib_del_tail")
lib_del_tail_time = t.timeit(trials)/(trials*n)
print "lib list tail deletion time: \t", lib_del_tail_time-lib_assign_t

t = Timer("array_del_tail()", "from __main__ import array_del_tail")
array_del_tail_time = t.timeit(trials)/(trials*n)
print "array list tail deletion time: \t", array_del_tail_time-array_assign_t

t = Timer("p_del_tail()", "from __main__ import p_del_tail")
p_del_tail_time = t.timeit(trials)/(trials*n)
print "pointer list tail deletion time: \t", p_del_tail_time-p_assign_t


t = Timer("lib_stack_insert()", "from __main__ import lib_stack_insert")
lib_stack_insert_time = t.timeit(trials)/(trials*n)
print "lib stack push time: \t", lib_stack_insert_time-lib_stk_assign_t

t = Timer("a_stack_insert()", "from __main__ import a_stack_insert")
a_stack_insert_time = t.timeit(trials)/(trials*n)
print "array stack push time: \t", a_stack_insert_time-a_stk_assign_t

t = Timer("p_stack_insert()", "from __main__ import p_stack_insert")
p_stack_insert_time = t.timeit(trials)/(trials*n)
print "pointer stack push time: \t", p_stack_insert_time-p_stk_assign_t


t = Timer("lib_stack_del()", "from __main__ import lib_stack_del")
lib_stack_del_time = t.timeit(trials)/(trials*n)
print "lib stack push time: \t", lib_stack_del_time-lib_stk_assign_t

t = Timer("a_stack_del()", "from __main__ import a_stack_del")
a_stack_del_time = t.timeit(trials)/(trials*n)
print "array stack push time: \t", a_stack_del_time-a_stk_assign_t

t = Timer("p_stack_del()", "from __main__ import p_stack_del")
p_stack_del_time = t.timeit(trials)/(trials*n)
print "pointer stack push time: \t", p_stack_del_time-p_stk_assign_t

