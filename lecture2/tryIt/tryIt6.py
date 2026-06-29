# YOU TRY IT!
# Write a program that
# Saves a secret number.
# Asks the user for a number guess.
# Prints whether the guess is too low, too high, or the same as the secret.

secret = 7
guess = int(input("Enter your number guess: "))

if secret == guess:
    print("Correct!")
elif secret > guess:
    print("Too low.")
else:
    print("Too high.")