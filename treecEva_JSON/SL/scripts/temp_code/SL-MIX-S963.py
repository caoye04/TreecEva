from collections import defaultdict

def calculate_security_score():
    # Packet signature sets from different network zones
    zone_a_signatures = frozenset({12, 25, 33, 47, 58})
    zone_b_signatures = frozenset({25, 33, 64, 71, 82})
    zone_c_signatures = frozenset({12, 47, 64, 91, 103})
    
    # Find common signatures between all zones
    common_signatures = zone_a_signatures & zone_b_signatures & zone_c_signatures
    
    # Count total occurrences of each signature across zones
    signature_counter = defaultdict(int)
    for sig in zone_a_signatures | zone_b_signatures | zone_c_signatures:
        count = sum([sig in zone_a_signatures, sig in zone_b_signatures, sig in zone_c_signatures])
        signature_counter[sig] = count
    
    # Calculate base metric from signature overlaps
    overlap_sum = sum(common_signatures)
    
    # Apply modular transformation based on signature counts
    transformed_values = []
    for sig, count in signature_counter.items():
        if count >= 2:  # Only consider signatures appearing in multiple zones
            mod_result = (sig * count) % 17
            transformed_values.append(mod_result)
    
    # Compute security score using comparison and modular arithmetic
    security_score = 0
    for val in transformed_values:
        if val > 8:
            security_score += val * 2
        else:
            security_score += val
        
    security_score = security_score % 100
    return security_score

security_score = calculate_security_score()
print(f"Result: {security_score}")