# global scope
name = "Dave"
count = 1

def greeding(name):
   color = "blue"
   count = 2
   print(color, name)
# greeding("Paula")
greeding("John")


def another():
	greeding(name)
# vs
def another2():
	color = "red"
	def greeding(name):
		# print(color)
		print(color, name)
	greeding("Paula")

another()
another2()
