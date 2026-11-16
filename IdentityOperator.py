x = 20
y = x
if(x is y):
    print("x and y have the same identity.")

x = 20
y = 30
if(x is y):
    print("x and y have the same identity.")
if(x is not y):
    print("x and y do not have the same identity.")

x = 5
if(type(x) is int):
    print("x is an integer.")