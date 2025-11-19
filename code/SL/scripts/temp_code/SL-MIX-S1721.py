import itertools

def analyze_signal_patterns(frequencies):
    extraterrestrial_score = 0
    
    # Generate all permutations of length 3
    for perm in itertools.permutations(frequencies, 3):
        # Early return condition for invalid patterns
        if perm[0] <= perm[1] and perm[1] <= perm[2]:
            continue
            
        # Calculate pattern strength using lambda closure
        strength_calculator = lambda x, y, z: (x & y) ^ z
        pattern_strength = strength_calculator(perm[0], perm[1], perm[2])
        
        # Only consider strong patterns
        if pattern_strength > 10:
            extraterrestrial_score += pattern_strength
        
        # Break if we've found enough strong patterns
        if extraterrestrial_score > 100:
            break
    
    return extraterrestrial_score

# Deep space observation data
observed_frequencies = [15, 7, 22, 3, 11, 19, 5]

# Combinatorics-based filtering of frequencies
filtered_frequencies = [f for f in observed_frequencies if f % 2 == 1]

extraterrestrial_score = analyze_signal_patterns(filtered_frequencies)
print(f"Result: {extraterrestrial_score}")