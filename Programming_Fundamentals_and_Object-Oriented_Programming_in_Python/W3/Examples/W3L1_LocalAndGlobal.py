x = 10 # global variable

def func():
    global x
    x = 5 # local variable 
    print("Local x:", x)

func()
print("Global x:", x)

