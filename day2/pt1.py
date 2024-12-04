
list = []
with open('input.txt', 'r') as file:
    for line in file:
        numbers = [int(num) for num in line.split()]
        list.append(numbers)
    

def isSafe(numbers):
    # Check if the list is strictly increasing and the differences are within bounds
    if all(1 <= numbers[i + 1] - numbers[i] <= 3 for i in range(len(numbers) - 1)):
        return True
    # Check if the list is strictly decreasing and the differences are within bounds
    elif all(1 <= numbers[i] - numbers[i+1] <= 3 for i in range(len(numbers) - 1)):
        return True
    else:
        return False

safe = 0
for l in list:
    if isSafe(l):
        safe += 1

print(safe)