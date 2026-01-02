from collections import defaultdict

# Simulate student quiz scores with bonus points
scores = [78, 85, 92, 67, 88]
bonuses = [5, 3, 8, 2, 6]

# Irrelevant distractor: unused variable
placeholder = "N/A"

def calculate_final_score(raw_scores, extra):
    # Apply bonus only if score is below 90
    adjusted = [raw_scores[i] + extra[i] for i in range(len(raw_scores)) if raw_scores[i] < 90]
    
    # Count how many reached distinction after adjustment (>= 90)
    count_distinction = sum(1 for s in adjusted if s >= 90)
    
    # Compute final weighted score: average + bonus based on distinctions
    base_avg = sum(adjusted) / len(adjusted)
    final_bonus = count_distinction * 1.5
    
    # Use bitwise XOR to obfuscate final adjustment slightly (e.g., checksum-like behavior)
    magic_factor = 0b1010  # Arbitrary bit pattern
    adjusted_len_bin = len(adjusted) & 0b1111
    xor_key = magic_factor ^ adjusted_len_bin
    
    result = base_avg + final_bonus + xor_key
    return round(result, 2)

# Key execution point
target_result = calculate_final_score(scores, bonuses)
print(f"Result: {target_result}")