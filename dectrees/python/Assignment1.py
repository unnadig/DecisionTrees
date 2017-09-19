
import monkdata as m
import dtree as dtree
import drawtree_qt5 as dt
import random

monk1 = m.monk1
monk2 = m.monk2
monk3 = m.monk3

monk1test = m.monk1test
monk2test = m.monk2test
monk3test = m.monk3test


mydic = {'a':4,'b':5}
print(mydic['a'])
print(mydic)
#print(monk1.attribute)


print(len(monk1))

print(m.attributes[2])

entropy1 = dtree.entropy(monk1)
print(entropy1)


entropy2 = dtree.entropy(monk2)
print(entropy2)

entropy3 = dtree.entropy(monk3)
print(entropy3)

def get_gain(monk):
	gain_list = []
	for attribute in range(6):
		gain_list.append(dtree.averageGain(monk,m.attributes[attribute]))
	return gain_list


gain_monk1 = get_gain(monk1)
gain_monk2 = get_gain(monk2)
gain_monk3 = get_gain(monk3)


print(gain_monk1)
print(gain_monk2)
print(gain_monk3)

BestAttribute = dtree.bestAttribute(monk3,m.attributes)
print(BestAttribute) 

#monk1_A5_1 = dtree.select(monk1,m.attributes[5],1)
#print(monk1_A5_1)

monk1_tree = dtree.buildTree(monk1,m.attributes)
#graf1 = dt.drawTree(monk1_tree)

monk2_tree = dtree.buildTree(monk2,m.attributes)
#graf2 = dt.drawTree(monk2_tree)

monk3_tree = dtree.buildTree(monk3,m.attributes)
#graf3 = dt.drawTree(monk3_tree)

print(dtree.check(monk1_tree, m.monk1))
print(dtree.check(monk1_tree, m.monk1test))
print(dtree.check(monk2_tree, m.monk2test))
print(dtree.check(monk3_tree, m.monk3test))

def partition(data,fraction):
	ldata = list(data)
	random.shuffle(ldata)
	breakPoint = int(len(ldata) * fraction)
	return ldata[:breakPoint], ldata[breakpoint:]

print(dtree.allPruned(monk1_tree))
dt.drawTree(dtree.allPruned()[1])
