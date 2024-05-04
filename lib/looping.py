#!/usr/bin/env python3
# the pass statement is a null operation that does nothing.pleaceholder for the code that will be implemented later.
def happy_new_year():
 # prints 10 to 1 countdown then "Happy New Year!"
    i = 10
    while i >= 1:
        print(i)
        i -= 1
    print("Happy New Year!")


happy_new_year()


def square_integers(int_list):
    # Use list comprehension to square each element and return the list of squares
    return [element * element for element in int_list]

# Call the function with a list of integers
result = square_integers([1, 2, 3])
print(result)



def fizzbuzz():
    i = 1  # Start from 1
    while i <= 100:  # Loop from 1 to 100
        if i % 3 == 0 and i % 5 == 0:  # Check if the number is divisible by both 3 and 5
            print("FizzBuzz")
        elif i % 3 == 0:  # Check if the number is divisible by 3
            print("Fizz")
        elif i % 5 == 0:  # Check if the number is divisible by 5
            print("Buzz")
        else:
            print(i)
        i += 1  # Increment i by 1 in each iteration


# Call the function
fizzbuzz()
