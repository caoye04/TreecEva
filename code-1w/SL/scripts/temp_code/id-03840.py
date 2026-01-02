def analyze_text_composition(text):
    char_freq = {}
    for c in text:
        if c.isalpha():
            char_freq[c.lower()] = char_freq.get(c.lower(), 0) + 1
    total_letters = sum(char_freq.values())
    unique_letters = len(char_freq)
    entropy = 0.0
    for freq in char_freq.values():
        p = freq / total_letters
        entropy -= p * __import__('math').log2(p)
    return {'total': total_letters, 'unique': unique_letters, 'entropy': round(entropy, 4)}

# Irrelevant helper function (decoy)
def compute_fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# Unused transformation map (distractor)
transformation_map = {i: chr((i + 13) % 26 + ord('a')) for i in range(26)}

# Misleading intermediate calculation (red herring)
redundant_sum = sum([i ** 2 for i in range(1, 15) if i % 3 == 0])

# Real data processing begins
raw_data_stream = 'AABBCDEEFFGGHHIIJJKKLLMMNNOOPPQQRRSSTTUUVVWWXXYYZZ'
data = [len(s) for s in raw_data_stream.split('D')]

# Weight configuration (some irrelevant entries)
weights = {
    'base': 1.5,
    'multiplier': 2.0,
    'offset': -3,
    'junk_factor': 999,  # unused
    'debug_mode': True     # unused
}

# Secondary decoy structure
temp_results = []
for idx, val in enumerate(data):
    temp = (idx + 1) * val ** 2
    if temp > 10:
        temp_results.append(temp // 2)

# Another red herring: tuple unpacking with dummy values
dummy_entries = [(1, 2, 'skip'), (3, 4, 'skip'), (5, 6, 'use')]
for x, y, label in dummy_entries:
    if label == 'use':
        adjustment = x + y  # Only this one matters, rest are distractions

# Core logic hidden among noise
def preprocess_sequence(seq, factor=1.2):
    processed = []
    for i, v in enumerate(seq):
        if i % 2 == 0:
            processed.append(v * factor)
        else:
            processed.append(v + factor)
    return [round(p, 2) for p in processed]

processed_data = preprocess_sequence(data, 1.1)

# Main scoring function buried in complexity
def calculate_final_score(sequence, config):
    base = config['base']
    mult = config['multiplier']
    offset = config['offset']
    
    # Real computation chain
    total = sum(sequence)
    max_val = max(sequence)
    avg = total / len(sequence)
    
    # Use enumerate and zip as required
    indexed = list(enumerate(sequence))
    shifted = [0] + sequence[:-1]
    pairs = list(zip(sequence, shifted))
    diffs = [a - b for a, b in pairs][1:]
    
    trend_score = sum(1 for d in diffs if d > 0) - sum(1 for d in diffs if d < 0)
    
    # Final formula combining multiple concepts
    raw_score = (avg * base + max_val / 2) * mult + trend_score + offset
    
    # Adjustment from earlier decoy
    global adjustment
    raw_score += adjustment  # adds 11 (from x=5, y=6)
    
    # This dictionary is never used (distractor)
    metadata_log = {
        'input_length': len(sequence),
        'computed_avg': avg,
        'timestamp': 'ignored'
    }
    
    return int(round(raw_score))

# Execute main logic
final_score = calculate_final_score(processed_data, weights)

# Print result as required
print(f"Target result: {final_score}")