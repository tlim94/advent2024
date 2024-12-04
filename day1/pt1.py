
with open('input.txt', 'r') as file:
    listOne = []
    listTwo = []

    for line in file:
        one, two = line.split()
        listOne.append(one)
        listTwo.append(two)        
    
listOne.sort()
listTwo.sort()

n = len(listOne)
totalDist = 0

for i in range(n):
    dist = abs(int(listOne[i]) - int(listTwo[i]))
    totalDist += dist

print(totalDist)