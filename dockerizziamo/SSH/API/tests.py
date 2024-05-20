import hashlib
import base64

def verify_password(stored_password, provided_password):
    try:
        # Split the stored password to extract components
        algorithm, iterations, salt, stored_hash = stored_password.split('$')
        
        # Ensure iterations is an integer
        iterations = int(iterations)
        
        # Hash the provided password with the extracted salt and iterations
        dk = hashlib.pbkdf2_hmac(
            'sha256',  # PBKDF2 with SHA256
            provided_password.encode(),  # encode the provided password to bytes
            salt.encode(),  # encode the salt to bytes
            iterations  # use the iteration count
        )
        
        # Convert the generated hash to a base64 encoded string for comparison
        provided_hash = base64.b64encode(dk).decode('ascii')
        
        # Compare the provided hash with the stored hash
        return provided_hash == stored_hash
    except Exception as e:
        print(f"Error: {e}")
        return False

# Example usage
stored_password = "pbkdf2_sha256$720000$wuvNJrUVoGU0l0kg2Zq9T1$ea32j/1fA20d/y2m1dVw1REDN3ebrVqnlbOlfsxZZ78="
provided_password = "admin"
result = verify_password(stored_password, provided_password)

print("Password match:", result)