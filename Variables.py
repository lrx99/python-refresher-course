#Variables
# Strings
first_Name = "John"
last_Name = "Lim"
full_Name = first_Name + last_Name
print("My name is :" + full_Name)
print(type(full_Name))

#Integers
age = 22
age += 1 #Age added by 1
#print("My age is :" + age) -> Result in error due to diff var types
print("My age is :" + str(age))
print(type(age))

#Floats
height = 170.1
print("My height is :" + str(height) + "cm")
print(type(height))

#Boolean
human = True
print("Are You a human :" + str(human))
print(type(human))