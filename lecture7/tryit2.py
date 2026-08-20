def div_by(n, d):
    """
    n and d are ints > 0
    Returns True if d divides n evenly and False otherwise
    """
    return n % d == 0

for i in range(1, 21):
    if div_by(i, 3):
        print(i, "делится на 3")
    else:
        print(i, "не делится на 3")
