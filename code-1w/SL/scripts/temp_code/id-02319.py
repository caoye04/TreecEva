import itertools

# Simulated sensor data processing with diagnostic analysis
raw_readings = [14, 7, 22, 9, 3, 18, 5, 11, 16, 8]

def preprocess(data):
    # Irrelevant transformation (distractor)
    normalized = [x / max(data) for x in data]
    scaled = [int(x * 100) for x in normalized]
    return scaled

def generate_combinations(values):
    # Distractor: generates unused combinations
    combo_store = []
    for r in range(2, 4):
        combo_store.extend(list(itertools.combinations(values, r)))
    return combo_store  # Never used

def filter_outliers(seq, limit):
    # Real but indirect preprocessing step
    return [x for x in seq if x > limit]

def shift_cipher(sequence, key):
    # Misleading cryptographic-looking function (not actually affecting result)
    shifted = [(x + key) % 25 for x in sequence]
    return shifted

def compute_entropy(data):
    # Complex distractor with no impact on final answer
    from collections import Counter
    counts = Counter(data)
    total = len(data)
    entropy = 0.0
    for count in counts.values():
        p = count / total
        entropy -= p * (p ** 0.5)  # Not real entropy, but looks plausible
    return round(entropy, 4)

def transform_sequence(arr):
    # Core relevant logic: reverse and apply conditional increment
    temp = []
    for i, val in enumerate(reversed(arr)):
        if i % 2 == 0:
            temp.append(val + 2)
        else:
            temp.append(val - 1)
    return temp

def analyze_pattern(signal, cutoff):
    # Key function: computes sum of values above cutoff
    filtered = [x for x in signal if x >= cutoff]
    aggregate = sum(filtered)
    # Additional irrelevant computation (red herring)
    avg_val = sum(signal) / len(signal) if signal else 0
    peak = max(signal) if signal else 0
    # Final decision logic
    if aggregate > 50:
        return aggregate + int(avg_val)
    else:
        return aggregate - int(peak)

# Main execution flow
processed = preprocess(raw_readings)

# Dead code path 1: combination generation (unused)
decoy_combos = generate_combinations(processed)

# Dead code path 2: outlier filtering with unused result
spurious_filter = filter_outliers(processed, 20)

# Dead code path 3: cipher transformation (no effect)
ciphered = shift_cipher(processed, 7)

# Dead code path 4: entropy calculation (distractor metric)
entropy_score = compute_entropy(ciphered)

# Actual relevant data path
intermediate_data = transform_sequence(raw_readings)
threshold = 15

# Critical statement
final_diagnostic = analyze_pattern(intermediate_data, threshold)

print(f"Result: {final_diagnostic}")