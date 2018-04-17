
import monkdata as m
import dtree as d
import random
import drawtree_qt5 as draw
import os
'''
# Entropy
print (d.entropy(m.monk1))
print (d.entropy(m.monk2))
print (d.entropy(m.monk3))
'''

'''
# Information Gain
for i in range(0, 6):
    print ('%.4f' %d.averageGain(m.monk1, m.attributes[i]), end = ' & ')
print ('\n', end = ' ')
for i in range(0, 6):
    print ('%.4f' %d.averageGain(m.monk2, m.attributes[i]), end = ' & ')
print ('\n', end = ' ')
for i in range(0, 6):
    print ('%.4f' %d.averageGain(m.monk3, m.attributes[i]), end = ' & ')
print ('\n', end = ' ')
'''

'''
# Build Decision Tree t3: by ourselves
bestAttr_l0 = d.bestAttribute(m.monk1, m.attributes)
print (bestAttr_l0)
for i in bestAttr_l0.values:
    l1 = d.select(m.monk1, bestAttr_l0, i)
    print (i, end = ' ')
    if d.allPositive(l1):
        print ('+')
    elif d.allNegative(l1):
        print ('-')
    else:
        print (d.bestAttribute(l1, [x for x in m.attributes if x != bestAttr_l0]))
'''

'''
# Build Decision Tree T2: by function:buildtree
t = d.buildTree(m.monk1, m.attributes, 2)
print (t)
# print(d.check(t, m.monk1test))
'''

'''
# Build Decision Tree T3: compute error
t3 = d.buildTree(m.monk1, m.attributes)
print ('%.4f' % (1 - d.check(t3, m.monk1)), end = ' & ')
print ('%.4f' % (1 - d.check(t3, m.monk1test)))
t2 = d.buildTree(m.monk2, m.attributes)
print ('%.4f' % (1 - d.check(t2, m.monk2)), end = ' & ')
print ('%.4f' % (1 - d.check(t2, m.monk2test)))
t3 = d.buildTree(m.monk3, m.attributes)
print ('%.4f' % (1 - d.check(t3, m.monk3)), end = ' & ')
print ('%.4f' % (1 - d.check(t3, m.monk3test)))
'''


# Pruning
def partition(data, fraction):
    ldata = list(data)
    random.shuffle(ldata)
    breakPoint = int(len(ldata) * fraction)
    return ldata[:breakPoint], ldata[breakPoint:]
	
def main():
	monk1train, monk1val = partition(m.monk1, 0.3)
	t3 = d.buildTree(monk1train, m.attributes)
	minError = 1 - d.check(t3, monk1val)
	while True:
		min = minError
		tSet = d.allPruned(t3)
		for t in tSet:
			temp = 1 - d.check(t, monk1val);
			if temp < min:
				min = temp
				t3 = t;
		if min >= minError:
			break
	return 1 - d.check(t3, m.monk1test)


a=0

for i in range(0,10):
	a+=main()

print(a/10)

os.system('pause')