import collections
print ('Regular dictionary:')
d = {}
d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
d['d'] = 'D'
d['e'] = 'E'

for k, v in d.items():
    print(k,v)

print ('\nOrderedDict:')
d = collections.OrderedDict()
d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
d['d'] = 'D'
d['e'] = 'E'

for k, v in d.items():
    print (k, v)


# output:Regular dictionary:
# ('a', 'A')
# ('c', 'C')
# ('b', 'B')
# ('e', 'E')
# ('d', 'D')

# OrderedDict:
# ('a', 'A')
# ('b', 'B')
# ('c', 'C')
# ('d', 'D')
# ('e', 'E')