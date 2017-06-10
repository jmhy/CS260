#!/usr/bin/env python

#datatype to represent basic element of linked list
class cell:
	def __init__(self):
		self.element = None
		self.next = None

	def __str__(self):
		return str(self.element)

#calls library hash function and returns it (mod buckets)
def h(x):
	return hash(x) % B

#returns empty dictionary
def MAKENULL():
	d = []
	for i in range(B):
		d.append(None)
	return d

#returns true if item x is in dictionary A, false otherwise
def MEMBER(x,A):
	global countIns
	iprobes = 1
	c = A[h(x)]
	while c is not None:
		if c.element == x:
			countIns.append(iprobes)
			return True
		else:
			c = c.next
			iprobes += 1
	countIns.append(iprobes)
	return False

#inserts item x into dictionary A, if not already a member of A
def INSERT(x,A):
	if not MEMBER(x, A):
		bucket = h(x)
		oldheader = A[bucket]
		n = cell()
		n.element = x
		n.next = oldheader
		A[bucket] = n

#deletes item x from dictionary A, if present
def DELETE(x,A):
	global countDel
	iprobes = 1
	bucket = h(x)
	if A[bucket] is not None:
		if A[bucket].element == x:
			A[bucket] = A[bucket].next
			countDel.append(iprobes)
		else:
			c = A[bucket]
			while c.next is not None:
				if c.next.element == x:
					c.next = c.next.next
					countDel.append(iprobes)
				else:
					c = c.next
					iprobes += 1
			countDel.append(iprobes)

#prints a representation of specified dictionary A for debug purposes
def PRINT_DICT(A):
	for i in range(len(A)):
		if A[i] is not None:
			c = A[i]
			print "[",
			while c is not None:
				print c,
				c = c.next
			print "]"

#begin test code

global countIns
global countDel
countIns = []
countDel = []
testwords = ["the","quick","brown","fox","jumped","over","the","lazy","dog"]
bkts = []
probesIns = []
probesDel = []
avgIns = []
avgDel = []

for B in range(1, 1010, 10):
	if B != 1:
		B = B - 1
	myDict = MAKENULL()
	
	countIns = []
	for w in testwords:
		INSERT(w,myDict)

	totalI = 0
	for i in countIns:
		totalI += i

	countDel = []
	for w in testwords:
		DELETE(w,myDict)

	totalD = 0
	for i in countDel:
		totalD += i
	
	bkts.append(B)
	probesIns.append(totalI)
	avgIns.append(float(totalI/float(len(countIns))))
	probesDel.append(totalD)
	avgDel.append(float(totalD/float(len(countDel))))

print "# Items in dict: "+str(len(countIns))
print
print "\tTotal\t\tTotal\t\tAverage\t\tAverage"
print "\tInsert\t\tDelete\t\tInsert\t\tDelete"
print "bkts\tProbes\t\tProbes\t\tProbes\t\tProbes"

for i in range(len(bkts)):
	print str(bkts[i])+"\t"+str(probesIns[i])+"\t\t"+str(probesDel[i])+"\t\t"+str(avgIns[i])+"\t\t"+str(avgDel[i])
