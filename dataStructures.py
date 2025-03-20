""" 
? Lists: 
In Python, every item in a list can be of a different type.
Lists are mutable, meaning they can be changed after they are created.
We can use the list(iterable) function to create a list object
 """


# ?Packing/Unpacking: -------------------------------------------------------------------------------------------------------------------------------------------------
# Packing: We can pack multiple values into a single variable
# Unpacking: We can unpack multiple values into multiple variables
# This technique only works if the number of variables on the left side of the assignment operator matches the number of elements in the list on the right side.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Boring way:
first = numbers[0]
second = numbers[1]
third = numbers[2]

# Unpacking the first three items into the first, second and third variabels. Packing the rest into the other variable:
first, sedond, third, *other = numbers


# ?Lambda Functions: -------------------------------------------------------------------------------------------------------------------------------------------------
# A simple one line anonymous function that we can pass to other functions.
# Lambda functions follow this syntax: lamnda parameters: expression

items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]

# Sorting:
# sort takes a key argument that is a function that is called on each item in the list to determine the sorting criteria.
items.sort(key=lambda item: item[1])

# Mapping:
# map takes two arguments, a function and one or more iterables. We can pass a function and the list of items. Map will iterate over the iterables that we pass and
# will call the lambda function on each parameter of the list. map() will return a map object, which is an iterable, so we can pass it to the list() function
pricesLambda = list(map(lambda item: item[1], items))


# Filtering:
# filter takes a function and an iterable. It will return an iterable with the items that the function returns True for.
# We can then pass this iterable to the list() function to get a list of the items that passed the filter.
filtered = list(filter(lambda item: item[1] >= 10, items))

# ?List Comprehensions (preferred by the communityu):----------------------------------------------------------------------------------------------------------------------------
# A shorter syntax when you want to create a new list by performing an operation on each item in an existing list.
# Syntax: [expression for item in iterable if optional condition]

# Mapping:
prices = [item[1] for item in items]

# Filtering:
filtered = [item for item in items if item[1] >= 10]

# ?Zip Function: -------------------------------------------------------------------------------------------------------------------------------------------------
# The zip function is used to combine two or more lists into a single list.
# It takes two or more iterables and returns a zip object that is an iterator of tuples.
# We cannot use comprehension for this operation because comprehension only works with a single list.

list1 = [1, 2, 3]
list2 = [10, 20, 30]
combine = list(zip('abc', list1, list2))

# ?Sets: -------------------------------------------------------------------------------------------------------------------------------------------------
# Sets are collections of unique items. They are unordered and unindexed.
numbers = [1, 1, 2, 2, 3, 4, 5, 1, 2]
first = set(numbers)
second = {1, 5, 6}
# Union: Returns a new set with all the unique items from both sets.
union = first | second

# Intersection: Returns a new set with all the items that are present in both sets.
intersection = first & second

# Difference: Returns a new set with all the items from the first set that are not in the second set.
difference = first - second

# Symmetric Difference: Returns a new set with all the items that are in one set but not in both.
symmetric_difference = first ^ second

# Validate the existence of an item in a set:
if 1 in first:
    print('yes')

# ?Dictionaries: -------------------------------------------------------------------------------------------------------------------------------------------------
# Dictionaries are collections of key-value pairs. They are unordered, changeable and indexed.
# We can only use immutable types for the keys of a dictionary. This means we can use strings, numbers or tuples as dictionary keys.

dictionary = dict(name='John', age=30)
dictionary = {
    'name': 'John',
    'age': 30
}

# Accessing Items:
value = dictionary['name']
value2 = dictionary.get('name')
unexistingValue = dictionary.get('unexistingKey', 'default value')

# Updating Items:
dictionary['name'] = 'Jane'
dictionary.update({'name': 'Jane', 'age': 32})

# Iterating over a dictionary:
for key in dictionary:
    print(key, dictionary[key])

# We can use the items() method to unpack the key-value pairs in a dictionary and then iterate over them
for key, value in dictionary.items():
    print(key, value)

# Removing items:
del dictionary['name']
dictionary.pop('age')

# ?Dictionary Comprehensions: -------------------------------------------------------------------------------------------------------------------------------------------------
# A shorter syntax when you want to create a new dictionary by performing an operation on each item in an existing dictionary.
dictionary = {}
for x in range(5):
    dictionary[x] = x * 2

dictionary_comprehension = {x: x * 2 for x in range(5)}

# ?Generator Expressions: -------------------------------------------------------------------------------------------------------------------------------------------------
# Generator expressions are handy when dealing with a really large data set. 
# Generators are iterable, so we can iterate over them and in each iteration we generate a new value.
# Unlike lists, generators don't store all the values in memory, they generate the values on the fly.
# We can create a generator expression by using parentheses instead of square brackets in the Commprehension expression

values = (x * 2 for x in range(10))
for x in values:
    print(x)
# ? Unpacking: -------------------------------------------------------------------------------------------------------------------------------------------------
first = [1, 2, 3]
second = [4, 5, 6]
values = [*first, *second]
print(values)