import random
import string

# Step 1: Ask user for desired password length
p_length = int(input("Enter desired password length: "))

# Step 2: Define the possible characters for the password
P_char = string.ascii_letters + string.digits + string.punctuation
# ascii_letters → A–Z and a–z
# digits → 0–9
# punctuation → special symbols like !@#$%^&*

# Step 3: Generate the password
p_word = ''.join(random.choice(P_char) for _ in range(p_length))

# Step 4: Display the generated password
print("\nGenerated Password:", p_word)
