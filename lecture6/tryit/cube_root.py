x = 27
epsilon = 0.01

if x >= 1:
    low = 0
    high = x
else:
    low = x
    high = 1

guess = (low + high) / 2

while abs(guess**3 - x) >= epsilon:
    if guess**3 > x:
        high = guess
    else:
        low = guess

    guess = (low + high) / 2
print(guess)