def preprocess_inputs(raw_values):
    cleaned = [x for x in raw_values if isinstance(x, (int, float)) and x > 0]
    normalized = [x / max(cleaned) for x in cleaned]
    return [round(x, 3) for x in normalized]


def analyze_pattern(seq):
    peaks = 0
    for i in range(1, len(seq) - 1):
        if seq[i-1] < seq[i] > seq[i+1]:
            peaks += 1
    return peaks

raw_data = [15, -3, 22, 0, 41, 'invalid', 8, 19, 41, 33]
config_params = {'scale': 2.5, 'offset': -1.2, 'active': True}

processed_data = preprocess_inputs(raw_data)

# Simulate auxiliary diagnostic check (not directly used)
diagnostic_flags = {}
diagnostic_flags['zero_count'] = sum(1 for x in raw_data if x == 0)
diagnostic_flags['negative_count'] = sum(1 for x in raw_data if isinstance(x, (int, float)) and x < 0)
diagnostic_flags['string_count'] = sum(1 for x in raw_data if isinstance(x, str))

baseline_ref = [0.366, 0.537, 1.0, 0.463, 0.780, 0.805]

# Misleading comparison with baseline (distractor computation)
similarity_score = 0
for a, b in zip(processed_data, baseline_ref):
    similarity_score += abs(a - b)
similarity_score = round(similarity_score, 4)

# Unused helper logic (dead path)
def adjust_magnitude(val, factor=1.1):
    return val * factor if val < 0.7 else val

# Main control flow with conditional logic
if len(processed_data) >= 5:
    magnitude_factor = 1.2
else:
    magnitude_factor = 0.8

adjusted_data = [x * magnitude_factor for x in processed_data]

# Threshold determined by pattern analysis
peak_count = analyze_pattern(processed_data)
threshold = 0.45 + (peak_count * 0.05)

# Core efficiency calculation
relevant_entries = [x for x in adjusted_data if x > threshold]
penalty = len(adjusted_data) - len(relevant_entries)
efficiency_numerator = sum(relevant_entries)
efficiency_denominator = len(relevant_entries) if relevant_entries else 1

# Final score computation
efficiency_score = efficiency_numerator / efficiency_denominator

# Irrelevant logging output (distraction)
log_entry = f"Processing complete: {len(raw_data)} inputs, {len(processed_data)} valid, {penalty} penalized"

diagnostic_flags['status'] = 'complete'

# Output the target result
Result: efficiency_score