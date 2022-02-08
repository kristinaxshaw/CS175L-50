#restaurant.py
#Kristina Shaw
#CS-175L

#declaring variables as False
vegetarian = False
vegan = False
gluten_free = False

#gathering input from user
response1 = input("Is anyone in your party a vegetarian?")
if response1 == "yes":
    vegetarian = True
elif response1 == "no":
    vegetarian = False

response2 = input("Is anyone in your party a vegan?")
if response2 == "yes":
    vegan = True
elif response2 == "no":
    vegan = False

response3 = input("Is anyone in your party gluten free?")
if response3 == "yes":
    gluten_free = True
elif response3 == "no":
    gluten_free = False

#displaying results
print("Here are your restaurant options: ")

if vegetarian == False and vegan == False and gluten_free == False:
    print("Joe's Gourmet Burgers")
    print("Mama's Fine Italian")
    print("Corner Cafe")
    print("The Chef's Kitchen")
    print("Main Street Pizza")
elif vegan == False and gluten_free == False:
    print("Mama's Fine Italian")
    print("Main Street Pizza")
    print("Corner Cafe")
    print("The Chef's Kitchen")
elif vegan == False:
    print("Main Street Pizza")
    print("Corner Cafe")
    print("The Chef's Kitchen")
else:
    print("Corner Cafe")
    print("The Chef's Kitchen")
