password = input("Enter your password: ")

# password_length = len(pass)

if len(password)<6 :
    strength = "Password too weak"
elif len(password)<=10:
    strength = "Password too medium"
else: 
    strength ="Password strong"
    
print("Password strength: ", strength)