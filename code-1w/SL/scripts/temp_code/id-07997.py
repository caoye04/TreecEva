def analyze_component(x, threshold=5):
    return x ** 2 if x > threshold else x + 3

# Irrelevant helper (distractor)
def unused_diagnostic(value):
    return bin(value)[2:].count('1')

# Misleading transformation chain
def transform_sequence(seq):
    temp = [s * 2 for s in seq if s % 2 == 0]
    processed = []
    for t in temp:
        if t < 10:
            processed.append(t ** 1.5)
        else:
            processed.append(t // 3)
    return processed  # Never used

# Simulates sensor drift compensation (red herring)
calibration_offset = sum([i * 0.1 for i in range(7)])
baseline_readings = [4, 6, 2, 8, 5]
adjusted = [r + calibration_offset for r in baseline_readings]

# Actual relevant data
raw_metrics = [3, 7, 4, 9, 6]

# Distractor: complex but unused bitwise cascade
def bit_cascade(val):
    step1 = val ^ 15
    step2 = step1 & 25
    step3 = step2 >> 2
    return step3 | 7

unused_results = [bit_cascade(n) for n in range(5)]

# Conditional expression embedded in mapping
processed_metrics = [
    analyze_component(x) + (10 if x % 2 == 0 else 5) for x in raw_metrics
]

# Tuple-based weight assignment (relevant)
weights = (0.8, 1.2, 0.9, 1.1, 1.0)
weighted_values = tuple(p * w for p, w in zip(processed_metrics, weights))

# Simulated redundancy check (irrelevant)
def crc_check(data):
    checksum = 0
    for item in data:
        checksum ^= int(item)
    return checksum % 17

crc_discard = crc_check(weighted_values)  # Dead end

# Core aggregation logic
benchmark_data = weighted_values  # Key assignment

def aggregate_performance(data):
    total = 0.0
    for idx, val in enumerate(data):
        if val > 10:
            total += val * 0.9
        else:
            total += val * 1.1
    # Final adjustment based on logical condition
    multiplier = 1.05 if sum(1 for v in data if v > 12) >= 2 else 0.95
    return total * multiplier  # Critical output

# Execution point of interest
final_score = aggregate_performance(benchmark_data)
print(f"Target result: {final_score}")