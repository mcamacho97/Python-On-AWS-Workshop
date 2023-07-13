# String refers to anything inside quotes
"The quick brown fox jumped over the lazy dog"
'The quick brown fox jumped over the lazy dog'

# Include a direct quote in a string
'The error message was "Incorrect Data Type"'

# Include a double quote in a string
"The error message was \"Incorrect Data Type\""

# String can be assigned to a variable
first_name = "Mauricio"
last_name = "Camacho"

# Concatenation
print(first_name + " " + last_name)

# Variables in Strings

# .format()
print("My first name is {} and my last name is {}".format(first_name, last_name))

# f string
print(f"My first name is {first_name} and my last name is {last_name}")

# New Lines and Indentation
# \n = new line
# \t = tab

string = "This is a string over\nthree lines \n\twith the third line idented"

# This is a string over
# three lines
#         with the third line indented


# Numbers
my_int = 50
sentence = "The total comes to: "
print(sentence + str(my_int))

#str() returns a string object
#int() returns an integer object
#float() returns a float object
#bool() returns a boolean object


# Dictionaries
user = {"first_name": "Ada"}
print(user) # Prints the value of user
print(user["first_name"]) # Prints the value of the key "first_name"
user["family_name"] = "Byron" # Adds a new key "family_name" with the value "Byron"
user["family_name"] = "Lovelace" # Update "family_name" with the value "Lovelace"
del user["family_name"] # Delete the key "family_name"


# Lists
# [0,1,2,3] is a number list
# [ "a", "b", "c"] is a string list
# [{"key": "value"}, {"key": "value"}] is a dictionary list

# Create
fruit = ["apple", "banana", "cherry"] # The first index is 0 
print(fruit[1]) # Prints the value of banana
len(fruit) # Prints the length of the list

# Update
fruit.append("kiwi") # Adds a new element to the end of the list
fruit.insert(2, "orange") # Adds a new element to the specified index

# Organizing a list
fruit.sort() # Sorts the list
fruit.reverse() # Reverses the list

# Delete
del fruit[1]
favorite_fruit = fruit.pop() # Removes the last element of the list
fresh_fruit = fruit.pop(1) # Removes the element at the specified index
fruit.remove('bananas') # Removes the specified element


# Determining Type
MY_VARIABLE = "A string"
print(type(MY_VARIABLE)) # <class 'str'>
