# rock paper scissors game - User Input lesson
import sys
import random
from enum import Enum

def rps():
	game_count = 0
	player_wins = 0
	pyton_wins = 0

	# globel variables using Enum
	def play_rps():
		nonlocal player_wins
		nonlocal pyton_wins

		class RPS(Enum):
			ROCK = 1
			PAPER = 2
			SCISSORS = 3

		playerchoice = input("\nEnter ...\n1 for Rock,\n2 for Paper,\n3 for Scissors.\n\n")

		# will assume the user has good interntions
		player = int(playerchoice)
		if playerchoice not in ["1", "2", "3"]:
			print("You must enter : 1, 2 or 3")
			return play_rps()

		computerchoice = random.choice("123")

		computer = int(computerchoice)

		print(f"\nYou chose {str(RPS(player)).replace('RPS.', '').title()}.")
		print(f"Pyton chose {str(RPS(computer)).replace('RPS.', '').title()}.\n")

		def decide_winner(player, computer):
			nonlocal player_wins
			nonlocal pyton_wins
			# control flow with if
			if player == 1 and computer == 3:
				player_wins += 1
				return "You won!"
			elif player == 2 and computer == 2:
				player_wins += 1
				return "You won!"
			elif player == 3 and computer == 2:
				return "You win!"
			elif player == computer:
				return "Tie game!"
			else:
				pyton_wins += 1
				return "Python won!"
		game_result = decide_winner(player, computer)
		print(game_result)

		nonlocal game_count
		game_count += 1
		print(f"\nGAME COUNT: {str(game_count)}")
		print(f"\nPlayer wins: {str(player_wins)}")
		print(f"\nPyton wins: {str(pyton_wins)}")

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
	return play_rps

rock_paper_scissors = rps()
# the finction can be imported but it will only run when it is called
if __name__ == "__main__":
	rock_paper_scissors()
