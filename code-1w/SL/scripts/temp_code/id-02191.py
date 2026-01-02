def analyze_signal(pattern):
    if not pattern:
        return 0
    transformed = [((x >> 1) ^ (x << 2)) & 255 for x in pattern]
    checksum = sum(transformed) % 100
    normalized = [x / (checksum + 1e-8) for x in transformed]
    return sum(int(n * 100) for n in normalized[:10])


def validate_input(data_str):
    if len(data_str) < 5:
        return False
    valid_chars = all(c.isalnum() or c in '_-' for c in data_str)
    has_digit = any(c.isdigit() for c in data_str)
    return valid_chars and has_digit


def compute_entropy(values):
    from math import log2
    freq_map = {}
    for v in values:
        freq_map[v] = freq_map.get(v, 0) + 1
    total = len(values)
    entropy = 0.0
    for count in freq_map.values():
        p = count / total
        entropy -= p * log2(p) if p > 0 else 0
    return round(entropy, 6)


def extract_features(raw_data):
    segments = raw_data.split('|')
    feature_vector = []
    for seg in segments:
        cleaned = seg.strip().upper().replace('X', '')
        if cleaned.startswith('Z'):
            continue
        length_score = len(cleaned) * 2
        vowel_count = sum(1 for c in cleaned if c in 'AEIOU')
        feature_vector.append(length_score + vowel_count)
    return feature_vector


def filter_outliers(scores, threshold=75):
    mean_val = sum(scores) / len(scores)
    deviations = [(s - mean_val) ** 2 for s in scores]
    variance = sum(deviations) / len(deviations)
    std_dev = variance ** 0.5
    return [s for s in scores if abs(s - mean_val) <= 2 * std_dev], std_dev


def evaluate_performance(metrics, min_limit):
    temp_results = {}
    
    # Irrelevant preprocessing block (distractor)
    alt_path = [x * 1.5 for x in metrics if x % 3 == 0]
    if len(alt_path) > 5:
        smoothing_factor = 0.85
    else:
        smoothing_factor = 1.15
    
    # Key transformation
    processed = [((x ** 2) + 10) // 3 for x in metrics]
    
    # Another red herring: complex conditional that doesn't affect outcome
    status_flags = []
    for val in processed:
        if val > 100:
            status_flags.append(1)
        elif val < 20:
            status_flags.append(-1)
        else:
            status_flags.append(0)
    
    # Decoy function call with no side effects
    _ = compute_entropy(processed)
    
    # Core logic buried in distractions
    adjusted = []
    for i, p in enumerate(processed):
        modifier = 1.2 if i % 4 == 0 else (0.9 if i % 5 == 0 else 1.0)
        adjusted.append(p * modifier)
    
    # Dead code path (never reached due to prior filtering)
    if any(x < 0 for x in adjusted):
        fallback = sum(abs(x) for x in adjusted)
        return fallback // 10
    
    # Actual critical computation
    filtered_adjusted, spread = filter_outliers(adjusted, threshold=min_limit)
    base_score = sum(filtered_adjusted)
    penalty = int(spread * 10)
    final_score = int(base_score - penalty)
    
    # Unused but misleading intermediate
    diagnostic_code = f"D{len(filtered_adjusted)}S{penalty}V{sum(status_flags)}"
    
    return final_score

# Simulated sensor data ingestion (realistic context)
data_stream = "A3B|XXC7|D9|E11|F4C|G6H|ZSKIP|I2J|R8M"

# Step 1: Extract features from stream
feature_list = extract_features(data_stream)

# Step 2: Analyze bit-level signal pattern (distractor with partial relevance)
signal_pattern = [len(feature_list), 42, 255, 128, 64, 32, 16]
analysis_result = analyze_signal(signal_pattern)

# Step 3: Generate metric data through multiple transformations
metric_data = [x * 3 + analysis_result // 10 for x in feature_list]

# Step 4: Validate dummy ID (irrelevant but plausible)
user_id = "ABCD1234"
is_valid = validate_input(user_id)

# Step 5: Main evaluation with hidden logic
base_threshold = 50
final_score = evaluate_performance(metric_data, base_threshold)

print(f"Result: {final_score}")