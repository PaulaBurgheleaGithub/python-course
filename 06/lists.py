# list seems to be the equivalent of the JS array

users = ['Dave', 'John', 'Sarah']
data = ['Dave', 42, True]

emptylist = []

# print('Dave' in emptylist)

# print(users[0])
# print(users[-2])
# print(users.index('Sarah'))
# very simillar to slice from JS, it does not give us the last value we have entered
# print(users[0:2])
# print(users[1:])
# print(users[-3:-1])

# print(len(data))
# append / add another value to the list
users.append('Elsa')
# print(users)
# add a list to another list
users += ['Jason']
emptylist += 'Jason'
# print(users)
# print(emptylist)

users.extend(['Paula', 'Maria'])
# print(users)

# users.extend(data)
# print(users)

# insert at a specific position
users.insert(0, 'Bob')
# print(users)
# insert at position 2 and stop at that position
users[2:2] = ["Eddie", "Alex"]
# print(users)
# replace at a specific position , refering to a slice
users[1:3] = ["Rob", "JPJ"]
# print(users)

users.remove('Bob')
# print(users)

# pop off a value
# print(users.pop())
# print(users)

del users[0]
# print(users)
# del data
data.clear()
# print(data)

# sort
users[1:2] = ['dave']
# this will be case sensitive
users.sort()
# print(users)
# sort case insensitive
users.sort(key=str.lower)
# print(users)

nums = [4, 42, 78, 1, 5]
nums.reverse()
# print(nums)

# nums.sort(reverse=True)
# print(nums)

# all the methods above will mutate the list, what if we wanted to change the list for just one instance but leave the original unchanged
# print(sorted(nums, reverse=True))
# print(nums)

# copy the list
# using the copy method
numscopy = nums.copy()
# using the list constructor
mynums = list(nums)
# slice the full list
mycopy = nums[:]

# print(numscopy)
# print(mynums)
# mycopy.sort()
# print(mycopy)
# print(nums)

# check the data type
# print(type(nums))
# mylist = list([1, "Paula", True])
# print(mylist)

# python 101 
n1 = [x for x in range(10) if x % 2 == 0] # even
n2 = [x for x in range(10) if x % 2 != 0] # odd
print(n1)
print(n2)

zipped = list(zip(n1, n2))
print(zipped) # [(0, 1), (2, 3), (4, 5), (6, 7), (8, 9)]
zipped_2 = zipped[::-1]
print(zipped_2) # [(8, 9), (6, 7), (4, 5), (2, 3), (0, 1)]

zipped_2.extend(n2[::-1])
print(zipped_2) #[(8, 9), (6, 7), (4, 5), (2, 3), (0, 1), 9, 7, 5, 3, 1]

n1[-5:-5] = [999]
print(n1)
n1[1:4] = ['a', 'b', 'c']
print(n1) #[999, 'a', 'b', 'c', 6, 8]

lst = sorted(n1, key=lambda x: (isinstance(x, int), x), reverse=True)
print(lst) #[999, 8, 6, 'c', 'b', 'a'] 
