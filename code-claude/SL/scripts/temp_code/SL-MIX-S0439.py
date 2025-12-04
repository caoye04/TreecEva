# Password policy checker function

def analyze_passwords(passwords, blacklist):
    # Configuration
    min_length = 6
    has_uppercase = False
    
    # Filter out blacklisted words
    filtered_words = [pwd for pwd in passwords if pwd.lower() not in blacklist]
    
    # Count valid passwords (with sufficient length)
    valid_count = sum(1 for word in filtered_words if len(word) >= min_length)
    
    # Check if any password has uppercase
    for pwd in filtered_words:
        if any(char.isupper() for char in pwd):
            has_uppercase = True
            break
    
    # Calculate security score
    security_rating = valid_count * (2 if has_uppercase else 1)
    
    print(f"Result: {valid_count}")
    return valid_count

# Test data
password_list = ["abc123", "password", "Secret", "hi", "AdminUser"]
blacklist_words = ["password", "admin"]

# Run analysis
result = analyze_passwords(password_list, blacklist_words)