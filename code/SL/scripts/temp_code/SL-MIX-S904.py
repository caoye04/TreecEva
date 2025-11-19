from collections import Counter
from itertools import combinations

def calculate_positional_score(fragment):
    char_positions = {}
    for idx, char in enumerate(fragment):
        if char not in char_positions:
            char_positions[char] = []
        char_positions[char].append(idx)
    
    score = 0
    for positions in char_positions.values():
        if len(positions) > 1:
            # Calculate sum of distances between all position pairs
            for pos1, pos2 in combinations(positions, 2):
                score += abs(pos2 - pos1)
    return score

def compute_frequency_weight(fragment):
    freq = Counter(fragment)
    total_chars = len(fragment)
    weight = 1.0
    for count in freq.values():
        ratio = count / total_chars
        weight *= (1.0 + ratio) if ratio > 0.25 else (1.0 - ratio)
    return weight

ancient_fragment = "abracadabra"
positional_score = calculate_positional_score(ancient_fragment)
frequency_weight = compute_frequency_weight(ancient_fragment)

# Apply ternary operator for normalization based on fragment length
normalized_score = positional_score/len(ancient_fragment) if len(ancient_fragment) > 10 else positional_score

# Final fragment score combines positional analysis with frequency adjustments
fragment_score = int(normalized_score * (frequency_weight * 100)) if frequency_weight > 0.8 else int(normalized_score + (frequency_weight * 10))

print(f"Result: {fragment_score}")