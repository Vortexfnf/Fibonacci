Numbers = [0, 1]

count = int(input("How many numbers do you want?"))

while len(Numbers) != count:
    Sum = Numbers[len(Numbers) - 2] + Numbers[len(Numbers) - 1]
    Numbers.append(Sum)

print(Numbers)