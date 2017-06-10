#!/usr/bin/env python

#a constant to be placed in a bucket that holds the element targeted for deletion
global deleted
deleted = "**********"

#calls library hash function and returns it (mod buckets)
def h(x):
	return hash(x) % B

#returns empty dictionary
def MAKENULL():
	d = []
	for i in range(B):
		d.append(None)
	return d

#scans dictionary A from the bkt for h(x) until either x is found, or empty bkt is found
#or has scanned entire table, thus determining that x is not present
#probetype (boolean) indicates calling function, true for INSERT, false for DELETE
#returns index of bkt at which this stops for any above reasons
def locate(x,A,probetype):
	global countIns
	global countDel
	initial = h(x)
	i = 0 #counter for bkts scanned
	while (i<B) and (A[(initial+i)%B] != x) and (A[(initial+i)%B] is not None):
		i = i + 1
	if probetype:
		countIns.append(i+1)
	else:
		countDel.append(i+1)
	return (initial+i) % B

#like locate, but also stops at and returns a deleted entry
def locate1(x,A):
	global deleted
	global countIns
	initial = h(x)
	i = 0 #counter for bkts scanned
	while (i<B) and (A[(initial+i)%B] != deleted) and (A[(initial+i)%B] != x) and (A[(initial+i)%B] is not None):
		i = i + 1
	countIns.append(i+1)
	return (initial+i) % B

#returns true if item x is in dictionary A, false otherwise
def MEMBER(x,A):
	if A[locate(x,A)] == x:
		return True
	else:
		return False

#inserts item x into dictionary A, if not already a member of A
def INSERT(x,A):
	global deleted
	if A[locate(x,A,True)] == x: #x is already in A
		return
	bucket = locate1(x,A)
	if (A[bucket] is None) or (A[bucket] == deleted):
		A[bucket] = x
	else:
		print "INSERT failed: table is full"

#deletes item x from dictionary A, if present
def DELETE(x,A):
	global deleted
	bucket = locate(x,A,False)
	if A[bucket] == x:
		A[bucket] = deleted

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
