import secrets, string
def generate_password(ensure_complexity=True):
    if length < 4:
        raise ValueError(" At least 4 characters long")
    
    alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    while True:
        pwd = ''.join(secrets.choice(alphabet) for _ in range(length))
        if not ensure_complexity:
            return pwd
        
        if (any(c.islower() for c in pwd)
            and any(c.isupper() for c in pwd)
            and any(c.isdigit() for c in pwd)
            and any(c in string.punctuation for c in pwd)):
            return pwd

if __name__ == "__main__":
    try:
        length = int(input("Enter password length (≥ 4): "))
        pwd = generate_password(length)
        print("Password:", pwd)
    except ValueError as e:
        print("Error:", e)

    
