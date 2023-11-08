# Tuples are simillar with list except that data inside that list will not change or the order?
# create
mytuple = tuple(('dave', 42, True))
anothertuple = (1, 4 , 2, "dana", 2, 2)
print(mytuple)
print(type(mytuple))
print(anothertuple)
print(type(anothertuple))

# copy a tuple - packing the tuple
newlist = list(mytuple)
newlist.append("Neil")
newtuple = tuple(newlist)
print(newtuple)

# hey is behaving like the remainder operator in JS
# (one, two, *hey) = anothertuple
# if we move the * to another value it still get's us the remaining values in betwen the two we have explicitly asked for. SO cool!
(one, *two, hey) = anothertuple
print(one)
print(two)
print(hey)
# counting the number of occurences
print(anothertuple.count(2))


