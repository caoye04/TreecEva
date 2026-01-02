def analyze_pattern(sequence):
    if len(sequence) < 3:
        return 0
    count = 0
    for i in range(len(sequence) - 2):
        if sequence[i] < sequence[i+1] > sequence[i+2]:
            count += 1
    return count

# Irrelevant helper function (decoy)
def compute_entropy(data):
    import math
    freq = {}
    for item in data:
        freq[item] = freq.get(item, 0) + 1
    entropy = 0.0
    total = len(data)
    for f in freq.values():
        p = f / total
        entropy -= p * math.log2(p)
    return round(entropy, 4)

# Misleading intermediate calculation
temp_result = [x**2 % 17 for x in range(15) if x % 3 != 0]
phantom_sum = sum(temp_result[:5]) * 0.5  # Dead-end computation

# Core logic disguised among distractors
def transform_metrics(raw_values, offset=3):
    adjusted = [(v + offset) ** 0.5 for v in raw_values if v > 0]
    filtered = [val for val in adjusted if val.is_integer()]
    return [int(x) for x in filtered]

# Unused but plausible function
def validate_structure(container):
    if not isinstance(container, list) or len(container) == 0:
        return False
    return all(isinstance(x, int) and x >= 0 for x in container)

# String-based distractor block
log_entry = "ERROR: Failed to process batch at index 7"
diagnostic_tag = log_entry.split(':')[0].lower().strip()
warning_count = len([c for c in diagnostic_tag if c in 'aeiou'])  # Red herring

# Data setup with noise
event_codes = [1, -2, 3, 4, -5, 6, 7, 8, 9]
metadata_flags = {k: (k % 4 == 0) for k in range(1, 10)}

# Another decoy transformation
shadow_copy = event_codes[::-1]
for idx in range(len(shadow_copy)):
    if shadow_copy[idx] < 0:
        shadow_copy[idx] = abs(shadow_copy[idx]) * 2

# Key function buried in complexity
def evaluate_performance(metrics, profile):
    # Extract relevant subset
    active_metrics = [m for m in metrics if m > 2]
    
    # Distracting normalization
    norm_factor = sum([i*i for i in range(1,6)]) / 55.0  # Always 1.0, but looks complex
    
    # Real transformation
    processed = transform_metrics(active_metrics, offset=len(profile.get('tags', [])))
    
    # Spurious conditional check (always true in this context)
    if len(processed) >= 2 and any(p > 2 for p in processed):
        base = processed[0] * processed[-1]
        
        # Additional valid operation mixed with noise
        sequence_check = analyze_pattern([base, base+3, base-1, base+2, base])
        bonus = 5 if sequence_check > 0 else 0
        
        # Final red herring: string length diversion
        tag_string = ''.join(profile.get('tags', ['X']))
        penalty = len(tag_string) if 'Z' in tag_string else 2
        
        return base + bonus - penalty
    
    return -1

# Actual execution path
user_profile = {
    'id': 'USR-92837',
    'tags': ['alpha', 'beta', 'gamma'],  # length 3, affects penalty
    'active': True
}

metric_data = [4, 5, -1, 6, 3, 2, 8]  # Will filter negatives and low values

# Critical statement
final_score = evaluate_performance(metric_data, user_profile)
print(f"Result: {final_score}")