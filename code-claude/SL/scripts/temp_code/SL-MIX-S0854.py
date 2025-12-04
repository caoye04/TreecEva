def validate_passwords(password_list):
    valid_passwords = 0
    total_passwords = len(password_list)
    
    for entry in password_list:
        policy, password = entry.split(': ')
        policy_range, required_char = policy.split(' ')
        min_count, max_count = map(int, policy_range.split('-'))
        
        # Count characters that appear in password
        char_count = password.count(required_char)
        
        # Check if password meets the policy requirements
        valid_passwords += 1 if min_count <= password.count(required_char) <= max_count else 0
    
    return valid_passwords

# Test data
password_entries = [
    '1-3 a: abcde',
    '1-3 b: cdefg',
    '2-9 c: ccccccccc'
]

result = validate_passwords(password_entries)
print(f"Valid passwords: {result}")