# closure - whne a nested function has access to the parent function

def parent_func(person, coins):
	# coins = 3

	def play():
		nonlocal coins
		coins -= 1
		if coins > 1:
			print ("\n" + person + " has " + str(coins) + " coins left.")
		elif coins == 1:
			print ("\n" + person + " has " + str(coins) + " coin left.")
		else:
			print ("\n" + person + " is out of coins.")

	return play

tommy = parent_func("Tommy", 3)
jenny = parent_func("Jenny", 5)

tommy()
tommy()

jenny()
