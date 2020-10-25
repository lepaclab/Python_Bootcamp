from random import randint  # use randint(a, b) to generate a random number between a and b

number = randint(1,10)

guess = None

while True:
	guess = input("Pick up a number from 1 to 10: ")
	guess = int(guess)
	if guess < number:
		print("too low")
	elif guess > number:
		print("too high")
	else:
		print("you won")
		play_again = input("Do you want to play again? (y/n) ")
		if play_again == "y":
			number = randint(1,10)
			guess = None
		else:
			print("Thank for you playing")
			break

