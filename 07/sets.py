# sets

nums = { 1, 2 , 3, 4}
nums2 = set((1, 2, 3, 4))
# print(nums)
# print(nums2)
# print(type(nums))
# print(len(nums))

# no duplicates are allowed - it will ignore the duplicate
nums = {1, 2, 2, 3}
# print(nums)

# True is a dupe of 1 , False is a dupe of zero
nums = {1, True, 2, False, 3, 4, 0}
print(nums)

# check if a value is in a set
print(2 in nums)

# you cannot refer to an elements in the set with and index position or a key

# add a new element to a set

nums.add(8)
print(nums)

# add elements from one set to another
morenums = {5, 6, 7}
nums.update(morenums)
print(nums)

# you can use update with list, tuples, and dict too

# merge two diffrent sets to create a new set
one = {1, 2, 3}
two = {5, 6, 7}
mynewset = one.union(two)
print(mynewset)
print(one)
print(two)

# keep only the duplicates from two diffrent sets
one = {1, 2, 3}
two = {5, 2, 3}

one.intersection_update(two)
print(one)

# keep everything except the duplicates
one = {1, 2, 3}
two = {5, 2, 3}

one.symmetric_difference_update(two)
print(one)
