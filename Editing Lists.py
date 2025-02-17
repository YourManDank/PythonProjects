# Adding an item to the list; the simplest way is to append items to a list (add to end):
olympic_sports = ['Wrestling','Hurdles','Shot Put Throw','Gymnastics']
print(olympic_sports)
olympic_sports.append('Hammer Toss')
print(olympic_sports)

# Adding multiple items to a new list:
airliners = []
airliners.append('Ryan Air')
airliners.append('Easy Jet')
airliners.append('British Airways')
print(airliners)

# Inserting new elements into a list, we can insert an element into any part of a list using the index method we previously practiced:
capital_cities = ['London','Paris','Berlin','Washing D.C']
capital_cities.insert(0,'Rome')
print(capital_cities)

# Removing elements from a list:
precious_stones = ['Ruby','Sapphire','Diamond','Emerald']
print(precious_stones)
del precious_stones[3]
print(precious_stones)

# The pop() method; somethings we want to retain the value of an item after it is deleted; for example if you want to remove a name from
# a list of active members and transfer it to a list of inactive members. The term 'pop' insinuates 'popping' an item from the top of a stack
anatomy = ['Hands','Arms','Legs','Feet']
print(anatomy)
popped_anatomy = anatomy.pop()
print(anatomy)
print(popped_anatomy)

# To track the item that gets removed by popping:
most_recent_item = anatomy.pop()
print(f"the most recent item to be popped from the list is {most_recent_item.title()}")
# You can specify to pop from an indexed position using anatomy.pop(#)

# Sometimes you wont know the position of the item that you would like to remove, for this we can use the remove function:
seasons = ['Spring','Summer','Autumn','Winter']
print(seasons)
seasons.remove('Winter')
print(seasons)