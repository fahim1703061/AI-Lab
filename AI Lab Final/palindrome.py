given = input("Enter a string to check if it is pallindrome: \n")
reversed_string = "".join(reversed(given))

if given == reversed_string:
    print("It's a pallindrome")
else:
    print("It's not a pallindrome")