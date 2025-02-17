# A tuple appears to be the same as a list except we use parenthesis instead of square brackets
# If we have a rectangle that should never change size then we can put its dimensions into a tuple rather than a bracket:

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# When we try to change one of the dimensions in the tuple:
dimensions[0] = 250
print(dimensions[0])
# Python responds with a Type error stating that a Tuple object does not support this type of item assignment