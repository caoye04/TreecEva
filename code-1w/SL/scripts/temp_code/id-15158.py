import math

# Simulated system log analysis with embedded computational logic
def preprocess_logs(raw):
    cleaned = []
    noise_filter = lambda x: x if x > 0 else 0
    for entry in raw:
        temp_val = abs(entry) ** 0.5
        if temp_val > 3:
            cleaned.append(int(noise_filter(temp_val)))
    return cleaned

# Irrelevant helper - dead code path (distractor)
def decrypt_sequence(data):
    return [x ^ 7 for x in data][::-1]

# Another red herring function dealing with unused security tokens
def validate_tokens(tokens):
    token_set = set()
    for t in tokens:
        if t % 2 == 0:
            token_set.add(t * 3)
    return sorted(list(token_set), reverse=True)

def compute_entropy(values):
    total = sum(values)
    if total == 0:
        return 0.0
    entropy = 0.0
    for v in values:
        p = v / total
        if p > 0:
            entropy -= p * math.log(p)
    return round(entropy, 6)

# Core diagnostic engine - combines multiple paradigms
def analyze_pattern(logs, flags):
    # Step 1: Preprocess logs
    processed = preprocess_logs(logs)
    
    # Step 2: Extract features
    feature_vector = []
    for i, val in enumerate(processed):
        if i % 2 == 0:
            feature_vector.append(val + 2)
        else:
            feature_vector.append(val * 2)
    
    # Step 3: Flag-based filtering
    active_flags = [f for f in flags if f in {1, 3, 4}]
    mask_value = 1
    for af in active_flags:
        mask_value <<= af
    
    # Step 4: Apply bit manipulation (irrelevant to final result but looks important)
    masked_features = [f ^ mask_value for f in feature_vector]
    
    # Step 5: Compute statistical profile (distraction)
    mean_val = sum(masked_features) / len(masked_features) if masked_features else 0
    variance = sum((x - mean_val) ** 2 for x in masked_features) / len(masked_features) if masked_features else 0
    
    # Step 6: Character frequency analysis on string representation (red herring)
    str_repr = ''.join([str(int(x)) for x in masked_features[:5]])
    char_count = {}
    for c in str_repr:
        char_count[c] = char_count.get(c, 0) + 1
    
    # Step 7: Conditional data transformation chain
    intermediate = 0
    for idx, fv in enumerate(feature_vector):
        if idx < 2:
            intermediate += fv * 3
        elif idx == 2:
            intermediate -= fv
        else:
            intermediate += fv // 2
    
    # Step 8: Final computation - depends only on first 4 logs and flag 3 presence
    base_score = sum(processed[:4])
    bonus = 17 if 3 in flags else 0
    penalty = len([x for x in logs if x < -5]) * 5
    
    # Critical statement
    final_diagnostic = base_score + bonus - penalty + intermediate % 19
    
    # Distractor: Unused complex structure
    diagnostics_report = {
        'raw_integrity': validate_tokens([len(logs), len(flags)]),
        'entropy_metric': compute_entropy(processed),
        'anomaly_map': {i: chr(65 + i % 26) for i in range(len(processed))},
        'debug_trace': decrypt_sequence([1, 2, 3, 4, 5])
    }
    
    return final_diagnostic

# Input data - carefully crafted to produce deterministic output
raw_log_data = [16, -25, 36, -49, 64, 81, -100]
system_security_flags = [1, 3, 7, 9]

# Execution flow
log_entries = raw_log_data
flags_config = system_security_flags

# Key assignment
final_diagnostic = analyze_pattern(log_entries, system_flags)

print(f"Result: {final_diagnostic}")