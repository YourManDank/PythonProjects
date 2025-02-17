# Sorting a list permanently:
pets = ['dog','cat','horse','parrot']
print(pets)
pets.sort()
print(pets)
# pets.sort will sort a list alphabetically, once a list is sorted using this method it cannot be reverted

# Sorting in reverse alphabetical order:

towns = ['Maidstone','Ipswitch','Canterbury','Ashford','Gillingham','Rochester']
print(towns)
towns.sort(reverse=True)
print(towns)
# True must always be Capitalised otherwise python will not recognise it as boolean

# Temporarily sorting a list:
trees = ['Birch','Oak','Rose','Yew','Pine']
print('Here is the original list:')
print(trees)

print('\nHere is the sorted list:')
print(sorted(trees))

print('\nHere is the original list again:')
print(trees)

# Sort() will permanently sort, sorted(list_name)) will sort it temporarily
# The sorted() function will also accept a revser=True command