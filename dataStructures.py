""" 
Lists: 
In Python, every item in a list can be of a different type.
Lists are mutable, meaning they can be changed after they are created.
We can use the list(iterable) function to create a list object
 """


# Packing/Unpacking: -------------------------------------------------------------------------------------------------------------------------------------------------
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
print(first, sedond, third, other)


# Lambda Functions: -------------------------------------------------------------------------------------------------------------------------------------------------
# A simple one line anonymous function that we can pass to other functions.
# Lambda functions follow this syntax: lamnda parameters: expression

items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]

# We can use lambda to sort a list of complex objects
# sort takes a key argument that is a function that is called on each item in the list to determine the sorting criteria.
items.sort(key=lambda item: item[1])

# We can also use lambda to map a list of complex objects
# map takes two arguments, a function and one or more iterables. We can pass a function and the list of items. Map will iterate over the iterables that we pass and
# will call the lambda function on each parameter of the list. map() will return a map object, which is an iterable, so we can pass it to the list() function

pricesLambda = list(map(lambda item: item[1], items))

print(pricesLambda)  # [10, 9, 12]
