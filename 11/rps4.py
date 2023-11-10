# rock paper scissors game - User Input lesson
import sys
import random
from enum import Enum

game_count = 0
# globel variables using Enum
def play_rps():

	class RPS(Enum):
		ROCK = 1
		PAPER = 2
		SCISSORS = 3

	playerchoice = input("\nEnter ...\n1 for Rock,\n2 for Paper,1\n3 for Scissors.\n\n")

	# will assume the user has good intentions
	player = int(playerchoice)
	if playerchoice not in ["1", "2", "3"]:
		print("You must enter : 1, 2 or 3")
		return play_rps()

	computerchoice = random.choice("123")

	computer = int(computerchoice)

	print("\nYou chose " + str(RPS(player)).replace('RPS.', "") + ".")
	print("Pyton chose " + str(RPS(computer)).replace('RPS.', "") + ".\n")

	def decide_winner(player, computer):
		# control flow with if
		if player == 1 and computer == 3:
			return "You win!"
		elif player == 2 and computer == 2:
			return "You win!"
		elif player == 3 and computer == 2:
			return "You win!"
		elif player == computer:
			return "Tie game!"
		else:
			return "Python won!"
	game_result = decide_winner(player, computer)
	print(game_result)

	global game_count
	game_count += 1
	print("\nGAME COUNT:	" + str(game_count))

	print("\nPlay again?")
	while True:
		playagain = input("\n Y for Yes or \b Q to Quit\n")
		if playagain.lower() not in ["y", "q"]:
			continue
		else:
			break

	if playagain.lower() == "y" :
		return play_rps()
	else:
		print("\nThank you for playing!")
		sys.exit("Bye!")

play_rps()
