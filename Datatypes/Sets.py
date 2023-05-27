


# sirisha={33,12,345,46,3,56,75}
# print(sirisha[0])
# sirisha.add({1,2,3,4,5})
# sirisha.update({1,2,3,4,5})
# sirisha.remove(33)
# sirisha={1,2,3,5,6,78}
# sirisha.pop()
# print(sirisha)



# set1={1,2,3,4,4}
# set2={5,6,7,8,4}
# print(set1.union(set2))it combines both sets and gives result
# print(set1.intersection(set2))it shows only commen element of the each set
# set1={1,2,3,44}
# # set2={44,6,7,8}
# print(set1.difference(set2))it removes commen element from set 1 and give output to set one elements only 


# set1={1,2,3,44,5,4,1,2,4,5,6}
# set2={1,2,3,4,5}
# print(set2.issubset(set1)) it shows set2 elements must suld be in subset set1



# set1={6,7,8,9,10}
# set2={1,2,3,4,5}
# print(set1.isdisjoint(set2))both set are quite diffrent in  that time only give true


# set1={1,2,3,4,5}
# set2={4,5,6,7,6}
# print(set1.symmetric_difference(set2))it is quite opposite to the intersection


# Set Methods using strings datatypes

# Creating a set
fruits = {"apple", "banana", "orange"}

# Adding elements to a set
fruits.add("mango")
print("Set after adding 'mango':", fruits)

# Removing elements from a set
fruits.remove("banana")
print("Set after removing 'banana':", fruits)

# Checking if an element exists in a set
print("Is 'apple' in the set?", "apple" in fruits)

# Union of two sets
more_fruits = {"strawberry", "kiwi"}
all_fruits = fruits.union(more_fruits)
print("Union of sets:", all_fruits)

# Intersection of two sets
common_fruits = fruits.intersection(more_fruits)
print("Intersection of sets:", common_fruits)

# Difference between two sets
unique_fruits = fruits.difference(more_fruits)
print("Difference between sets:", unique_fruits)

# Checking if a set is a subset or superset of another set
subset = {"apple", "mango"}
print("Is subset?", subset.issubset(fruits))
print("Is superset?", fruits.issuperset(subset))

# Removing all elements from a set
fruits.clear()
print("Cleared set:", fruits)
