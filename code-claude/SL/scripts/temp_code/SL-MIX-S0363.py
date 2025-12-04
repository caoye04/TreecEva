def validate_email(email):
    # Parse email into username and domain
    if '@' not in email or email.count('@') > 1:
        return False
    
    parts = email.split('@')
    username = parts[0].lower()
    domain_parts = parts[1].split('.')
    
    # Various validation checks
    if len(username) < 3 or len(domain_parts) < 2:
        return False
    
    # Check domain validity
    email_domain = domain_parts[0].lower()
    tld = domain_parts[-1].lower()
    
    # Calculate statistics about the email
    digits_in_username = sum(1 for char in username if char.isdigit())
    special_chars = sum(1 for char in username if not char.isalnum())
    domain_length = len(email_domain)
    
    # Find common characters between username and domain
    common_chars = len(set(email_domain).intersection(set(username)))
    
    # Calculate domain score (not used in validation)
    popular_tlds = {'com': 10, 'org': 8, 'net': 7, 'edu': 9, 'io': 6}
    domain_score = popular_tlds.get(tld, 3) + domain_length
    
    # Calculate username strength (not directly used)
    username_strength = len(username) + digits_in_username * 2 - common_chars
    
    # Additional checks that don't affect the final result
    has_uppercase = any(char.isupper() for char in email)
    consecutive_digits = 0
    max_consecutive = 0
    
    for char in username:
        if char.isdigit():
            consecutive_digits += 1
            max_consecutive = max(max_consecutive, consecutive_digits)
        else:
            consecutive_digits = 0
    
    # Final validation (not relevant to our question)
    is_valid = (domain_length >= 2 and special_chars <= 2)
    
    print(f"Common characters: {common_chars}")
    return is_valid

# Test with sample email
email = "user123@example.com"
validate_email(email)