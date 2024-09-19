# 1. Integer
int_num = 10  # Integer
print(f'Integer: {int_num}, Type: {type(int_num)}')

# 2. Float
float_num = 10.5  # Float
print(f'Float: {float_num}, Type: {type(float_num)}')

# 3. String
string_val = "Hello, World!"  # String
print(f'String: "{string_val}", Type: {type(string_val)}')

# 4. Boolean
bool_val = True  # Boolean
print(f'Boolean: {bool_val}, Type: {type(bool_val)}')

# 5. List
list_val = [1, 2, 3, 4, 5]  # List
print(f'List: {list_val}, Type: {type(list_val)}')

# 6. Tuple
tuple_val = (1, 2, 3)  # Tuple
print(f'Tuple: {tuple_val}, Type: {type(tuple_val)}')

# 7. Dictionary
dict_val = {'name': 'Alice', 'age': 30}  # Dictionary
print(f'Dictionary: {dict_val}, Type: {type(dict_val)}')

# 8. Set
set_val = {1, 2, 3, 4}  # Set
print(f'Set: {set_val}, Type: {type(set_val)}')

# Casting examples
# 1. Integer to Float
cast_to_float = float(int_num)  # Casting integer to float
print(f'Cast Integer to Float: {cast_to_float}, Type: {type(cast_to_float)}')

# 2. Float to Integer
cast_to_int = int(float_num)  # Casting float to integer
print(f'Cast Float to Integer: {cast_to_int}, Type: {type(cast_to_int)}')

# 3. String to Integer
string_num = "123"
cast_string_to_int = int(string_num)  # Casting string to integer
print(f'Cast String to Integer: {cast_string_to_int}, Type: {type(cast_string_to_int)}')

# 4. Integer to String
cast_int_to_string = str(int_num)  # Casting integer to string
print(f'Cast Integer to String: "{cast_int_to_string}", Type: {type(cast_int_to_string)}')

# 5. List to Tuple
list_to_tuple = tuple(list_val)  # Casting list to tuple
print(f'Cast List to Tuple: {list_to_tuple}, Type: {type(list_to_tuple)}')

# 6. Tuple to List
tuple_to_list = list(tuple_val)  # Casting tuple to list
print(f'Cast Tuple to List: {tuple_to_list}, Type: {type(tuple_to_list)}')
