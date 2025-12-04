def generate_security_params(user_level, access_attempts):
    # Initialize security parameters
    base_value = 42
    verification_code = 0
    security_threshold = 100
    
    # Process user level (only odd levels matter for verification)
    if user_level > 0:
        verification_code = user_level if user_level % 2 == 1 else user_level + 1
        security_threshold += user_level * 5
    
    # Process access history
    failed_attempts = sum(1 for attempt in access_attempts if not attempt)
    successful_attempts = len(access_attempts) - failed_attempts
    
    # Calculate security modifier based on attempts
    security_modifier = successful_attempts - failed_attempts
    base_value = base_value + (security_modifier if security_modifier > 0 else 0)
    
    # Generate distraction values
    potential_keys = [base_value + i for i in range(3)]
    backup_code = lambda x: x * 2 - 3
    alternative_value = backup_code(verification_code)
    
    # Update verification code based on security threshold
    if security_threshold > 150:
        verification_code = verification_code + 10
    elif security_threshold > 120:
        verification_code = verification_code + 5
    
    # Set mask for bitwise operation
    mask = 0xFF
    if failed_attempts > successful_attempts:
        mask = 0x7F
    
    # Final key calculation with bitwise operations
    encryption_key = (base_value ^ verification_code) & mask
    print(encryption_key)
    validation_key = (alternative_value & mask) | base_value
    
    return {
        "encryption": encryption_key,
        "validation": validation_key,
        "threshold": security_threshold
    }

# Test the function
user_level = 7
access_log = [True, True, False, True, True]
result = generate_security_params(user_level, access_log)
print(f"Result: {result['encryption']}")