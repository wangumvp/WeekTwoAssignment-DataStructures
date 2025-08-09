#empty list
my_list = []
#Append the elements 10, 20, 30, and 40 
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40) 
print("List after appending elements:", my_list) 
#insert the element 15 at index 2
my_list.insert(2, 15)
print("List after inserting 15 at index 2:", my_list)
my_list.append(50)
my_list.append(60)
my_list.append(70)
#remove the last element
my_list.remove(70)
my_list.sort()
print("Sorted list:", my_list)
#Find and print the index of the value 30
index_of_30 = my_list.index(30)
print("Index of 30:", index_of_30)
