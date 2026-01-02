import itertools

# Simulated sensor data processing with red herrings and complex flow
def collect_readings():
    raw_signals = [1, 2, 3, 4, 5]
    offset = 17
    scale_factor = 3
    processed = [(x * scale_factor + offset) % 11 for x in raw_signals]
    return processed

# Irrelevant transformation - decoy function
def encrypt_data(data):
    return [d ^ 255 for d in data[:3]]

# Unused but plausible helper
def validate_checksum(arr):
    return sum(arr) % 7 == 0

# Core transformation chain
def transform_signal(seq):
    shifted = [x << 1 for x in seq]  # Bit shift left
    filtered = list(filter(lambda x: x > 10, shifted))
    paired = list(itertools.combinations(filtered, 2))
    sums = [a + b for a, b in paired]
    return sorted(sums)[::2]  # Every other sum

# Misleading diagnostic path (dead end)
def compute_health_score(logs):
    baseline = 95.0
    penalty = 0
    for log in logs:
        if log < 20:
            penalty += 3.5
    return max(baseline - penalty, 0)

# Main analysis with critical nesting and distractors
def analyze_pattern(data):
    temp_buffer = []
    history = {"peak": 0, "count": 0}
    adjustment = 4

    for i in range(len(data)):
        if data[i] % 2 == 0:
            for j in range(i + 1, len(data)):
                diff = data[j] - data[i]
                if diff > 5:
                    entry = {
                        'index_pair': (i, j),
                        'diff': diff,
                        'product': data[i] * data[j]
                    }
                    temp_buffer.append(entry)

                    # Red herring update
                    if diff > 10:
                        history["peak"] = max(history["peak"], diff)
                        history["count"] += 1

    # Decoy aggregation
    dummy_agg = sum(entry['product'] for entry in temp_buffer) // len(temp_buffer) if temp_buffer else 0

    # Critical calculation hidden among distractions
    valid_differences = [entry['diff'] for entry in temp_buffer if entry['product'] > 30]
    if not valid_differences:
        return -1

    avg_diff = sum(valid_differences) / len(valid_differences)
    ceiling_value = int(avg_diff + 0.5)  # Round to nearest integer

    # Secondary adjustment based on combinatorics
    combo_count = len(list(itertools.permutations(valid_differences, 2)))
    if combo_count > 0:
        ceiling_value += (combo_count % 9)

    final_adjustment = 5
    result = ceiling_value * 3 - final_adjustment

    return result

# Orchestration with misleading setup
if __name__ == "__main__":
    # Real data pipeline
    signal_data = collect_readings()
    transformed_data = transform_signal(signal_data)

    # Fake security layer (unused)
    encrypted = encrypt_data(transformed_data)
    verified = validate_checksum(transformed_data)

    # Spurious health check
    score = compute_health_score(transformed_data)

    # Key execution point
    final_diagnostic = analyze_pattern(transformed_data)
    
    # Output required result
    print(f"Result: {final_diagnostic}")