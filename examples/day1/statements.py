

# 1. Assignment Statement
# Assign values to variables
x = 5
y = 10
name = "Test"

# 2. Print Statement
# Display output to the console
print("The value of x is: {x}")

# 3. If-Else Conditional Statement
# Make decisions based on conditions
if x > y:
    print("x is greater than y")
else:
    print("x is less than or equal to y")

# 4. For Loop
# Iterate over a sequence (like a list or range)
for i in range(5):
    print("Iteration: {i}")

# 5. While Loop
# Repeatedly execute code while a condition is true
count = 0
while count < 3:
    print(f"Count: {count}")
    count += 1

# 6. Function Definition and Call Statement
# Define a reusable block of code and call it
def greet(person):
    return f"Hello, {person}!"

print(greet(name))

# 7. List Comprehension
# Short and readable way to create lists
squares = [num ** 2 for num in range(5)]
print(f"Squares: {squares}")

# 8. Try-Except Statement
# Handle exceptions (errors)
try:
    result = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    print("You can't divide by zero!")
finally:
    print("This block runs no matter what.")

# 9. Import Statement
# Importing external modules
import math
print(f"The square root of 16 is: {math.sqrt(16)}")
