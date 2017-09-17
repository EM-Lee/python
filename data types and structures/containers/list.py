### containers
# hthttp://cs231n.github.io/python-numpy-tutorial/#python-containers

## list []
'''
A list is the Python equivalent of an array,
but is resizeable and can contain elements of different types.
'''

xs = [3, 1, 2]
print(xs, xs[2])
print(xs[-1])
xs[2] = 'foo'
print(xs)
xs.append('bar')
print(xs)
x = xs.pop() #remove and return the last element of the list
print(x, xs)

# slicing
print('')
nums = list(range(5))
print(nums)
print(nums[2:4])
print(nums[2:])
print(nums[:2])
print(nums[:]) #get a slice of the whole list
print(nums[:-1])
nums[2:4] = [8, 9]
print(nums)

# loops
print('')
animals = ['cat', 'dog', 'monkey']
for animal in animals:
    print(animal)

# if you want access to the index of each element
animals = ['cat', 'dog', 'monkey']
for idx, animal in enumerate(animals):
    print("#%d: %s" % (idx + 1, animal))
    
animals = ['cat', 'dog', 'monkey']
for idx, animal in enumerate(animals, 1):
    print(idx, animal)

# list comprehension example
print('')
nums = [0, 1, 2, 3, 4]
squares = []
for x in nums:
    squares.append(x ** 2)
print(squares)

# simpler
print('')
nums = [0, 1, 2, 3, 4]
squares = [x ** 2 for x in nums]
print(squares)

# simpler with conditions
print('')
nums = [0, 1, 2, 3, 4]
even_squares = [x ** 2 for x in nums if x % 2 == 0]
print(even_squares)
