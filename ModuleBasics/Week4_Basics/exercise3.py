import random

secret_number = random.randint(1, 10)
attempts = 0

print("Guess the secret number! It is between 1 and 10.")

while True:
   try:
       user_guess = int(input("Enter your guess: "))
       attempts += 1

       if user_guess == secret_number:
           print(f"Congratulations! You guessed the number in {attempts} attempts.")
           break
       elif user_guess < secret_number:
           print("The secret number is higher.")
       else:
           print("The secret number is lower.")
   except ValueError:
       print("Invalid input. Please enter an integer.")
