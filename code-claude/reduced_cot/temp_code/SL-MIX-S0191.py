def calculate_security_score(password_data):
    # Calculate password security score based on multiple factors
    base_score = 0
    length_factor = 0
    complexity_bonus = 0
    penalty = 0
    
    # Process each password attempt
    for entry in password_data:
        username = entry['username']
        password = entry['password']
        timestamp = entry['timestamp']
        
        # Analyze password length (primary factor)
        if len(password) >= 12:
            length_factor = 50
        elif len(password) >= 8:
            length_factor = 30
        else:
            length_factor = 10
        
        # Check for complexity (secondary factor)
        has_upper = any(c.isupper() for c in password)
        has_lower = any(c.islower() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_special = any(not c.isalnum() for c in password)
        
        # Calculate complexity bonus
        complexity_count = sum([has_upper, has_lower, has_digit, has_special])
        complexity_bonus = complexity_count * 10
        
        # Check for common patterns (penalties)
        common_patterns = ['123', 'abc', 'password', 'admin']
        pattern_check = password.lower()
        for pattern in common_patterns:
            if pattern in pattern_check:
                penalty += 15
                break
        
        # Calculate base score for this entry
        entry_score = length_factor + complexity_bonus - penalty
        
        # Track highest base score
        if entry_score > base_score:
            base_score = entry_score
        
        # Distractor: Calculate time-based metrics that aren't used
        time_parts = timestamp.split(':')  
        hour = int(time_parts[0])
        minute = int(time_parts[1])
        time_factor = (hour * 60 + minute) % 24
    
    # Distractor: Analyze username patterns (not used in final calculation)
    username_stats = {}
    for entry in password_data:
        first_char = entry['username'][0].lower() if entry['username'] else ''
        if first_char in username_stats:
            username_stats[first_char] += 1
        else:
            username_stats[first_char] = 1
    
    # Apply normalization factor (unnecessary calculation)
    normalization = 100 / 90
    adjusted_score = base_score * normalization
    
    # Final security level determination
    if base_score >= 70:
        return 3  # High security
    elif base_score >= 40:
        return 2  # Medium security
    else:
        return 1  # Low security

# Test data
password_data = [
    {'username': 'admin', 'password': 'Secure123!', 'timestamp': '14:25'},
    {'username': 'user1', 'password': 'password123', 'timestamp': '09:30'},
    {'username': 'developer', 'password': 'C0d3r@2023', 'timestamp': '11:45'}
]

# Calculate the security score
security_level = calculate_security_score(password_data)

print(f"Result: {security_level}")