# Immutable examples
int_value = 42
# int_value[0] = 5 # TypeError: 'int' object does not support item assignment
float_value = 3.14
# float_value[0] = 1 # TypeError: 'float' object does not support item assignment
name = "Fido"
print(name[0]) # Output: 'F'
# name[0] = "R" # TypeError: 'str' object does not support item assignment
tuple_value = (1, 2, 3)
# tuple_value[0] = 100 # TypeError: 'tuple' object does not support item assignment

# Mutable examples
#    Keys   0       1
tricks = ["sit", "roll"]
tricks.append("stay")
tricks[0] = "GSG"
print(tricks) # Output: ['sit', 'roll', 'stay']

d = {0: "sit", 2: "roll"}
print(d[0])
d[0] = "hi"
print(d)

dog_info = {"name": "Buddy", "age": 5}
dog_info["breed"] = "Labrador"
print(dog_info) # Output: {'name': 'Buddy', 'age': 5, 'breed': 'Labrador'}

commands = {"sit", "stay"}
commands.add("roll")
print(commands) # Output: {'stay', 'sit', 'roll'} (order may vary)


l1 = [1,2,3,4,4]
l2 = [1,2,3,4,4]
l3 = [1,3,2,4,4]
print(l1 == l2)
print(l1 == l3)
print(l1)

s1 = {1,2,3,4,4}
s2 = {1,2,3,4,4}
s3 = {1,3,2,4,4}
print(s1 == s2)
print(s1 == s3)

print(s1)
print(set(l1))
