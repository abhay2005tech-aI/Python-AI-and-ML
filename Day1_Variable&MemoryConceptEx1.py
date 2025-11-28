name = "John"
age1 = 30
age2 = 890
print("Name:", name)
print("Age1:", age1)
print("Age2:", age2)
is_active = True    
print(name, age1, age2, is_active)
print(type(name), type(age1), type(age2), type(is_active))
age2 = age1
print(age2)
print(id(name), id(age1), id(age2), id(is_active))
print(id(name) == id(age1))
print(id(age1) == id(age2))
