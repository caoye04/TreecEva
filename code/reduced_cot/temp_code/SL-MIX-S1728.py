from itertools import permutations
from collections import defaultdict

def fibonacci_sequence(n):
    if n <= 0:
        return []
    elif n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    else:
        seq = [1, 1]
        for i in range(2, n):
            seq.append(seq[i-1] + seq[i-2])
        return seq

# Ancient script character set
rare_glyphs = ['♐', '♑', '♒', '♓', '♈']
glyph_weights = {'♐': 3, '♑': 5, '♒': 2, '♓': 7, '♈': 4}

# Calculate Fibonacci weights for first 10 positions
fib_weights = fibonacci_sequence(10)

# Initialize complexity analyzer
pattern_frequency = defaultdict(int)
linguistic_complexity_score = 0

# Generate all 3-character permutations
for idx, perm in enumerate(permutations(rare_glyphs, 3)):
    # Early termination for computational efficiency
    if idx >= 30:
        break
        
    # Calculate pattern weight
    pattern_weight = sum(glyph_weights[char] for char in perm)
    
    # Apply Fibonacci positional weighting
    fib_multiplier = fib_weights[idx % len(fib_weights)]
    
    # Conditional scoring based on pattern characteristics
    if pattern_weight > 10:
        adjusted_score = pattern_weight * fib_multiplier
    else:
        adjusted_score = pattern_weight + fib_multiplier
    
    # Update frequency map and cumulative score
    pattern_key = ''.join(perm)
    pattern_frequency[pattern_key] = adjusted_score
    linguistic_complexity_score += adjusted_score
    
    # Break early if complexity threshold reached
    if linguistic_complexity_score > 1000:
        break

print(f"Result: {linguistic_complexity_score}")