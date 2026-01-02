import math

def analyze_readings(readings):
    cumulative_score = 0
    temp_offset = 0
    for r in readings:
        if r < 50:
            cumulative_score += r * 1.2
        elif r < 100:
            cumulative_score += r * 0.9
        else:
            temp_offset += r // 10  # Irrelevant accumulation
    return cumulative_score

def validate_structure(data):
    if len(data) < 5:
        return False
    checksum = sum(d * (i+1) for i, d in enumerate(data)) % 17
    return checksum == 3

def filter_anomalies(records):
    anomalies = set()
    for i, record in enumerate(records):
        if record % 13 == 0:
            anomalies.add(i)
    cleaned = [r for i, r in enumerate(records) if i not in anomalies]
    return cleaned  # Dead code path: result not used in main logic

def compute_entropy(values):
    freq_map = {}
    for v in values:
        freq_map[v] = freq_map.get(v, 0) + 1
    total = len(values)
    entropy = 0.0
    for count in freq_map.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 6)

def process_metrics(data, limits):
    # Key processing begins
    subset = data[2:9:2]  # Slicing: elements at index 2,4,6,8
    offset = len(data) - len(limits)
    adjusted = [x - offset for x in subset]

    # Red herring: complex but unused transformation
    transformed = []
    for x in adjusted:
        if x > 25:
            transformed.append(int(math.sqrt(x) * 3))
        else:
            transformed.append(x ** 1.5)

    # Relevant computation chain
    base_value = analyze_readings(adjusted)
    validation_flag = validate_structure(adjusted)

    intermediate = base_value / 2
    if validation_flag:
        intermediate += 17

    # Dictionary-based threshold mapping
    threshold_map = {k: v * 1.1 for k, v in enumerate(limits)}
    surge_correction = 0
    for i in range(len(threshold_map)):
        if i % 2 == 0:
            surge_correction += threshold_map[i] * 0.1

    # Decoy entropy calculation with side-effect-free function
    _ = compute_entropy(data)
    _ = compute_entropy(limits)

    # Final computation
    scaling_factor = 1.0
    if len(adjusted) > 3:
        scaling_factor *= 1.3
    final_diagnostic = int(intermediate * scaling_factor - surge_correction)

    # Critical assignment point
    return final_diagnostic

# Main execution block
health_data = [45, 88, 105, 49, 76, 134, 68, 92, 110, 58]
thresholds = [20, 25, 30, 35, 40]

# Unused variables and misleading initializations
baseline_reference = sum(health_data) // len(health_data)
diagnostic_log = []
consistency_check = False

# Core statement
final_diagnostic = process_metrics(health_data, thresholds)

# Output result
print(f"Result: {final_diagnostic}")