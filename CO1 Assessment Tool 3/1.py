import re

def validate_email(email):
    pattern = r'^[A-Za-z][A-Za-z0-9._]*@[A-Za-z]+\.(com|org|edu|net|in)$'
    return "Valid Email" if re.fullmatch(pattern, email) else "Invalid Email"

def validate_password(password):
    pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%&!]).{8,}$'
    return "Strong Password" if re.fullmatch(pattern, password) else "Weak Password"

def validate_mobile(mobile):
    pattern = r'^[6-9]\d{9}$'
    return "Valid Mobile Number" if re.fullmatch(pattern, mobile) else "Invalid Mobile Number"

print("===== Intelligent Validator =====")

email = input("Enter Email: ")
password = input("Enter Password: ")
mobile = input("Enter Mobile Number: ")

print("\n----- Validation Result -----")
print(validate_email(email))
print(validate_password(password))
print(validate_mobile(mobile))