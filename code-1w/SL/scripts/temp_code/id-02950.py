def process_metrics(entries):
    total = 0
    count = 0
    for entry in entries:
        if 'valid' in entry and entry['valid']:
            total += entry.get('value', 0) * entry.get('weight', 1)
            count += 1
    return total / count if count else 0

# Irrelevant helper (dead path)
def analyze_sentiment(text):
    return sum(1 for c in text if c in '!?.')

# Decoy accumulator with misleading intermediate
temp_accumulator = 0
for i in range(17):
    temp_accumulator += (i * i) % 5

# Core transformation pipeline
data_stream = [
    {'value': 3, 'weight': 2, 'valid': True, 'meta': 'A'},
    {'value': 5, 'weight': 1, 'valid': True, 'meta': 'B'},
    {'value': 8, 'weight': 3, 'valid': False, 'meta': 'C'},  # invalid
    {'value': 4, 'weight': 2, 'valid': True, 'meta': 'D'},
    {'value': 7, 'weight': 1, 'valid': True, 'meta': 'E'}
]

# Unused but plausible-looking filter
cleaned_data = [d for d in data_stream if d.get('value', 0) > 2]

# Bit manipulation red herring
bit_fingerprint = 0
for d in data_stream:
    bit_fingerprint ^= d['value'] << 1
    bit_fingerprint |= len(d.get('meta', ''))

# Conditional expression with distractor logic
size_factor = 2 if len(data_stream) > 4 else 1
bonus_shift = (lambda x: x >> 1 if x % 2 else x // 3)(bit_fingerprint & 15)

# Real computation chain begins
base_score = process_metrics(data_stream)

# Simulated normalization (partially irrelevant)
normalized_scores = []
for d in data_stream:
    if d.get('valid', False):
        norm_val = (d['value'] - base_score) ** 2
        normalized_scores.append(norm_val)

variance_proxy = sum(normalized_scores) / len(normalized_scores) if normalized_scores else 0

# Fake aggregation to mislead control flow understanding
dummy_aggregate = 0
for ns in normalized_scores:
    dummy_aggregate += ns * 0.9

# Critical recursive reduction (simple recursion + conditional expression)
def compute_final_threshold(stream, depth=0):
    if depth >= 3 or not stream:
        return base_score + variance_proxy
    
    valid_values = [s['value'] for s in stream if s.get('valid', False)]
    if not valid_values:
        return base_score
    
    mid = len(valid_values) // 2
    left_half = [{'value': v, 'valid': True} for v in valid_values[:mid]]
    right_half = [{'value': v, 'valid': True} for v in valid_values[mid:]]
    
    # Conditional expression blend
    left_contribution = (lambda x: x[0] if x else 0)(sorted(left_half, key=lambda e: e['value']))
    right_contribution = (lambda x: x[-1] if x else 0)(sorted(right_half, key=lambda e: e['value']))
    
    combined_hint = (left_contribution + right_contribution) / 2
    
    # Recursive refinement step
    return compute_final_threshold(
        [{'value': combined_hint, 'valid': True}], 
        depth + 1
    )

# Misleading secondary function call (never used)
def calculate_entropy(seq):
    from math import log2
    freq = {}
    for s in seq:
        freq[s] = freq.get(s, 0) + 1
    return -sum((f / len(seq)) * log2(f / len(seq)) for f in freq.values())

# Key execution point
threshold_balance = compute_final_threshold(data_stream)

# Print final result as required
print(f"Result: {threshold_balance}")