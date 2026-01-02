def analyze_text(text):
    char_freq = {}
    for char in text.lower():
        if char.isalpha():
            char_freq[char] = char_freq.get(char, 0) + 1
    return char_freq

# Irrelevant helper function (decoy)
def calculate_entropy(data):
    import math
    total = sum(data.values())
    entropy = 0
    for count in data.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 6)

# Unused transformation function (dead code path)
def transform_data(x):
    return [i**2 for i in x if i % 2 == 0]

# Main processing pipeline
def preprocess_metrics(raw):
    cleaned = {k: max(v, 0) for k, v in raw.items()}
    normalized = {}
    total = sum(cleaned.values())
    for k, v in cleaned.items():
        normalized[k] = v / total if total > 0 else 0
    return normalized

# Complex weighting logic with distractors
def apply_weights(vals, wts):
    result = 0
    adjustment_factor = 0.85  # red herring variable
    temp_store = []  # misleading intermediate storage
    for key in vals:
        if key in wts:
            weighted_val = vals[key] * wts[key]
            temp_store.append(weighted_val)
            result += weighted_val
    # Spurious normalization (not actually affecting final result)
    if len(temp_store) > 3:
        avg_temp = sum(temp_store) / len(temp_store)
        result = result * (1 + avg_temp * 0.01)  # negligible impact
    return result

# Core evaluation function
def evaluate_performance(met, wghts):
    processed = preprocess_metrics(met)
    score = apply_weights(processed, wghts)
    bonus = 0
    # Conditional bonus logic (partially irrelevant)
    if 'readability' in processed and processed['readability'] > 0.3:
        bonus += 5
    if 'complexity' in processed:
        bonus -= 2  # counteracts previous line, net zero effect
    # Final adjustment based on character diversity (real but subtle)
    diversity_bonus = len(set(''.join(met.keys()))) * 0.01
    return round(score * 100 + bonus + diversity_bonus, 6)

# Simulated input generation
raw_input = {
    'readability': 0.72,
    'accuracy': 0.85,
    'consistency': 0.68,
    'verbosity': 0.44,
    'structure': 0.91
}

# Weight configuration (critical)
weights = {
    'readability': 0.2,
    'accuracy': 0.35,
    'consistency': 0.25,
    'verbosity': 0.1,
    'structure': 0.1
}

# Phantom data structure (distractor)
diagnostic_log = {
    'timestamp': '2023-11-05',
    'version': '2.1.0',
    'status': 'completed',
    'ignored_value': sum(len(str(v)) for v in raw_input.values())
}

# Auxiliary lambda (meets language feature requirement)
validate_range = lambda x: 0 <= x <= 1

# Validate inputs (has side-effect of filtering but not used directly)
valid_metrics = {k: v for k, v in raw_input.items() if validate_range(v)}

# Another decoy operation
snapshot = list(map(lambda item: f'{item[0]}:{item[1]:.2f}', valid_metrics.items()))

# Key execution point
final_score = evaluate_performance(valid_metrics, weights)

# Output result as required
print(f"Result: {final_score}")