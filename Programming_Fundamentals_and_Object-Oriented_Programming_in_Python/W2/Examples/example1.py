# Print statement:
print("h",end=" ")
print("Hello world!")

# Variables
# int - integer
# float
# char, string
x = int("5")
y = x + 1
a = y % x
z = float(7.6)
# String concatination
year = 2025
st = str(f"The year is: {year} m")
st = str("The year is: {} m".format(year))
st = str("The year is: " + str(year) + " m")
st = str("The year is: %s m %s" % (year, z))

print(x)
print(y)
print(z)
print(st)

# Read from user
x = input("Enter a number: ")
print(x)
