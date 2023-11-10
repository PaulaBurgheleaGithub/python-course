import sys
import random

game_count = 0

def guess(name='PlayerOne'):
	game_count = 0
	player_wins = 0

	def play_guess():
		nonlocal name
		nonlocal player_wins

		playerchoice = input(f"\nWelcome, {name}! To start the game please enter a number between 1 and 3\n")

		player = int(playerchoice)
		# if the user does not enter a number in the range
		if playerchoice not in ["1", "2", "3"]:
			print(f"{name}, please enter : 1, 2 or 3")
			return play_guess()
		
		computerchoice = random.choice("123")
		computer = int(computerchoice)
		
		print(f"\n{name}, you chose {playerchoice}.")
		print(f"The winning number was: {computer}.\n")

		def decide_winner(player, computer):
			nonlocal name
			nonlocal player_wins
			if player == computer:
				player_wins += 1
				return f"{name} won!"
			else:
				return f"Sorry ...{name}, you did not guess the number!"

		game_result = decide_winner(player, computer)
		print(game_result)

		nonlocal game_count
		game_count += 1
		print(f"\nGAME COUNT: {game_count}")
		print(f"\n{name}'s wins: {player_wins / game_count:.2%}")

		print(f"\nPlay again, {name}?")
		while True:
			playagain = input("\n Y for Yes or \b Q to Quit\n")
			if playagain.lower() not in ["y", "q"]:
				continue
			else:
				break

		if playagain.lower() == "y" :
			return play_guess()
		else:
			print(f"\nThank you for playing!")
			sys.exit(f"Bye {name}!")
	return play_guess

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

	rock_paper_scissors = guess(args.name)
	rock_paper_scissors()
