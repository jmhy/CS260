#!/usr/bin/env python

#NOTE: I could not get this to read from stdin and use the make utility at the same time

import sys

def prefix(expr):
	token = expr.pop(0)
	if token == '+':
		return prefix(expr) + prefix(expr)
	elif token == '-':
		return prefix(expr) - prefix(expr)
	elif token == '*':
		return prefix(expr) * prefix(expr)
	elif token == '/':
		return prefix(expr) / prefix(expr)
	else:
		return int(token)

#begin tests
print "Testing prefix: - * / 15 - 7 + 1 1 3 + 2 + 1 1"
print "Result should be '5'"
test = ['-','*','/',"15",'-','7','+','1','1','3','+','2','+','1','1']
print prefix(test)
