my_list = []

# append 10, 20, 30, and 40 to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# insert 15 at the second position
my_list.insert(1, 15)

# extend the list with [50, 60, 70]
my_list.extend([50, 60, 70])

# remove the last element from the list
my_list.pop()

# sort the list in ascending order
my_list.sort()

# find and print the index of the element 30
index_of_30 = my_list.index(30)
print(index_of_30)
