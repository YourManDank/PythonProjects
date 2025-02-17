# It is possible to slice a for loop if we want to loop a subset of the list:
players = ['Charlie','James','Clarence','Tommy','Jack']
print("Here are the first three players on the team:")
for player in players[:3]:
    print(player.title())

# Slicing lists has a wide number of applications. For example we can use it to categorise a much large dataset into smaller sub-sets
# which will allows us to generate useful information when we search and pull data based on the categories we have created