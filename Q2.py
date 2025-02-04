full_name = input("Enter your full name: ").strip()
names = full_name.split()
if len(names) >= 2:
    initials = names[0][0].upper() + "." + names [-1][0].upper()
    print(f"Your initials are: {initials}")
else:
    print(f"Please enter both your first anme and lastname.")
    