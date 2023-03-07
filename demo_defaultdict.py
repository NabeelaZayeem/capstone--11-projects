from collections import defaultdict,Counter,OrderedDict,ChainMap
d1=defaultdict(int)
d2=defaultdict(list)
d1['a']=1
d1['b']=2
d2['x']=[1,22,44]
print(d1)
print(d2)
#########COUNTER############
l=[1,2,3,1,3,5,2,4,5,4,6,4,2]
l2=Counter(l)
print(l2)
###########ORDERED DICT#############


####CHAIN MAP###
dict1={'a':10,'b':20}
dict2={'x':20,'y':24}
dt=ChainMap(dict1,dict2)
print(dt)
print(dt['a'])