import math

# Irrelevant helper function (dead code path)
def unused_checksum(data):
    return sum(data) % 256

# Misleading signal generator with decoy logic
def generate_noise(length, seed=42):
    result = []
    for i in range(length):
        val = (seed * i + 17) % 100
        if val % 3 == 0:
            val = math.sqrt(val) if val > 0 else 0
        result.append(val * 0.1)
    return result

# Distractor: fake filter that's never used
def deprecated_filter(x):
    return [i for i in x if i > 0.5]

# Real data preprocessor with embedded red herrings
def preprocess_signal(raw_sequence):
    temp_offset = 0.0
    scaling_factor = 1.0
    
    # Irrelevant normalization branch (never taken due to input)
    if len(raw_sequence) > 1000:
        scaling_factor = 0.1
        temp_offset = sum(raw_sequence) / len(raw_sequence)
    
    # Actual relevant transformation
    cleaned = []
    for x in raw_sequence:
        adjusted = x - 0.5  # Center around zero
        if abs(adjusted) < 0.1:
            adjusted = 0.0
        cleaned.append(round(adjusted * 2, 3))
    
    # Dead computation - looks important but doesn't affect output
    magnitude = sum([abs(c) for c in cleaned])
    avg_magnitude = magnitude / len(cleaned) if cleaned else 0
    
    # Return only what's needed
    return cleaned

# Auxiliary diagnostic (decoy usage)
def compute_entropy(data):
    from collections import Counter
    counts = Counter([round(d, 1) for d in data])
    total = len(data)
    entropy = 0.0
    for count in counts.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 4)

# Core analysis with conditional expression and hidden logic chain
def analyze_signal(processed_data):
    # Key intermediate values
    peak = max(processed_data, default=0)
    trough = min(processed_data, default=0)
    span = peak - trough
    
    # Complex conditional with nested logic
    base_score = span * 100 if span >= 0.5 else span * 50
    
    # Additional signal features (some irrelevant)
    zero_crossings = 0
    prev = processed_data[0] if processed_data else 0
    for val in processed_data[1:]:
        if prev < 0 <= val or prev > 0 >= val:
            zero_crossings += 1
        prev = val
    
    # Decoy weighting (unused)
    if zero_crossings > 10:
        adjustment = 1.2
    elif zero_crossings > 5:
        adjustment = 1.1
    else:
        adjustment = 0.9
    
    # Hidden key logic: count how many values are exactly integer multiples of 0.25
    precision_hits = 0
    for val in processed_data:
        if abs(val) > 0:
            normalized = abs(val) / 0.25
            if abs(normalized - round(normalized)) < 1e-6:
                precision_hits += 1
    
    # Final computation - only precision_hits and base_score matter
    # All other computed variables are distractors
    final_diagnostic = int(base_score + precision_hits * 10)
    
    # Critical execution point
    return final_diagnostic

# Irrelevant global constants
data_limit = 10000
threshold_config = {'level': 'high', 'tolerance': 0.05}

# Main execution flow
if __name__ == "__main__":
    # Generate initial sequence using simple deterministic rule
    raw_input = [0.1 * i for i in range(1, 11)]  # [0.1, 0.2, ..., 1.0]
    
    # Process through pipeline
    processed_data = preprocess_signal(raw_input)
    
    # Perform final analysis
    final_diagnostic = analyze_signal(processed_data)
    
    # Output result
    print(f"Result: {final_diagnostic}")