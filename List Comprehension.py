# List comprehension allows us to create a new list using items that exist in a previous list
squares = [value **2 for value in range(1,11)]
print(squares)

# In this example we create our expression that multiplies the given range (1,11) by the second power (**2); generating the square numbers of each value in the range

# Slicing a List
# In order to slice a list we need to specify the first and last elements that we want to work with:

players = ['Charlie','Martin','Florence','Isaac','Matthew']
print(players[0:3])

# Python stops one item before the second index, meaning that a range of 0:3 will give items 0, 1 and 2.

# We can generate a slice from a list ay any point within it:
seasons = ['Spring','Summer','Autumn','Winter']
print(seasons[2:4])
# Will print Autumn and Winter.

# If you do not include the first item then Python will automatically index from the beginning of the list:
trees = ['Oak','Yew','Birch','Beech','Sand','Rose']
print(trees[:3])

# A similar thing happens if you slice without specifying the second index:
cats = ['Tabby','Persian','Burmese','Siamese']
print(cats[2:])
# This method of not indexing either the first or second item allows us to split a list in two at the given index point.

