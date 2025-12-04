# Function to calculate valid password combinations based on specific rules

def is_valid(password):
    # Check if password meets security criteria
    has_uppercase = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    return has_uppercase and has_digit and len(password) >= 5

# Available character sets
uppercase_letters = 'AB'
lowercase_letters = 'xy'
digits = '12'

# Generate all possible combinations of 5 characters
possible_combinations = []
for a in uppercase_letters + lowercase_letters + digits:
    for b in uppercase_letters + lowercase_letters + digits:
        for c in uppercase_letters + lowercase_letters + digits:
            for d in uppercase_letters + lowercase_letters + digits:
                for e in uppercase_letters + lowercase_letters + digits:
                    possible_combinations.append(a + b + c + d + e)

# Count how many combinations satisfy the validation rules
valid_combinations = len([p for p in possible_combinations if is_valid(p)])

# Display the result
print(f"Result: {valid_combinations}")