# while loop - will execute a block of code while a condition is true
value = 1
# while value <= 10 : 
#    print(value)
#    if value == 5:
#       break
#    value +=1

# while value <= 10 : 
#    value +=1
#    if value == 5:
#       continue
#    print(value)
# else:
#    print("Value id now equal to "+ str(value))

# for loop

# for x in names:
#    print(x)
   
# for x in "Mississippi":
#    print(x)

# for x in names:
# 	if x == "Sara":
# 		break
# 	print(x)

# for x in names:
# 	if x == "Sara":
# 		continue
# 	print(x)

# ranges
# for x in range(4):
#    print(x)
# for x in range(2, 4):
#    print(x)
for x in range(10, 100, 10):
   print(x)
else:
   print("Glad that\'s over!")

names = ["Dave", "Sara", "John"]
actions = ["codes", "eats", "sleeps"]

# for name in names:
# 	for action in actions:
# 		print(name + " " + action + ".")

for action in actions:
	for name in names:
		print(name + " " + action + ".")

