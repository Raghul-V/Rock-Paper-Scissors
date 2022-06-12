# import the required modules
import ascii_art
import os
import random


CHOICES = {
	"R": {"name": "Rock", "value": 0, "logo": ascii_art.rock},
	"P": {"name": "Paper", "value": 1, "logo": ascii_art.paper},
	"S": {"name": "Scissors", "value": 2, "logo": ascii_art.scissors}
}


def winner(choice1, choice2):
	""" Returns 0 if choice1 wins, 1 if choice2 wins and -1 if ties """
	# if both are same then it's a tie
	if choice1 == choice2:
		return -1
	# else if the value of choice1 is exactly one more than the value of choice2 modulus 3, then choice1 wins
	if CHOICES[choice1]["value"] == (CHOICES[choice2]["value"] + 1) % 3:
		return 0
	# otherwise choice2 wins
	return 1


def rock_paper_scissors():
	# clear screen
	os.system("clear")
	
	greetings = "Welcome to Rock-Paper-Scissors!\n"
	print(greetings)
	
	# input the winning score
	winning_score = int(input("Enter the winning score of the game: "))
	
	# set scores to 0
	player_score = 0
	computer_score = 0

	choices_str = ", ".join([f"'{key}' for '{CHOICES[key]['name']}'" for key in CHOICES])
	
	# set a loop till anyone of those win
	while player_score < winning_score and computer_score < winning_score:
		# clear the screen
		os.system("clear")
		
		print(greetings)
		print(f"Your Score: {player_score}   Computer Score: {computer_score}   Winning Score: {winning_score}\n")
		
		# input from player
		player_choice = input(f"Your Choice: {choices_str} : ").upper()
		while player_choice not in CHOICES.keys():
			print("Enter a valid input!\n")
			player_choice = input(f"Your Choice: {choices_str} : ").upper()
		print(CHOICES[player_choice]["logo"])
		print(f"You chose: {CHOICES[player_choice]['name']}\n")
		# choose a random option for computer
		computer_choice = random.choice(list(CHOICES.keys()))
		print(CHOICES[computer_choice]["logo"])
		print(f"Computer chose: {CHOICES[computer_choice]['name']}\n\n")
		# evaluate, display and increment the score of winner
		winner_val = winner(player_choice, computer_choice)
		if winner_val == -1:
			print("It was a tie!")
		elif winner_val == 0:
			print("You win!")
			player_score += 1
		else:
			print("You lose!")
			computer_score += 1
		
		input("Press any key to continue...")

	os.system("clear")
	
	print(greetings)
	print(f"Your Score: {player_score}   Computer Score: {computer_score}   Winning Score: {winning_score}\n")
	
	# display the winner of the game
	if computer_score == winning_score:
		print("Sorry! You lost the game...\n")
	else:
		print("Wow! You won the game...\n")

	# ask for replay and if yes restart the game
	if input("Do you want to play again? 'Y' or 'N': ").upper() == "Y":
		rock_paper_scissors()


if __name__ == "__main__":
	rock_paper_scissors()


