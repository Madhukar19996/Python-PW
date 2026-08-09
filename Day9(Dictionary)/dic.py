## Dictionaries are used to store data values in key:value pairs.
# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
# Dictionary items are ordered, changeable(mutable), and do not allow duplicates.
# Dictionary items are presented in key:value pairs, and can be referred to by using the key name.
#  { }

#1. creating a dictionary

#Approach 1:
# mydic1={"brand":"ford","model":"Aspire","year":2024}
#
# mydic2={
#      "brand":"ford",
#      "model":"Aspire",
#      "year":2024
#      }
# print(mydic1) #{'brand': 'ford', 'model': 'Aspire', 'year': 2024}
# print(mydic2)  #{'brand': 'ford', 'model': 'Aspire', 'year': 2024}


#Approach 2: using dict() constructor
# mydic=dict(name="Madhukar",age=27,country="India")
# print(mydic) #{'name': 'Madhukar', 'age': 27, 'country': 'India'}

#a key can have multiple values
# mydic={
#
#      "brand":"ford",
#      "model":"Aspire",
#      "year":2024,
#      "colors":["red","white","blue"]
# }
# print(mydic) #{'brand': 'ford', 'model': 'Aspire', 'year': 2024, 'colors': ['red', 'white', 'blue']}


##Access items/values from dict
#You  can access the items of a dictionary by referring to its key name , inside [] brackets.
#Approach 1 :
# mydic1={"brand":"ford","model":"Aspire","year":2024}
# print(mydic1["model"]) #Aspire

#Approach 2: using get() method
# mydic1={"brand":"ford","model":"Aspire","year":2024}
# print(mydic1.get("brand")) #ford

# 3 Get keys : keys() method will return a list of all the keys int the dictionary.
# mydic={"brand":"ford","model":"Aspire","year":2024}
# print(mydic.keys()) #dict_keys(['brand', 'model', 'year'])


# 4 Get values : values() method will return a list of all the keys int the dictionary.

# mydic={"brand":"ford","model":"Aspire","year":2024}
# print(mydic.values()) #dict_values(['ford', 'Aspire', 2024])


##5 Get items : items() method will return each item in a dictionary, as tuples ina list.
# mydic={"brand":"ford","model":"Aspire","year":2024}
# print(mydic.items()) #dict_items([('brand', 'ford'), ('model', 'Aspire'), ('year', 2024)])


#6 . check if key is exist( searching key in a dictionary)
# mydic={"brand":"ford","model":"Aspire","year":2024}
# if "model" in mydic:
#     print("existed")
# else:
#     print("not existed")

# 7. Adding values in a dictionary.
# mydic={"brand":"ford","model":"Aspire","year":2024}
# mydic["color"]="black"
# print(mydic) #{'brand': 'ford', 'model': 'Aspire', 'year': 2024, 'color': 'black'}

# 8. update values in a dictionary-- update() method
# mydic={"brand":"ford","model":"Aspire","year":2024}
# mydic["color"]="black"
# print("Before upadtion:",mydic) #{'brand': 'ford', 'model': 'Aspire', 'year': 2024, 'color': 'black'}
#
# mydic.update({"year":2025})
# mydic.update({"colors":"white"})
# print("After upadtion ",mydic) #After upadtion  {'brand': 'ford', 'model': 'Aspire', 'year': 2025, 'color': 'black', 'colors': 'white'}

# 9. Removing items from dictionary.
#Approach 1 : using pop()
# mydic={"brand":"ford","model":"Aspire","year":2024}
# mydic.pop("model")
# print("After removing",mydic) #After removing {'brand': 'ford', 'year': 2024}

#Approach 2 : using popitem()
#removes the last inserted item (in versions before 3.7, a random item is removed )
# mydic={"brand":"ford","model":"Aspire","year":2024}
# mydic.popitem()
# print("After removing",mydic) #After removing {'brand': 'ford', 'model': 'Aspire'}

#Appraoch 3: using del keyword - removes the item with the specified key name
# mydic={"brand":"ford","model":"Aspire","year":2024}
#del mydic["model"] # this will remove only model item
#print("After removing",mydic) #After removing {'brand': 'ford', 'year': 2024}
#del mydic
# print("After removing",mydic) #NameError: name 'mydic' is not defined --> This will delete dictionary completely.


#Appraoch 4: The clear() method clears the dictionary

# mydic={ "brand":"Ford", "model":"Aspire", "year" : 2024 }
# mydic.clear()
# print(mydic)  #{}

# 10. Copying the dictionary
#Appraoch 1: using copy()
# mydic1 = {"brand": "Ford", "model": "Aspire", "year": 2024}
# mydic2=mydic1.copy()
# print(mydic1) #{'brand': 'Ford', 'model': 'Aspire', 'year': 2024}
# print(mydic2) #{'brand': 'Ford', 'model': 'Aspire', 'year': 2024}

# Appraoch 2: using dict()--> built method in python
# mydic1={ "brand":"Ford", "model":"Aspire", "year" : 2024 }
# mydic2=dict(mydic1)
# print(mydic1) #{'brand': 'Ford', 'model': 'Aspire', 'year': 2024}
# print(mydic2) #{'brand': 'Ford', 'model': 'Aspire', 'year': 2024}


#11. length of dictionary
# mydic={ "brand":"Ford", "model":"Aspire", "year" : 2024 }
# print(len(mydic))  #3

#11. looping with dictionary
#Print all key names in the dictionary, one by one
#mydic={ "brand":"Ford", "model":"Aspire", "year" : 2024 }
# for i in mydic:
#     print(i)

# mydic={ "brand":"Ford", "model":"Aspire", "year" : 2024 }
# for i in mydic.keys():
#     print(i)

#Print all values in the dictionary, one by one

mydic={ "brand":"Ford", "model":"Aspire", "year" : 2024 }
# for i in mydic:
#     print(mydic[i])

# for i in mydic.values():
#     print(i)


# Print all the items from teh dictionary

for i,j in mydic.items():
    print(i,j)