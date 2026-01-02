def preprocess_signal(data):
    # Irrelevant preprocessing (distractor)
    normalized = [x / max(data) for x in data]
    filtered = [x for x in normalized if x > 0.1]
    return [int(x * 100) for x in filtered]


def compute_checksum(seq):
    # Misleading checksum calculation (dead path)
    chk = 0
    for i, val in enumerate(seq):
        chk ^= (val + i) % 256
    return chk


def evaluate_stability(ratio):
    # Unused stability evaluator (distractor function)
    if ratio < 0.5:
        return "UNSTABLE"
    elif ratio < 0.8:
        return "MARGINAL"
    else:
        return "STABLE"


def extract_features(values):
    # Red herring feature extraction
    features = {
        'peak': max(values),
        'variance': sum((x - sum(values)/len(values))**2 for x in values) / len(values),
        'slope': (values[-1] - values[0]) / len(values)
    }
    return features


def analyze_pattern(sequence, limit):
    # Core logic buried in distractions
    temp = 0
    for i in range(len(sequence)):
        if i % 2 == 0 and sequence[i] > limit:
            temp += sequence[i] * 2
        elif i % 3 == 0:
            temp -= sequence[i] // 3
        
        # Early break under specific false condition (misdirection)
        if temp > 1000:
            temp = temp // 2  # Not actually triggered
    
    # Conditional expression with actual relevance
    adjustment = 7 if len(sequence) > 5 else 3
    
    # Real key computation
    cumulative = 0
    for val in sequence:
        if val % 4 == 0:
            cumulative += val // 4
        else:
            cumulative -= val % 4
    
    # Final result built from multiple steps
    result = (cumulative + temp) + adjustment
    
    # Dead comparison (looks important but isn't)
    status_flag = "CRITICAL" if result < 0 else "NORMAL"
    
    return result

# Main execution
raw_input = [12, 15, 24, 7, 36, 19, 44]
processed = preprocess_signal(raw_input)

# Unused derived values (distractors)
decoded = [x ^ 15 for x in processed]
baseline_offset = sum(decoded) % 17

# Simulated threshold from irrelevant logic
threshold = len(processed) * 2 if sum(processed) > 300 else len(processed) + 3

# Actual signal pattern used in analysis
logic_sequence = [x % 13 for x in processed]

# Unused diagnostic branches
if threshold > 10:
    phase_code = 5
else:
    phase_code = 9

# Key statement containing answer
final_diagnostic = analyze_pattern(logic_sequence, threshold)

# Print required output
print(f"Result: {final_diagnostic}")