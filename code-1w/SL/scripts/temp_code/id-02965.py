def analyze_text_pattern(text):
    char_freq = {}
    for c in text:
        char_freq[c] = char_freq.get(c, 0) + 1
    
    # Distractor: count vowels but not used later
    vowel_count = sum(1 for v in 'aeiou' if v in char_freq)
    
    # Generate list of positions for consonants (semi-relevant)
    consonant_positions = [i for i, c in enumerate(text) if c.isalpha() and c.lower() not in 'aeiou']
    
    # Distractor: unused transformation
    shifted = ''.join(chr((ord(c) - ord('a') + 3) % 26 + ord('a')) if c.islower() else c for c in text)
    
    return consonant_positions

# Helper to check primality (used later)
is_prime = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n**0.5)+1))

# Main data processing
sequence = list(range(10, 25))
prime_flags = [is_prime(num) for num in sequence]

# Weight assignment with distractor elements
weights = []
base_weight = 1.5
for i, flag in enumerate(prime_flags):
    weight = base_weight + i * 0.1
    if flag:
        weight *= 1.2
    # Dead code path (never executed due to logic)
    if False and i > 20:
        weight += 100  # unreachable
    weights.append(round(weight, 4))

# Distractor: create auxiliary structure not fully used
aux_data = dict(zip(sequence, enumerate(weights)))
index_map = {val: idx for idx, val in enumerate(sequence)}

# Secondary computation - counts something irrelevant
running_sum = 0
for pos, val in enumerate(sequence):
    if val % 2 == 0:
        running_sum += pos * 2

# Core calculation function
def calculate_total(flags, wts):
    total = 0.0
    # Use enumerate and zipped iteration
    for idx, (f, w) in enumerate(zip(flags, wts)):
        if f:
            total += w * (idx + 1)
        else:
            total -= w * 0.5
    # Minor nonlinear adjustment
    return round(total + (0.25 if total > 10 else 0), 4)

# Critical execution point
final_score = calculate_total(prime_flags, weights)

# Print result as required
print(f"Result: {final_score}")