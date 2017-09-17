### containers
# http://cs231n.github.io/python-numpy-tutorial/#python-containers

## set {}
'''
A set is an unordered collection of distinct elements.
'''

animals = {'cat', 'dog'}
print('cat' in animals)
print('fish' in animals)
animals.add('fish')
print('fish' in animals)
print(len(animals))
animals.add('cat')
print(len(animals))
animals.remove('cat')
print(len(animals))

# loops
print('')
animals = {'cat', 'dog', 'fish'}
for idx, animal in enumerate(animals):
    print('#%d: %s' % (idx + 1, animal))
    
# set comprehensions
print('')
from math import sqrt
nums = {int(sqrt(x)) for x in range(30)}
print(nums)