import re
x = r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+_-]+\.[a-zA-Z]{2,}$"
email = "john.doe@example.com"
match = re.match(x, email)

if match:
    print("The email address is valid.")
else:
    print("The email address is invalid.")