# The range() function:
for value in range(1,5):
    print(value)

# The range function is one of python's off-by-one functions, and in this case the for loop begins counting at the first specified value
# and stops counting at the second; in this case 5. This range will therefore count 1,2,3,4 but not 5.

# So if we want to print the range 1-5:

for values in range(1,6):
    print(values)

# We can also convert a range into a list:
numbers = list(range(1,6))
print(numbers)

# We can also tell python to skip numbers in a given range:
even_numbers = list(range(2, 11, 2))
print(even_numbers)

# We can create a range of technically any numbers we want, EG; square numbers:

squares = []
for value in range (1,11):
    square = value **2
    squares.append(square)

print(squares)

# Finding the min, max and sum of a list:
# >>> digits = [1, 2, 3, 4, 5 ,6 ,7 ,8 ,9, 0]
# min(digits) = 0
# max(digits) = 9
# sum(digits = 45)
