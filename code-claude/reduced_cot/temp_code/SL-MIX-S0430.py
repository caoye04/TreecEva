def analyze_lock_combination(digits, pattern):
    # Initial values for analysis
    base_value = sum(d for d in digits if d % 2 == 0)
    noise_factor = len([p for p in pattern if p.isupper()])
    
    # Process the digits with some transformations
    transformed = []
    for i, digit in enumerate(digits):
        # Apply transformation based on pattern
        if i < len(pattern) and pattern[i].isalpha():
            transformed.append((digit * 2) % 10)
        else:
            transformed.append(digit)
    
    # Calculate potential combinations
    potential_a = sum(transformed) % 16
    potential_b = (base_value + noise_factor) % 16
    
    # Determine direction factors
    clockwise_factor = sum(1 for c in pattern if c.islower())
    counter_factor = sum(1 for c in pattern if c.isupper())
    
    # Directional preference calculation
    is_clockwise = clockwise_factor > counter_factor
    
    # Secondary calculations that don't affect the result
    security_level = (max(digits) * min(digits)) % 100
    complexity_score = len(set(digits)) * noise_factor
    
    # Determine the lock's optimal position
    result = potential_a ^ potential_b
    
    # Final rotation adjustment based on direction
    optimal_rotation = (result & 0xF) if is_clockwise else 15 - (result & 0xF)
    
    print(f"Result: {optimal_rotation}")
    return optimal_rotation

# Lock combination and pattern
digits = [3, 8, 5, 2, 9]
pattern = "AbCdE"

# Analyze the combination
rotation = analyze_lock_combination(digits, pattern)