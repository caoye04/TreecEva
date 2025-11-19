password = "SecurePass2024"

# Step 1: Count character types
uppercase_count = sum(1 for c in password if c.isupper())
lowercase_count = sum(1 for c in password if c.islower())
digit_count = sum(1 for c in password if c.isdigit())

# Step 2: Calculate base score with weights
base_score = uppercase_count * 3 + lowercase_count * 2 + digit_count * 4

# Step 3: Check for common patterns and apply penalty
has_consecutive = False
for i in range(len(password) - 1):
    if ord(password[i+1]) - ord(password[i]) == 1:
        has_consecutive = True
        break

penalty = 5 if has_consecutive else 0
adjusted_score = base_score - penalty

# Step 4: Encode strength using bitwise operations
strength_level = adjusted_score // 10
strength_code = (strength_level << 2) | (digit_count & 0x3)

print(f"Result: {strength_code}")