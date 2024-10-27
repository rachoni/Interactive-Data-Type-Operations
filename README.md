# Interactive Data Type Operations System

## Overview
The Interactive Data Type Operations System is a Python program that allows users to explore and perform various operations on different data types. Users can select from a list of data types, including Strings, Numbers, Booleans, and Additional Data Types (Lists, Tuples, and Dictionaries), and execute predefined operations for each. This interactive program is designed to help users learn basic operations and functions on commonly used Python data types.

## How It Works
The program prompts the user to select a data type by entering a number corresponding to each data type. Depending on the user’s choice, the program performs a set of operations and displays the results.

## Data Types and Operations

### 1. Strings
If the user selects **Strings**:
- **Substring Extraction**: Extracts and prints a substring from a sentence.
- **Uppercase Conversion**: Converts the entire sentence to uppercase.
- **Word Replacement**: Replaces a specific word in the sentence.

### 2. Numbers
If the user selects **Numbers**:
- Prompts the user to enter two numbers.
- **Arithmetic Operations**: Performs addition, subtraction, multiplication, and division (with zero-division error handling).
- **Power Operation**: Raises the first number to the power of the second.

### 3. Booleans
If the user selects **Booleans**:
- Declares two boolean variables.
- **Logical Operations**: Executes AND, OR, and NOT operations.
- **Comparison Operations**: Performs comparison operations and displays the results.

### 4. Additional Data Types
If the user selects **Additional Data Types**:
- **List Operations**: Creates a list, appends an element, and accesses an element by index.
- **Tuple Operations**: Creates a tuple, attempts modification (demonstrating immutability), and calculates the tuple length.
- **Dictionary Operations**: Creates a dictionary, accesses a value, and adds a new key-value pair.

## Code Example

```python
# Prompt the user to choose a data type
choice = input("Choose a data type to perform operations on (1-4): ")

if choice == '1':
    # String operations
    my_sentence = 'Learning Python is fun!'
    my_word = my_sentence[9:15]
    new_sentence = my_sentence.upper()
    replace_word = my_sentence.replace('fun', 'awesome')
    print(f'My sentence: {my_sentence}\nMy word: {my_word}\nUppercase sentence: {new_sentence}\nReplaced word: {replace_word}')

elif choice == '2':
    # Number operations
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))
    result_addition = first_number + second_number
    result_subtraction = abs(first_number - second_number)
    result_multiplication = first_number * second_number
    result_power = first_number ** second_number
    if second_number != 0:
        result_division = first_number / second_number
        print(f'Result division: {result_division}')
    else:
        print("ERROR: Cannot divide by zero!")

elif choice == '3':
    # Boolean operations
    is_right = True
    is_not_right = False
    number, min_value, max_value = 5, 0, 10
    print(f"AND operation: {is_right and (number > min_value)}")
    print(f"OR operation: {is_right or (number == min_value)}")

elif choice == '4':
    # Additional data type operations
    my_list = ['male', 34, True]
    my_list.append('banana')
    print(f'List: {my_list}')
    my_tuple = ('apple', 'banana', 'cherry')
    print(f'Tuple length: {len(my_tuple)}')
    my_dictionary = {'brand': 'Ferrari', 'model': 'Testarossa', 'year': 1991}
    my_dictionary.update({'color': 'red'})
    print(f'Dictionary: {my_dictionary}')

else:
    print("ERROR: Invalid selection!")
