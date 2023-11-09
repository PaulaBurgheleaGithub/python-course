def hello_world():
   print("Hello world!")
# hello_world()

# naming : all lowwer case
# PARAMTERS = placeholders for data we want a function to receive
def sum(x = 0, y = 0):
	if (type(x) is not int or type(y) is not int):
		return 0
	return x + y
# ARGRUMENT - the actual data when the function is called
total = sum("a", 3)
# print(total)

def multiple_items(*params):
	print(params)
	print(type(params))

# multiple_items("Paula", "John", "Ana")

def mult_named_itesm(**kwargs):
	print(kwargs)
	print(type(kwargs))

mult_named_itesm(first ="Paula", last= "Ana")
