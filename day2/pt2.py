
list = []
with open('input.txt', 'r') as file:
    for line in file:
        numbers = [int(num) for num in line.split()]
        list.append(numbers)
    

def isSafe(numbers):
    def isIncreasingAndTolerate(nums):
        # Check for strictly increasing
        increasing = all(1 <= nums[i+1] - nums[i] <= 3 for i in range(len(nums) - 1))
        # Check for strictly decreasing
        decreasing = all(1 <= nums[i] - nums[i+1] <= 3 for i in range(len(nums) - 1))
        return increasing or decreasing

    # Check if the original list is valid
    if isIncreasingAndTolerate(numbers):
        return True

    # Check if removing one element makes the list valid
    for i in range(len(numbers)):
        temp_numbers = numbers[:i] + numbers[i+1:]
        if isIncreasingAndTolerate(temp_numbers):
            return True

    return False

safe = 0
for l in list:
    if isSafe(l):
        safe += 1

print(safe)