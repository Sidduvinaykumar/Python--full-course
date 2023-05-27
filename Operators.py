
# """ Arithmetic operators are used to perform mathematical calculations in programming """
# # Addition
# a = 10
# b = 5
# result = a + b
# print("Addition:", result)

# Subtraction
# result = a - b
# print("Subtraction:", result)

# # Multiplication
# result = a * b
# print("Multiplication:", result)

# # Division
# result = a / b
# print("Division:", result)

# # Floor Division (returns the quotient without the remainder)
# result = a // b
# print("Floor Division:", result)

# # Modulus (returns the remainder)
# result = a % b
# print("Modulus:", result)

# # Exponentiation
# result = a ** b
# print("Exponentiation:", result)

# """ Relational operators are used to compare values or variables in programming. 
# They return a Boolean value (True or False) based on the comparison result. """
# # Comparison or Relatnol 
# a = 10
# b = 5

# # Equal to
# result = a == b
# print("Equal to:", result)

# # Not equal to
# result = a != b
# print("Not equal to:", result)

# # Greater than
# result = a > b
# print("Greater than:", result)

# # Less than
# result = a < b
# print("Less than:", result)

# # Greater than or equal to
# result = a >= b
# print("Greater than or equal to:", result)

# # Less than or equal to
# result = a <= b
# print("Less than or equal to:", result)



# """ Logical operators are used to combine and manipulate Boolean values in programming.
# They allow you to perform logical operations such as AND, OR, and NOT """


# a = True
# b = False

# # Logical AND
# result = a and b
# print("Logical AND:", result)

# # Logical OR
# result = a or b
# print("Logical OR:", result)

# # Logical NOT
# result = not a
# print("Logical NOT:", result)

# """ Assignment operators are used to assign values to variables in programming. 
# They combine the assignment operation with another operation, such as addition, subtraction, multiplication, etc """


# a = 10
# b = 5

# # Addition assignment
# a += b  # equivalent to a = a + b
# print("Addition assignment:", a)

# # Subtraction assignment
# a = 10
# b = 5

# a -= b  # equivalent to a = a - b
# print("Subtraction assignment:", a)

# # Multiplication assignment
# a = 10
# b = 5

# a *= b  # equivalent to a = a * b
# print("Multiplication assignment:", a)

# # Division assignment
# a = 10
# b = 5

# a /= b  # equivalent to a = a / b
# print("Division assignment:", a)

# # Modulus assignment
# a = 10
# b = 5

# a %= b  # equivalent to a = a % b
# print("Modulus assignment:", a)

# # Exponentiation assignment
# a = 10
# b = 2

# a **= b  # equivalent to a = a ** b
# print("Exponentiation assignment:", a)


# """ Membership operators are used to test whether a value or variable is a member of a sequence,
# such as a string, list, or tuple. In Python, the membership operators are in and not in.  """

# # Membership operators with lists
# fruits = ['apple', 'banana', 'orange']

# # Check if 'apple' is present in the list
# result = 'apple' in fruits
# print("'apple' in fruits:", result)

# # Check if 'grape' is not present in the list
# result = 'grape' not in fruits
# print("'grape' not in fruits:", result)

# # Membership operators with strings
# message = 'Hello, world!'

# # Check if 'world' is present in the string
# result = 'world' in message
# print("'world' in message:", result)

# # Check if 'Python' is not present in the string
# result = 'Python' not in message
# print("'Python' not in message:", result)

# """ Identity operators are used to compare the identity of objects in Python.
# They check if two objects refer to the same memory location. In Python, the identity operators are is and is not. """

# # Identity operators with integers
# a = 10
# b = 10
# c = 5

# # Check if 'a' and 'b' refer to the same object
# result = a is b
# print("a is b:", result)

# # Check if 'a' and 'c' refer to the same object
# result = a is c
# print("a is c:", result)

# # Check if 'a' and 'b' refer to different objects
# result = a is not b
# print("a is not b:", result)

# # Identity operators with lists
# list1 = [1, 2, 3]
# list2 = list1
# list3 = [1, 2, 3]

# # Check if 'list1' and 'list2' refer to the same object
# result = list1 is list2
# print("list1 is list2:", result)

# # Check if 'list1' and 'list3' refer to different objects
# result = list1 is not list3
# print("list1 is not list3:", result)


# """ Bitwise operators are used to perform operations on individual bits of binary numbers.
# They are useful when working with low-level data manipulation or certain bitwise operations.  """

# # Bitwise AND
# a = 10  # 1010
# b = 5   # 0101

# result = a & b
# print("Bitwise AND:", result)  # Output: 0

# # Bitwise OR
# result = a | b
# print("Bitwise OR:", result)   # Output: 15

# # Bitwise XOR
# result = a ^ b
# print("Bitwise XOR:", result)  # Output: 15

# # Bitwise NOT
# result = ~a
# print("Bitwise NOT:", result)  # Output: -11

# # Bitwise Left Shift
# result = a << 1
# print("Bitwise Left Shift:", result)  # Output: 20

# # Bitwise Right Shift
# result = a >> 1
# print("Bitwise Right Shift:", result)  # Output: 5
