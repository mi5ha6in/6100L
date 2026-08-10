# Найти guess, такой что guess² ≈ x (в пределах epsilon), используя бисекцию
x = 0.4
epsilon = 0.01

if x >= 1:
    low = 0
    high = x
else:
    low = x
    high = 1

guess = (low + high) / 2

while abs(guess**2 - x) >= epsilon:
    if guess**2 < x:
        low = guess
    else:
        high = guess
    
    guess = (low + high) / 2
print(guess, 'is close to square root of', x)
