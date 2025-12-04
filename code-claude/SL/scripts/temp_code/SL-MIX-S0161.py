def is_valid_password(password, min_length=8, has_special=True):
    special_chars = set('@#$%^&*!')
    if len(password) < min_length:
        return False
    if has_special and not any(char in special_chars for char in password):
        return False
    return True

# Password analysis for a security system
password_attempts = {
    'user1': ['abc123', 'password!', 'secure@123'],
    'user2': ['qwerty', 'admin@1', 'P@ssw0rd'],
    'user3': ['letmein', '123456', 'admin123$']
}

# Security levels dictionary
security_levels = {'low': 6, 'medium': 8, 'high': 10}

# Extract all passwords for analysis
all_passwords = []
for user, passwords in password_attempts.items():
    # Calculate user risk score (not used in final calculation)
    risk_score = 5 - len([p for p in passwords if is_valid_password(p)])
    # Add passwords to main list
    all_passwords.extend(passwords)

# Some statistics about password lengths (not directly used in answer)
total_length = sum(len(p) for p in all_passwords)
avg_length = total_length / len(all_passwords) if all_passwords else 0

# Find valid password combinations based on different security requirements
combos = []
for password in all_passwords:
    # Try different security configurations
    for level, length in security_levels.items():
        # Determine if special chars should be required based on level
        require_special = level != 'low'
        # Check if password is valid with these settings
        if is_valid_password(password, length, require_special):
            combos.append((password, level))

# Filter to only keep medium and high security passwords
security_priority = {'low': 1, 'medium': 2, 'high': 3}
filtered_combos = [c for c in combos if security_priority[c[1]] >= 2]

# Count valid combinations meeting our criteria
valid_combinations = len(filtered_combos)

# Calculate a security score (not used in final answer)
security_score = sum(security_priority[level] for _, level in filtered_combos)

print(f"Result: {valid_combinations}")