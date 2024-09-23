# Python Sets - Examples in One File

# 1. Creating Sets
my_set = {1, 2, 3, 4}  # Using curly braces
another_set = set([1, 2, 2, 3])  # Using the set() function, duplicates removed

print("Initial sets:")
print("my_set:", my_set)          # Output: {1, 2, 3, 4}
print("another_set:", another_set)  # Output: {1, 2, 3}

# 2. Adding Elements to a Set
my_set.add(5)
print("\nAfter adding 5 to my_set:", my_set)  # Output: {1, 2, 3, 4, 5}

# 3. Removing Elements from a Set
my_set.remove(3)
print("\nAfter removing 3 from my_set:", my_set)  # Output: {1, 2, 4, 5}

# Using discard (won't raise an error if element is not found)
my_set.discard(6)  # 6 is not in my_set, no error
print("\nAfter discarding 6 (no change expected):", my_set)

# 4. Set Operations

# Union: Combine all unique elements from both sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2
print("\nUnion of set1 and set2:", union_set)  # Output: {1, 2, 3, 4, 5}

# Intersection: Elements common to both