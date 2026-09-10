import bcrypt

# Hashes and salts a given password using bcrypt and returns the hashed password as a string. 

def hash_password(password: str) -> str:
    password_bytes = password.encode("utf-8")

    hashed_password = bcrypt.hashpw(
        password_bytes,
        bcrypt.gensalt(),
    )

    return hashed_password.decode("utf-8")

# Verifies input password against the stored hashed password using bcrypt, returning True if they match, otherwise False.

def verify_password(
    password: str,
    password_hash: str,
) -> bool:
    password_bytes = password.encode("utf-8")
    hashed_password_bytes = password_hash.encode("utf-8")

    return bcrypt.checkpw(
        password_bytes,
        hashed_password_bytes,
    )