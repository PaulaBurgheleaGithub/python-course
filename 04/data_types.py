import math
# string data type

# literal assigment

first = "Dave"
last = "Gray"

# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))

# constructor function

# pizza = str("Margherita")
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))

# concatenation

fullname = first + " " + last
# print(fullname)

# fullname += "!"
# print(first + " " + last + "!")

# casting a number to a string
decade = str(1980)
# print(type(decade))
# print(decade)
# print(fullname + " " + str(1984))

statement = "I like music from the " + decade + "s"
# print(statement) 

# Multiple lines
multiline = '''
Hey, how are you?   

I was just checking in.  
						All good?
'''

# print(multiline)

# escaping special characters

sentence = 'I\'m bacl at work!\tHey!\n\nWhere\'s this at\\located?'
# print(sentence)

# String Methods

# print(first)
# print(first.lower())
# print(first.upper())
# print(first)

# print(multiline.title())
# print(multiline.replace("good", "OK"))
# print(multiline)

# print(len(multiline))
# multiline +="                            "
# multiline = "                   " + multiline
# print(len(multiline))

# print(len(multiline.strip()))
# print(len(multiline.lstrip()))
# print(len(multiline.rstrip()))

# Build a menu

title = " menu".upper()
# print(title.center(20, "="))
# print("Coffee".ljust(16, ".") + "$1".rjust(4))
# print("Muffin".ljust(16, ".") + "$2".rjust(4))
# print("Chesecake".ljust(16, ".") + "$4".rjust(4))

# print("")

# String Index Values
# print(first[1])
# print(first[-1])
# print(first[1:])

# some methods return boolean data

# print(first.startswith("D"))
# print(first.endswith("Z"))

# Bolean data type
myvalue = True
x = bool(False)
# print(type(x))
# print(isinstance(myvalue, bool))

# Numberic data types

# integer type
price = 100
best_price = int(80)
# print(type(price))
# print(isinstance(best_price, int))

# float type
gpa = 3.28
y = float(1.14)
# print(type(gpa))

# complex type
comp_value = 5 + 3j
# print(type(comp_value))
# print(comp_value.real)
# print(comp_value.imag)

# Built in functions for numbers
# print(abs(gpa))
# print(gpa + -1)
# print(round(gpa))
# print(round(gpa, 1))

# using Math module
print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

# casting a string to a number

zipcode = "100001"
zip_value = int(zipcode)
print(type(zip_value))

# error when yoy attemnt to case incorrect data
