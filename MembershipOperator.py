math = 90
english = 95
total = math + english
avg = int(total / 2)
validRange = range(0, 101)
if (avg not in validRange):
    print("Invalid input.")
elif (avg in range(91, 101)):
    print("Grade: A1")
else:
    print("Try harder next time.")