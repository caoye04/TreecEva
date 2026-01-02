def preprocess_signals(raw_input, threshold=0.7):
    filtered = [x for x in raw_input if abs(x) > threshold]
    normalized = [(x - min(filtered)) / (max(filtered) - min(filtered)) for x in filtered]
    return [round(val, 3) for val in normalized]


def generate_baseline(size):
    base = []
    for i in range(size):
        base.append((i * 0.1) % 1.0)
    return [round(b, 3) for b in base]


def shift_sequence(seq, offset):
    return seq[offset:] + seq[:offset]


def evaluate_coherence(data):
    score = 0
    for i in range(len(data) - 1):
        if data[i] < data[i+1]:
            score += 1
    return score / (len(data) - 1) if len(data) > 1 else 0


def analyze_patterns(dataset, reference):
    intersection = set(dataset) & set(reference)
    symmetric_diff = set(dataset) ^ set(reference)
    
    # Irrelevant transformations
    temp_shifted = shift_sequence(reference, 3)
    _ = [x * 1.5 for x in temp_shifted if x < 0.5]  # dead computation
    
    coherence_main = evaluate_coherence(dataset)
    coherence_ref = evaluate_coherence(reference)
    
    # Decoy metrics
    mean_deviation = abs(sum(dataset) / len(dataset) - sum(reference) / len(reference))
    _ = mean_deviation * 2  # unused distraction
    
    # Core logic disguised among noise
    overlap_score = len(intersection) * 100
    divergence_penalty = len(symmetric_diff) * 10
    adjustment_factor = int(coherence_main * 50) - int(coherence_ref * 30)
    
    # Misleading intermediate that looks important
    pseudo_entropy = 0
    seen = set()
    for x in dataset:
        if x not in seen:
            pseudo_entropy += 1
            seen.add(x)
    _ = pseudo_entropy * 0.1  # decoy usage
    
    result = overlap_score - divergence_penalty + adjustment_factor
    return int(result)

# Main execution flow
sensor_readings = [0.15, 0.82, 0.33, 0.91, 0.67, 0.24, 0.76, 0.55, 0.43, 0.88]

# Irrelevant preprocessing branch
_ = preprocess_signals(sensor_readings, threshold=0.2)  # not used later

# Actual relevant data path
cleaned_signals = preprocess_signals(sensor_readings, threshold=0.6)
baseline_reference = generate_baseline(len(cleaned_signals))

# Multiple transformations with red herrings
transformed_data = []
for idx, val in enumerate(cleaned_signals):
    if idx % 2 == 0:
        transformed_data.append(round(val * 1.2, 3))
    else:
        transformed_data.append(round(val * 0.85, 3))

# Dead code block — visually significant but irrelevant
historical_weights = [0.1, 0.3, 0.4, 0.2]
decay_factor = 0.9
for i in range(5):
    historical_weights = [w * decay_factor for w in historical_weights]
    total_weight = sum(historical_weights)

# Key statement
final_diagnostic = analyze_patterns(transformed_data, baseline_reference)

print(f"Result: {final_diagnostic}")