# Initial string
text = "  hello world!  "

# Applying various string methods
text_upper = text.upper()  # Convert to uppercase
text_stripped = text.strip()  # Remove leading and trailing spaces
text_replaced = text_stripped.replace("world", "Python")  # Replace 'world' with 'Python'
text_split = text_replaced.split(" ")  # Split the string into a list of words
text_joined = "-".join(text_split)  # Join the words with a hyphen
text_find = text_joined.find("Python")  # Find the index of 'Python'
text_count = text_joined.count("o")  # Count occurrences of 'o'
text_capitalized = text_joined.capitalize()  # Capitalize the first word
text_isalpha = text_capitalized.isalpha()  # Check if all characters are alphabetic
text_endswith = text_capitalized.endswith("n")  # Check if string ends with 'n'

# Output results
print("Original Text:", text)
print("Uppercase:", text_upper)
print("Stripped:", text_stripped)
print("Replaced:", text_replaced)
print("Split into list:", text_split)
print("Joined with hyphen:", text_joined)
print("Index of 'Python':", text_find)
print("Count of 'o':", text_count)
print("Capitalized:", text_capitalized)
print("Is Alphabetic:", text_isalpha)
print("Ends with 'n':", text_endswith)
