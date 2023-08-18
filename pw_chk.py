import re
def checking(passwrd):
    expression=r'^[a-zA-Z0-9,_]{8, }$'
    if re.match(expression,passwrd):
        return True
        
pass1="helowoaAld_20202"
if checking(pass1):
    print("Valid Password")
else:
    print('Invalid password')