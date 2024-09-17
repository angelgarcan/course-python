
# Python Expressions

# 1. Arithmetic Expressions: These include basic mathematical operations.
x = 5 + 3  # Addition
y = 10 - 2  # Subtraction
z = 4 * 2  # Multiplication
a = 10 / 2  # Division (returns a float)
b = 10 // 3  # Floor division (returns an integer)
c = 2 ** 3  # Exponentiation (power)
d = 10 % 3  # Modulus (remainder)

# 2. Comparison Expressions: Evaluate the relationship between two values, resulting in a boolean.
x_comp = 5 > 3  # Greater than (True)
y_comp = 5 < 3  # Less than (False)
z_comp = 5 == 5  # Equality (True)
a_comp = 5 != 3  # Not equal (True)
b_comp = 5 >= 3  # Greater than or equal to (True)
c_comp = 5 <= 3  # Less than or equal to (False)

# 3. Logical Expressions: Use 'and', 'or', and 'not' operators to evaluate logical conditions.
x_logic = (5 > 3) and (8 > 6)  # Both conditions are True, result is True
y_logic = (5 < 3) or (8 > 6)  # One condition is True, result is True
z_logic = not (5 < 3)  # Negates the False condition, result is True

# 4. Bitwise Expressions: Work at the bit level (binary digits).
x_bit = 5 & 3  # Bitwise AND
y_bit = 5 | 3  # Bitwise OR
z_bit = 5 ^ 3  # Bitwise XOR
a_bit = ~5  # Bitwise NOT
b_bit = 5 << 1  # Left shift
c_bit = 5 >> 1  # Right shift

# 5. Membership Expressions: Check for membership within a sequence (like a list, tuple, string).
my_list = [1, 2, 3, 4]
x_mem = 3 in my_list  # Checks if 3 is in the list (True)
y_mem = 5 not in my_list  # Checks if 5 is not in the list (True)

# 6. Identity Expressions: Compare the memory location of two objects.
x_id = [1, 2, 3]
y_id = x
z_id = [1, 2, 3]

x_is_y = x_id is y_id  # True (same object in memory)
x_is_z = x_id is z_id  # False (different objects, even if they have the same content)

# 7. Lambda Expressions: Create anonymous functions using the 'lambda' keyword.
add = lambda a, b: a + b
result = add(2, 3)  # Output: 5
