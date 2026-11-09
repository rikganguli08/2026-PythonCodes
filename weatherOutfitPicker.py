temperature = int(input("Enter the temperature: "))
print("Temperature is:", temperature)
if temperature < 25:
    outfit = "jacket"
    print("it is a cold day")
    print("You should wear a", outfit)
else:
    outfit = "t-shirt"
    print("it is a hot day")
    print("You should wear a", outfit)

is_raining = input("Is it raining? (yes/no): ")
if is_raining == "yes":
    print("You should also bring an umbrella.")

print("====WEATHER OUTFIT PICKER====")
print("Temperature:", temperature)
print("Outfit:", outfit)
print("carry an umbrella:", is_raining)
print("===================================")