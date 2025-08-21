# Create a condition where a user is granted access only if both the username and password match predefined values. 
# Use logical operators to combine conditions:

# Start
# Set user to "GSG"
user = str("GSG")
# Set passwd to "123123"
passwd = "123123"
# Ask the user to enter the username
# Input username
username = input("Enter the username: ")
# Ask the user to enter the password
# Input password
password = input("Enter the password: ")
# If user == username and password == passwd then
if (username == user) and (password == passwd):
#   Display success
    print("Success!")
# Else
else:
#   Display username or password is wrong
    print("username or password is wrong!")
# End if
# end


# Start
# Set user to "GSG"
user = "GSG"
# Set passwd to "123123"
passwd = "123123"
# Ask the user to enter the username
# Input username
username = input("Enter the username: ")
# Ask the user to enter the password
# Input password
password = input("Enter the password: ")
# If user == username then
if username == user:
#   If password == passwd then
    if password == passwd:
#       Display success
        print("Success!")
#   else
    else:
#       Display password is wrong
        print("Password is wrong!")
#   end if
# Else
else:
#   Display username is wrong
    print("Username is wrong!")
# End if
# end
