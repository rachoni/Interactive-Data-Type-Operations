# Interactive Data Type Operations System

# Prompt the user to choose a data type to perform operations on
print("Choose a data type to perform operations on:")
print("1. Strings")
print("2. Numbers")
print("3. Booleans")
print("4. Additional Data Types (List, Tuple, Dictionary)")

# Get the user's choice and store it in a variable
choice = input("Enter the number of your choice (1-4): ")

# If the user chooses Strings (choice == '1'):
if choice == '1':

    # Declare a string variable, e.g., sentence = "Learning Python is fun!"
    # Extract and print a substring, such as the word "Python" from the sentence.
    # Convert the entire sentence to uppercase and print it.
    # Replace a word in the sentence (e.g., replace "fun" with "awesome") and print the modified sentence.

    my_sentence = 'Learning Python is fun!'
    my_word = my_sentence[9:15]
    new_sentence = my_sentence.upper()
    replace_word = my_sentence.replace('fun', 'awesome')

    print(f'My sentence: {my_sentence}\nMy word: {my_word}\nUppercase sentence: {new_sentence}\nReplaced word: {replace_word}')

# If the user chooses Numbers (choice == '2'):
elif choice == '2':

    # Prompt the user to input two numbers, e.g., num1 and num2.
    # Perform and print the results of addition, subtraction, multiplication, and division.
    # Handle division by zero (e.g., print an error message if num2 is zero).
    # Perform a power operation, raising num1 to the power of num2, and print the result.

    first_number = int(input())
    second_number = int(input())

    result_addition = first_number + second_number
    result_subtraction = abs(first_number - second_number)
    result_multiplication = first_number * second_number
    result_power = first_number ** second_number

    if first_number != 0 and second_number != 0:
        result_division = first_number / second_number

        print(f'Result addition: {result_addition}\nResult subtraction: {result_subtraction}\nResult multiplication: {result_multiplication}\nResult division: {result_division}\nResult power: {result_power}')

    elif first_number == 0 or second_number == 0:

        print(f'Result addition: {result_addition}\nResult subtraction: {result_subtraction}\nResult multiplication: {result_multiplication}\nERROR: Cannot divide by zero!\nResult power: {result_power}')

# If the user chooses Booleans (choice == '3'):
elif choice == '3':

    # Declare two boolean variables, e.g., is_python_fun = True, is_sunny = False.
    # Perform and print the results of logical operations: AND, OR, NOT.
    # Perform and print the results of comparison operations (e.g., 10 > 5 and 5 == 5).

    is_right = True
    is_not_right = False

    number = 5
    min_value = 0
    max_value = 10

    if number > min_value and number < max_value:
        print(is_right)

    if max_value > number or min_value == number:
        print(is_right)

    for number in range(min_value, max_value + 1):
        if (not min_value != number) or (not max_value != number):
            print(is_not_right)
            break

# If the user chooses Additional Data Types (choice == '4'):
elif choice == '4':

    # ### List Operations ###
    # Create a list with mixed data types (e.g., numbers, strings, booleans).
    # Append a new element to the list and print the updated list.
    # Access and print the 4th element in the list.

    my_list = ['male', 34, True]
    my_list.append('banana')

    print(f'{my_list}\n{my_list[-1]}')
    print()

    # ### Tuple Operations ###
    # Create a tuple with some string elements (e.g., fruits).
    # Print the length of the tuple.
    # Try to modify one element in the tuple and handle the resulting TypeError.

    my_tuple = ('apple', 'banana', 'cherry')

    my_new_list = list(my_tuple)
    my_new_list.remove('cherry')
    my_new_list.append('orange')

    my_new_tuple = tuple(my_new_list)

    print(len(my_tuple))
    print(my_new_tuple)
    print()

    # ### Dictionary Operations ###
    # Create a dictionary with some key-value pairs (e.g., name, age, city).
    # Access and print the value for one of the keys (e.g., "age").
    # Add a new key-value pair to the dictionary and print the updated dictionary.

    my_dictionary = {
        'brand': 'Ferrari',
        'model': 'Testarossa',
        'year': 1991
    }

    item_of_my_dictionary = my_dictionary['brand']

    my_dictionary.update({'color': 'red'})

    print(f'{item_of_my_dictionary}\n{my_dictionary}')

# If the user enters an invalid choice:
else:

    # Print an error message indicating an invalid selection.

    print('ERROR: Invalid selection!')