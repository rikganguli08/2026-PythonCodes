day = input("what is the day?: ")
hw_complete = input("is your homework complete? (yes/no): ")

if hw_complete == "yes":
    #print("Great! You can relax and enjoy your day.")
    hw_complete = True
else:
    #print("You should complete your homework first.")
    hw_complete = False

print("========== SMART DAY PLANNER ============")
# OR operator
if day == "Saturday" or day == "Sunday":
    print("Day: weekend - time to relax and enjoy your day!")
    print("Morning: No school today!")
else:
    print("Day: weekday - time to focus on your studies.")
    print("Morning: School time!")

# NOT operator
if hw_complete:
    print("Evening: You can relax and enjoy your evening!")
if not hw_complete:
    print("Evening: Finish your hw in time!")

# AND operator
if day == "Sunday" and hw_complete:
    print("Fun activity: Time to watch a movie!")
print("================================")