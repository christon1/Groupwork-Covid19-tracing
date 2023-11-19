import hashlib

# Hash the intended password
intended_password = "password"
hashed_intended_password = hashlib.sha256(intended_password.encode()).hexdigest()

print("Hashed intended password:", hashed_intended_password)
 