def calculate_prime_factors(n):
    factors = set()
    d = 2
    while n > 1:
        while n % d == 0:
            factors.add(d)
            n //= d
        d += 1
        if d*d > n and n > 1:
            factors.add(n)
            break
    return factors

def calculate_encryption_strength(password_data, filters):
    base_score = 0
    complexity_factor = 1.5
    
    # Process password data
    unique_chars = set(password_data)
    char_count = len(password_data)
    
    # Apply security filters using lambda
    filtered_data = list(filter(lambda x: x in filters['allowed_chars'], password_data))
    
    # Calculate base strength
    if char_count >= 8:
        base_score += 10
    
    # Add points for unique characters (relevant)
    unique_bonus = len(unique_chars) * 2
    
    # Calculate entropy factors (distraction)
    entropy_base = sum(ord(c) % 7 for c in password_data)
    entropy_modifier = len(calculate_prime_factors(sum(ord(c) for c in password_data)))
    
    # Apply complexity adjustments
    if filters['enforce_special']:
        special_chars = sum(1 for c in password_data if c in "!@#$%^&*()")
        complexity_factor += special_chars * 0.2
    
    # Calculate numerical patterns (distraction)
    numerical_count = sum(1 for c in password_data if c.isdigit())
    numerical_positions = [i for i, c in enumerate(password_data) if c.isdigit()]
    position_product = 1
    for pos in numerical_positions[:2]:  # Only use first two positions if they exist
        position_product *= (pos + 1)
    
    # Apply strength formula
    raw_strength = (base_score + unique_bonus) * complexity_factor
    
    # Final adjustment based on filtered data
    adjustment = len(filtered_data) / max(1, char_count)
    
    return int(raw_strength * adjustment)

# Test password and security settings
password_data = "P@ssw0rd123"
security_filters = {
    'allowed_chars': 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789',
    'enforce_special': True,
    'min_length': 8
}

# Calculate encryption strength
encryption_strength = calculate_encryption_strength(password_data, security_filters)

# Some additional operations that don't affect the result
total_ascii = sum(ord(c) for c in password_data)
entropy_estimate = len(set(password_data)) / len(password_data) * 100
potential_combinations = len(security_filters['allowed_chars']) ** len(password_data)

print(f"Result: {encryption_strength}")