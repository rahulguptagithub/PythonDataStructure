# Q-1- Discuss string slicing and provide examples

# SOLUTION 1- 
# String slicing is a powerful feature in Python that allows you to extract a specific portion of a string.
# EXAMPLE-
#         string[start:end:step]

# start: The index where the slice begins (inclusive).
# end: The index where the slice ends (exclusive).
# step: The interval between each index in the slice (optional).

# BASIC SLICING:
# text = "Hello, World!"
# slice1 = text[0:5]  # 'Hello'
# slice2 = text[7:12]  # 'World'
# print(slice1)  # Output: Hello
# print(slice2)  # Output: World

# Q-2- Explain the key features of lists in Python

# SOLUTION-2-
# Lists in Python are versatile and widely used data structures that allow you to store and manipulate collections of items. 
# -Lists maintain the order of elements.
# -Lists are mutable, meaning you can modify them after creation. 
# -Lists can contain elements of different data types. For example, a list can include
# integers, strings, floats, and even other lists.
# EXAMPLE-

# mixed_list = [1, "hello", 3.14, [2, 3]]

# Python lists come with a variety of built-in methods for common operations:
# Appending elements: list.append(item)
# Inserting elements: list.insert(index, item)
# Removing elements: list.remove(item) or list.pop(index)
# Sorting: list.sort()
# Reversing: list.reverse()
# Finding length: len(list)

# EXAMPLE-: NESTED LISTS:
# nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# EXAMPLE:Indexing and Slicing
# example_list = [10, 20, 30, 40, 50]
# print(example_list[1])    # Output: 20
# print(example_list[1:4])  # Output: [20, 30, 40]

# EXAMPLE:Copying Lists:
# original_list = [1, 2, 3]
# copied_list = original_list[:]  # or original_list.copy()


# QUESTION 3- DescrIbe hoW to access modify and delete elements on a list with examples.

# SOLUTION3-
# Accessing, modifying, and deleting elements in a list in Python is straightforward.
# EXAMPLES: Accessing Elements:

# # Example list
# fruits = ['apple', 'banana', 'cherry', 'date']

# # Accessing elements
# first_fruit = fruits[0]  # 'apple'
# second_fruit = fruits[1]  # 'banana'
# last_fruit = fruits[-1]  # 'date' (negative index)

# print(first_fruit)  # Output: apple
# print(second_fruit)  # Output: banana
# print(last_fruit)  # Output: date


# -Modifying Elements
# You can change the value of an existing element by accessing it through its index.
# # Modifying elements
# fruits[1] = 'blueberry'  # Change 'banana' to 'blueberry'

# print(fruits)  # Output: ['apple', 'blueberry', 'cherry', 'date']


# -Deleting Elements
# WE can remove elements from a list using several methods:

# Using del statement:
# del fruits[0]  # Deletes 'apple'
# print(fruits)  # Output: ['blueberry', 'kiwi', 'mango']

# -Summary
# Accessing elements: Use indexing (e.g., list[index]).
# Modifying elements: Assign a new value to an index (e.g., list[index] = new_value).
# Deleting elements: Use del, remove(), or pop() methods to remove elements based on index or value.

# QUESTION 4- Compare and contrast tuples and lists with examples.

# SOLUTION 4- Tuples and lists are both built-in data structures in Python that can store collections of items.


# -Key Differences

# Feature	     Lists	                                                Tuples

# Mutability	 Mutable (can be modified)	                        Immutable (cannot be modified)
# Syntax	     Defined with square brackets []	                Defined with parentheses ()
# Performance	 Slower due to mutability	                        Faster due to immutability
# Use Cases	 Suitable for collections of items that may change	Suitable for fixed collections of items
# Methods	     More methods available (e.g., append, remove)	    Fewer methods (e.g., count, index)
# Memory Usage  Generally uses more memory	                    More memory-efficient


# Examples -List Example:
# 1. Creating Lists and Tuples:
# fruits = ['apple', 'banana', 'cherry']
# print(fruits)  # Output: ['apple', 'banana', 'cherry']

# Examples -Tuple Example:
# fruits_tuple = ('apple', 'banana', 'cherry')
# print(fruits_tuple)  # Output: ('apple', 'banana', 'cherry')


# 5. Use Cases
# Lists are typically used when you need a collection of items that may change,
# such as maintaining a list of user inputs or tasks.

# Tuples are often used to represent fixed collections of items,
# such as coordinates (x, y) or returning multiple values from a function.

# Summary
# Lists are mutable, allowing for modification, while tuples are immutable.
# Lists use more memory and are generally slower due to their mutability.
# Tuples are better suited for fixed collections of items and can be used as keys in dictionaries, while lists cannot.
        

# QUESTION 5- Describe the key features of sets and provide examples of their use.

# SOLUTION 5- Key Features of Sets:

# 1-Unordered Collection:
# EXAMPLES- 
# my_set = {3, 1, 4}
# print(my_set)  # Output: {1, 3, 4} (or similar, but order may vary)

# EXAMPLE 2- Unique Elements
# my_set = {1, 2, 2, 3}
# print(my_set)  # Output: {1, 2, 3}

# EXAMPLE 3- Immutable Elements:
# valid_set = {1, 'hello', (2, 3)}
# # invalid_set = {1, [2, 3]}  # This will raise a TypeError

# EXAMPLE 4-
# Mathematical Set Operations:
# Sets support standard set operations such as union, intersection, difference, and symmetric difference.

# set_a = {1, 2, 3}
# set_b = {3, 4, 5}

# union = set_a | set_b  # {1, 2, 3, 4, 5}
# intersection = set_a & set_b  # {3}
# difference = set_a - set_b  # {1, 2}
# symmetric_difference = set_a ^ set_b  # {1, 2, 4, 5}


# Efficient Membership Testing in Large Data Sets:
# Sets are ideal for situations where you need to frequently check the presence of an item in a large collection.

# Example:
# Checking for banned users in a forum.
# banned_users = {'user5', 'user8', 'user10'}
# current_user = 'user8'

# if current_user in banned_users:
#     print("Access denied.")


# QUERSTION 6- Discuss the use cases of tuples and sets in Python programming.

# SOLUTION 6- Use Cases of Tuples and Sets in Python Programming:
# TUPLES-
# Tuples are immutable, ordered collections that are ideal when you need a fixed structure or want to ensure data integrity.

# Use Cases of Tuples:
# Storing Immutable Data: Tuples are often used when you need to store a collection of items that shouldn't be modified
# throughout the program. This immutability ensures data safety.

# EXAMPLE:
# coordinates = (40.7128, -74.0060)  # New York City latitude and longitude

# Return Multiple Values from a Function: Tuples are commonly used to return multiple values from a function,
# where you can unpack them into separate variables.

# Example:
# def get_person_info():
#     name = "Alice"
#     age = 30
#     return (name, age)

# person_name, person_age = get_person_info()

# SETS:
# Sets are unordered, mutable collections that store unique elements and are highly optimized for membership testing
# and mathematical set operations.

# Use Cases of Sets:
# Removing Duplicates: One of the most common use cases for sets is to remove duplicates from a collection (like a list).
# This is particularly useful when you want to ensure all elements are unique.

# Example:
# my_list = [1, 2, 2, 3, 4, 4, 5]
# unique_set = set(my_list)
# print(unique_set)  # Output: {1, 2, 3, 4, 5}

# Efficient Membership Testing: Sets provide an average time complexity of O(1) for membership tests,
# making them ideal for tasks that require frequent checking for element presence.

# Example:
# allowed_ips = {'192.168.1.1', '192.168.1.2', '192.168.1.3'}
# if '192.168.1.2' in allowed_ips:
#     print("Access granted.")

# Mathematical Set Operations (Union, Intersection, Difference): Sets are designed for operations like union,
# intersection, difference, and symmetric difference. This makes them extremely useful in data analysis and filtering tasks.

# Example:
# set_a = {1, 2, 3}
# set_b = {3, 4, 5}

# union = set_a | set_b  # {1, 2, 3, 4, 5}
# intersection = set_a & set_b  # {3}
# difference = set_a - set_b  # {1, 2}

# Conclusion:
# Tuples are best suited for scenarios where data immutability is required, like storing coordinates, returning multiple values
# from functions, or using immutable sequences as dictionary keys.
# Sets are optimal when you need to ensure uniqueness, perform membership checks efficiently, or conduct operations involving 
# unions, intersections, and differences between collections.

# QUESTION 7- Describe how to add modify and delete items in a dictionary with examples.
# SOLUTION 7- Dictionaries in Python are mutable collections of key-value pairs, where each key is unique.

# Adding Items to a Dictionary:
# # Initial dictionary
# my_dict = {'name': 'Alice', 'age': 25}

# # Adding a new key-value pair
# my_dict['city'] = 'New York'

# print(my_dict)  
# # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}

# Modifying Items in a Dictionary:
# # Initial dictionary
# my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}

# # Modifying an existing key-value pair
# my_dict['age'] = 26

# print(my_dict)
# # Output: {'name': 'Alice', 'age': 26, 'city': 'New York'}

# Deleting Items from a Dictionary:
# # Initial dictionary
# my_dict = {'name': 'Alice', 'age': 27, 'city': 'San Francisco'}

# # Deleting a key-value pair
# del my_dict['city']

# print(my_dict)
# # Output: {'name': 'Alice', 'age': 27}

# Summary:
# Adding items: Assign a value to a new key.
# my_dict['new_key'] = value

# Modifying items: Reassign a new value to an existing key.
# my_dict['existing_key'] = new_value

# Deleting items:

# del to delete a key-value pair.
# pop() to remove a key and return its value.
# popitem() to remove the last inserted key-value pair.
# clear() to remove all key-value pairs from the dictionary.


# QUESTION-8- DIscuss the importance of dictionary keys being immutable and provide examples.
# SOLUTION- 8-
# -Efficient Hashing and Retrieval:
# Python dictionaries use a hash table internally for storing key-value pairs. To retrieve values efficiently,
# the dictionary hashes the key using the hash() function.

# -Ensuring Dictionary Integrity:
# If mutable objects like lists were allowed as dictionary keys, modifying the key after it has been inserted could 
# break the internal structure of the dictionary. The dictionary would no longer be able to locate the key properly, 
# leading to data corruption or errors.

# Examples of Valid and Invalid Dictionary Keys:

# -Valid Keys (Immutable Objects):
# Strings: Strings are immutable in Python, so they can be used as dictionary keys.
# my_dict = {'name': 'Alice', 'city': 'New York'}
# print(my_dict['name'])  # Output: Alice

# -Invalid Keys (Mutable Objects):
# Lists: Lists are mutable, meaning their content can change. Trying to use a list as a 
# key will result in a TypeError.
# my_dict = {[1, 2, 3]: 'numbers'}  # Raises TypeError: unhashable type: 'list'

# Summary:
# Immutability of dictionary keys ensures the consistency and efficiency of hash-based lookups.
# Keys need to remain unchanged after being added to the dictionary, as any changes would affect 
# the key's hash value and lead to errors during retrieval.
# Valid dictionary keys include immutable types like strings, numbers, and tuples (with immutable elements).
# Invalid keys include mutable types like lists and dictionaries.
