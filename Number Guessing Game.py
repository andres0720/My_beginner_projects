import random
#Main if statement
def random_number_game():
  correct_number = random.randint(1,100)

  guesses = 0
  while True:

    try:
      inputnumber = int(input("Guess a number Between 1 and 100!!  "))
      guesses += 1
      if inputnumber == correct_number:
        print(f'CORRECT! You have guessed the right number in {guesses} attempts')
        break
      elif inputnumber > correct_number:
        print("Wow there! try a smaller number")
      else:
        print("Oof! maybe a little higher?")
    except ValueError:
      print("Please enter a valid number.")
#Game restart function
def main():
  keep_playing = True
  while keep_playing:
    random_number_game()
    response = input("Do you want to play again? (Y/N) ")
    if response == 'y':
      keep_playing = True
    elif response == 'Y':
      keep_playing = True
    else:
      keep_playing = False
  print("Thanks For Playing!")

print("Welcome To My Number Guessing game!")
main()