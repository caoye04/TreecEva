import itertools

# Simulated sensor data processing with embedded diagnostics
def collect_readings():
    raw_sequence = [i ** 2 for i in range(15) if i % 3 != 0]
    offset = sum([1 for _ in itertools.islice(itertools.count(7), 5)])  # red herring: computes 5, unused later
    return [x + offset for x in raw_sequence]

# Irrelevant transformation chain (dead path)
def deprecated_filter(data):
    return [x for x in data if x > 10 and x % 2 == 0]

# Distractor function: looks important but not used in main logic
def compute_legacy_checksum(arr):
    checksum = 0
    for i, val in enumerate(arr):
        checksum ^= (val * i) % 17
    return checksum

# Real preprocessing with conditional expression
def preprocess(signal):
    cleaned = [x for x in signal if x % 4 == 0 or x < 50]
    # Apply gain only if above threshold, else leave unchanged
    amplified = [val * (1.5 if val < 30 else 1) for val in cleaned]
    return [int(x) for x in amplified]

# Recursive frequency counter (core logic)
def count_frequency_recursive(lst, index=0, acc=None):
    if acc is None:
        acc = {}
    if index == len(lst):
        return acc
    key = lst[index]
    acc[key] = acc.get(key, 0) + 1
    return count_frequency_recursive(lst, index + 1, acc)

# Signal analyzer using itertools.groupby (key operation)
def analyze_signal(data):
    sorted_data = sorted(data)
    groups = [list(group) for k, group in itertools.groupby(sorted_data)]
    
    # Misleading intermediate calculation
    phantom_moment = sum([len(g) * g[0] for g in groups if len(g) > 2]) // 3 if any(len(g) > 2 for g in groups) else 0
    
    # Actual diagnostic logic
    freq_map = count_frequency_recursive(data)
    peak_values = [k for k, v in freq_map.items() if v >= 2]
    modulation_index = sum(peak_values) if peak_values else -1
    
    # Secondary check using conditional expression
    base_reference = 42 if modulation_index > 50 else 24
    
    # Final computation
    diagnostic_score = modulation_index * base_reference // (len(peak_values) or 1)
    
    # Dead code branch (never executed due to condition)
    if False and diagnostic_score > 100:
        backup_system = [diagnostic_score >> 2 for _ in range(3)]
        diagnostic_score += sum(backup_system)
    
    return diagnostic_score

# Unused helper: adds confusion
def generate_synthetic_sample(n):
    return [(i * 7) % 101 for i in range(n)]

# Main execution flow
if __name__ == "__main__":
    readings = collect_readings()
    processed_data = preprocess(readings)
    
    # Red herring variables
    temp_analysis = deprecated_filter(processed_data)
    legacy_hash = compute_legacy_checksum(temp_analysis)
    synthetic_test = generate_synthetic_sample(10)
    
    final_diagnostic = analyze_signal(processed_data)
    print(f"Result: {final_diagnostic}")