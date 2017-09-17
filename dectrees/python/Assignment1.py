import monkdata as m
import dtree as dtree

monk1 = m.monk1
monk2 = m.monk2
monk3 = m.monk3

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

#for monk in range(1,4):
#	gain_list = []
#	for attribute in range(6):
#		gain_list.append(dtree.averageGain('monk{}'.format(monk),m.attributes[attribute])
#		print(gain_list)


#for i in range(1, 4):
#	for j in range(6):
#		gain[str(i)] = i
#		print('s')

#print(gain['2'])