# rock paper scissors game - User Input lesson
import sys
import random
from enum import Enum

def rps(name='PlayerOne'):
	game_count = 0
	player_wins = 0
	pyton_wins = 0

	# globel variables using Enum
	def play_rps():
		nonlocal name
		nonlocal player_wins
		nonlocal pyton_wins

		class RPS(Enum):
			ROCK = 1
			PAPER = 2
			SCISSORS = 3

		playerchoice = input(f"\n{name}, please enter ...\n1 for Rock,\n2 for Paper,\n3 for Scissors.\n\n")

		# will assume the user has good interntions
		player = int(playerchoice)
		if playerchoice not in ["1", "2", "3"]:
			print(f"{name}, please enter : 1, 2 or 3")
			return play_rps()

		computerchoice = random.choice("123")

		computer = int(computerchoice)

		print(f"\n{name}, you chose {str(RPS(player)).replace('RPS.', '').title()}.")
		print(f"Pyton chose {str(RPS(computer)).replace('RPS.', '').title()}.\n")

		def decide_winner(player, computer):
			nonlocal name
			nonlocal player_wins
			nonlocal pyton_wins
			# control flow with if
			if player == 1 and computer == 3:
				player_wins += 1
				return f"{name} won!"
			elif player == 2 and computer == 2:
				player_wins += 1
				return f"{name} won!"
			elif player == 3 and computer == 2:
				return f"{name} won!"
			elif player == computer:
				return "Tie game!"
			else:
				pyton_wins += 1
				return f"Python won!\nSorry ...{name} :("
		game_result = decide_winner(player, computer)
		print(game_result)

		nonlocal game_count
		game_count += 1
		print(f"\nGAME COUNT: {game_count}")
		print(f"\n{name}'s wins: {player_wins}")
		print(f"\nPyton wins: {pyton_wins}")

		print(f"\nPlay again, {name}?")
		while True:
			playagain = input("\n Y for Yes or \b Q to Quit\n")
			if playagain.lower() not in ["y", "q"]:
				continue
			else:
				break

		if playagain.lower() == "y" :
			return play_rps()
		else:
			print(f"\nThank you for playing!")
			sys.exit(f"Bye {name}!")
	return play_rps


# the finction can be imported but it will only run when it is called
if __name__ == "__main__":
	import argparse

	parser = argparse.ArgumentParser(
		description="Provides a personalised game experience."
	)

	parser.add_argument(
		"-n", "--name", metavar="name",
		required=True, help="The name of the player."
	)

	args = parser.parse_args()

	rock_paper_scissors = rps(args.name)
	rock_paper_scissors()
