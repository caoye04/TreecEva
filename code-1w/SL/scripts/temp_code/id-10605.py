def analyze_metrics(entries):
    totals = [0] * len(entries[0])
    counts = [0] * len(entries[0])

    for entry in entries:
        for i, val in enumerate(entry):
            if val > 0:  # Only consider positive metrics
                totals[i] += val
                counts[i] += 1

    averages = [totals[i] / counts[i] if counts[i] > 0 else 0 for i in range(len(totals))]
    return averages


def calculate_redundant_factor(data):
    # Irrelevant computation - distractor
    factor = 1
    for row in data:
        for elem in row:
            factor = (factor * (elem % 7 + 1)) % 97
    return factor


def track_state_history(values):
    # Dead code path - never used
    history = []
    state = 0
    for idx, v in enumerate(values):
        if idx % 2 == 0:
            state += v ** 0.5
        else:
            state -= v // 3
        history.append(state)
    return history


def calculate_performance(raw_data):
    processed = analyze_metrics(raw_data)
    
    # Misleading normalization step (not actually affecting final score)
    normalized = [round(p * 0.85, 4) for p in processed]
    
    # Key logic: compute weighted sum based on position
    weights = [0.2, 0.3, 0.5]
    weighted_sum = sum(processed[i] * weights[i] for i in range(len(processed)))
    
    # Secondary adjustment based on pattern detection
    patterns_detected = 0
    for i in range(1, len(processed)):
        if processed[i] > processed[i-1]:
            patterns_detected += 1
    
    adjustment = 1.0 + (patterns_detected * 0.05)
    adjusted_score = weighted_sum * adjustment
    
    # Red herring: complex but unused calculation
    zipped_data = list(zip(raw_data[0], raw_data[1], raw_data[2]))
    derived_flags = [any(z > 10 for z in triplet) for triplet in zipped_data]
    flag_influence = sum(1 for f in derived_flags if f) * 0.01
    
    # Final score computed here — this is the answer
    final_score = round(adjusted_score + 0.5, 2)
    
    # Print result as required
    print(f"Result: {final_score}")
    return final_score

# Input data
benchmark_data = [
    [5, 12, 8],
    [7, 10, 15],
    [6, 14, 11]
]

# Unused helper — distractor
def validate_entry(entry):
    return all(isinstance(x, int) and x >= 0 for x in entry)

# Trigger execution
final_score = calculate_performance(benchmark_data)