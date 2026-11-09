# ================================
# SCHOOL CLUB MEMBER BADGE
# ================================

# ---------- PART 1: member details ----------
# YOUR CODE HERE
# Ask for the member name and the club name with input().
# Save each answer in its own variable.
MemberName = input("Enter member name: ")
ClubName = input("Enter club name: ")

# ---------- PART 2: data types ----------
# YOUR CODE HERE
# Make member_number = 8, points = 9.5 and is_active = True.
# Print each one with its data type, using type().
member_number = 8
points = 9.5
is_active = True

print(f"Member Number: {member_number} (Type: {type(member_number)})")
print(f"Points: {points} (Type: {type(points)})")
print(f"Is Active: {is_active} (Type: {type(is_active)})")

# ---------- PART 3: badge code ----------
# YOUR CODE HERE
# Join: the first 3 letters of the name,
#       the last letter of the club,
#       and the member number turned into text.
# Save it in badge_code and print it.
badge_code = MemberName[:3] + ClubName[-1] + str(member_number)
print(f"Badge Code: {badge_code}")

# ---------- PART 4: final badge ----------
print("===== CLUB BADGE =====")
# YOUR CODE HERE
# Print four lines: Member, Club, Code and Points | Active.
# Join the words and the values with +.
print("Member: " + MemberName)
print("Club: " + ClubName)
print("Code: " + badge_code)
print("Points | Active: " + str(points) + " | " + str(is_active))
print("========================")