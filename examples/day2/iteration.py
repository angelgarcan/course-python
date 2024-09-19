# Simple range example: stop at 5 (5 is not included)
for i in range(5):
    print(i)
# Output: 0 1 2 3 4

# Range with start and stop
for i in range(2, 8):
    print(i)
# Output: 2 3 4 5 6 7

# Range with start, stop, and step
for i in range(1, 10, 2):
    print(i)
# Output: 1 3 5 7 9


# Iterating over a list
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)
# Output: apple banana cherry

# Using for loop with range
for i in range(3):
    print(f'Iteration: {i}')
# Output: 
# Iteration: 0
# Iteration: 1
# Iteration: 2

# Simple while loop
count = 0
while count < 5:
    print(f'Count is {count}')
    count += 1
# Output:
# Count is 0
# Count is 1
# Count is 2
# Count is 3
# Count is 4

for i in range(5):
    if i == 3:
        break  # Break out of the loop when i is 3
    print(i)
# Output: 0 1 2

for i in range(5):
    if i == 2:
        continue  # Skip the iteration when i is 2
    print(i)
# Output: 0 1 3 4
