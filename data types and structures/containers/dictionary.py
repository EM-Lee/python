### containers
# http://cs231n.github.io/python-numpy-tutorial/#python-containers

## dictionary {}
'''
a dictionary stores (key, value) pairs
'''
d = {'cat':'cute', 'dog':'furry'}
print(d['cat'])
print('cat' in d)
d['fish'] = 'wet'
print(d['fish'])
# print(d['monkey']) #KeyError: 'monkey' not a key of d
print(d.get('monkey', 'N/A'))
print(d.get('fish', 'N/A'))
del d['fish']
print(d.get('fish', 'N/A'))

# loop
print('')
d = {'person':2, 'cat':4, 'spider':8}
for animal in d:
    legs = d[animal]
    print('A %s has %d legs.' % (animal, legs))

# 'items' method to access to keys and their corresponding values
print('')
d = {'person':2, 'cat':4, 'spider':8}
for animal, legs in d.items():
    print('A %s has %d legs.' % (animal, legs))

# dictionary comprehension
# to construct a dictionary
print('')
nums = [0, 1, 2, 3, 4]
even_num_to_square = {x: x ** 2 for x in nums if x % 2 == 0}
print(even_num_to_square)
