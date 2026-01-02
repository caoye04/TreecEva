import itertools

# Simulated sensor data preprocessing with red herrings
def preprocess_stream(raw_packets):
    checksum = 0
    processed = []
    for pkt in raw_packets:
        temp_val = (pkt ^ 0xAB) & 0xFF
        if temp_val % 3 == 0:
            checksum += temp_val
        processed.append(temp_val | 10)
    return processed, checksum

# Irrelevant audio processing decoy
def analyze_tone(frequency_seq):
    peak = max(frequency_seq)
    avg = sum(frequency_seq) / len(frequency_seq)
    return {'peak': peak, 'average': avg, 'deviation': peak - avg}

# Core transformation logic
transformer = lambda x: ((x >> 2) ^ 0x1F) + (x % 7)

raw_input = [120, 205, 67, 92, 150, 230, 45]

# Step 1: Preprocess input with side-effect checksum (distractor)
filtered_data, validation_sum = preprocess_stream(raw_input)

# Step 2: Apply transformation using lambda map
transformed_data = list(map(transformer, filtered_data))

# Step 3: Baseline calculation with irrelevant operations
baseline_candidate_1 = sum(transformed_data) // len(transformed_data)
baseline_candidate_2 = transformed_data[2] * 2 - 5
baseline = min(baseline_candidate_1, baseline_candidate_2)

# Step 4: Decoy function call with unused result
audio_analysis = analyze_tone([440, 320, 180, 510])

# Step 5: Generate auxiliary metrics (some used, some not)
aux_metrics = {
    'range': max(transformed_data) - min(transformed_data),
    'parity_count': len([x for x in transformed_data if x % 2 == 0]),
    'growth_rate': (transformed_data[-1] - transformed_data[0]) / len(transformed_data)
}

# Step 6: Anomaly detection with bit manipulation distraction
shift_accum = 0
for val in transformed_data:
    shift_accum ^= (val << 1) & 0xFF
anomaly_score = (shift_accum % 17) * 3.5  # Real contributor

# Step 7: Red herring statistical analysis
stat_flags = []
for i, val in enumerate(transformed_data):
    if val > baseline and i % 2 == 0:
        stat_flags.append(i * 2)

# Step 8: Aggregation using itertools.cycle to confuse control flow
aggregate_metrics = lambda data, base: sum(itertools.islice(itertools.cycle([abs(x - base) for x in data]), 0, len(data) * 2)) // 2

# Step 9: Critical assignment - target of reasoning
final_diagnostic = aggregate_metrics(transformed_data, baseline) + anomaly_score

# Step 10: Unused diagnostic path (dead code)
if final_diagnostic < 0:
    final_diagnostic = abs(final_diagnostic)
elif final_diagnostic > 1000:
    final_diagnostic = final_diagnostic // 3

# Output the result as required
print(f"Result: {final_diagnostic}")