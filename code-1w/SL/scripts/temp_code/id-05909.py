from collections import defaultdict, Counter
import itertools

# Simulate sensor data aggregation in a distributed monitoring system
def collect_sensor_readings():
    readings = [102, 95, 110, 97, 108, 103, 99, 111]
    metadata_map = defaultdict(list)
    for i, val in enumerate(readings):
        metadata_map[f'sensor_{i % 4}'].append(val)
    return dict(metadata_map)

# Irrelevant helper: counts digit occurrences (distractor)
def count_digits(numbers):
    digit_freq = Counter()
    for n in numbers:
        for digit in str(n):
            digit_freq[digit] += 1
    return digit_freq

# Dead function – never called
def legacy_normalization(data):
    mean_val = sum(data) / len(data)
    return [round((x - mean_val) / mean_val * 100, 2) for x in data]

# Bit manipulation decoy: looks important but unused later
def obfuscate_key(value):
    key = value ^ 255
    key = (key << 2) & 0xFF
    key ^= (value >> 1)
    return key

# Another red herring: complex transformation with no downstream use
def compute_entropy(arr):
    freq = Counter(arr)
    total = len(arr)
    entropy = 0.0
    for count in freq.values():
        p = count / total
        entropy -= p * (p ** 0.5)  # Not actual entropy, just mimic complexity
    return round(entropy, 6)

# Core logic disguised among noise
def extract_critical_metrics(sensor_dict):
    flattened = []
    for k, v in sensor_dict.items():
        if 'sensor_1' in k or 'sensor_3' in k:
            flattened.extend([x for x in v if x > 100])
        elif 'sensor_2' in k:
            flattened.extend([x for x in v if x < 105])
    return flattened

# Comparison filter with short-circuit logic distraction
def apply_thresholds(values, low=95, high=110):
    result = []
    for v in values:
        # Complex condition with misleading parentheses
        if (v >= low and not (v > high)) or ((v > high) and (v % 2 == 0 and True)):
            result.append(v)
        else:
            pass  # Explicit noop to suggest something might be missing
    return result

# Real computation path hidden behind decoys
def calculate_baseline(metrics):
    temp_store = []
    for x in metrics:
        temp_store.append(x * 1.5)  # Actual transformation
    avg = sum(temp_store) / len(temp_store)
    return int(avg)  # Critical baseline

# Misleading XOR-based checksum (unused)
def generate_checksum(data):
    chk = 0
    for d in data:
        chk ^= (d + 13) & 0xF
    return chk

# Main evaluation logic that actually matters
def evaluate_performance(metrics, base):
    # Use itertools to create combinations (looks complex but has purpose)
    pairs = list(itertools.combinations(metrics, 2))
    diffs = [abs(a - b) for a, b in pairs]
    avg_diff = sum(diffs) / len(diffs)

    # Real calculation: ratio-based score
    raw_score = (avg_diff * 100) / base

    # Final adjustment using bitwise AND (actually used)
    final_part = int(raw_score) & 0xFFFF  # Mask out higher bits, still large int

    return final_part

# --- Execution Flow ---
data_pool = collect_sensor_readings()

# Distractor calls (no side effects)
digit_analysis = count_digits([102, 95, 110, 97, 108])
entropy_value = compute_entropy([102, 95, 110, 108])

# Real pipeline begins here
filtered_metrics = extract_critical_metrics(data_pool)
applied_values = apply_thresholds(filtered_metrics)
baseline = calculate_baseline(applied_values)

# Key statement
final_score = evaluate_performance(applied_values, baseline)

# Print target result
print(f"Target result: {final_score}")