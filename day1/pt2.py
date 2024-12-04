from collections import Counter

with open('input.txt', 'r') as file:
    listOne = []
    listTwo = []

    for line in file:
        one, two = line.split()
        listOne.append(one)
        listTwo.append(two)

listTwoCounter = Counter(listTwo)
n = len(listOne)
similarityScore = 0

for i in range(n):
    curr = listOne[i]
    sim = int(curr) * int(listTwoCounter[curr])
    similarityScore += sim

print(similarityScore)