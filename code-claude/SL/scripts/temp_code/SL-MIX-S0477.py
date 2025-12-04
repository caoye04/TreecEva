def calculate_score(password):
    # Calculate password strength based on various criteria
    base_score = 0
    length_score = min(len(password) * 4, 40)
    
    # Track character types
    has_lowercase = False
    has_uppercase = False
    has_digit = False
    has_special = False
    
    # Count of each character type
    lowercase_count = 0
    uppercase_count = 0
    digit_count = 0
    special_count = 0
    
    # Check each character
    for char in password:
        if char.islower():
            lowercase_count += 1
            has_lowercase = True
        elif char.isupper():
            uppercase_count += 1
            has_uppercase = True
        elif char.isdigit():
            digit_count += 1
            has_digit = True
        else:
            special_count += 1
            has_special = True
    
    # Calculate bonus for character variety
    type_count = sum([has_lowercase, has_uppercase, has_digit, has_special])
    type_bonus = type_count * 10
    
    # Calculate deductions for repeated patterns
    repeated_chars = 0
    for i in range(1, len(password)):
        if password[i] == password[i-1]:
            repeated_chars += 1
    
    # This variable is not used in final calculation
    sequential_count = 0
    
    # Apply all modifiers
    final_score = base_score + length_score + type_bonus - repeated_chars * 3
    
    # Cap the score between 0 and 100
    return max(0, min(final_score, 100))

# Test with password
password = "P@ssw0rd"

# Calculate entropy (not used in final result)
char_set_size = 94  # printable ASCII characters
possible_combinations = char_set_size ** len(password)
entropy = possible_combinations / 1000000

# Calculate score
password_strength = calculate_score(password)

# Apply additional rules (these don't affect the final result)
common_passwords = {"password", "123456", "qwerty"}
if password.lower() in common_passwords:
    penalty_factor = 0.5
else:
    penalty_factor = 1.0

# Print the result
print(f"Result: {password_strength}")