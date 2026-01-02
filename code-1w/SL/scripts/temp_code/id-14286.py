import itertools

# Simulated sensor array data (real values)
data_stream = [107, 214, 153, 98, 241, 188, 132, 76, 305, 167, 110, 204]

def analyze_variance(sequence, window_size=3):
    """Irrelevant helper: computes moving variance (not used in final result)"""
    variances = []
    for i in range(len(sequence) - window_size + 1):
        window = sequence[i:i+window_size]
        mean = sum(window) / window_size
        variance = sum((x - mean)**2 for x in window) / window_size
        variances.append(round(variance, 3))
    return variances

def generate_checksum(signal):
    """Distraction function: computes XOR checksum (never called)"""
    checksum = 0
    for val in signal:
        checksum ^= (val * 3) % 256
    return checksum

# Distractor: complex-looking but unused data transformation
expanded_grid = [[x + 10*i for x in data_stream] for i in range(4)]
aggregated_metrics = list(map(lambda row: sum(row) // len(row), expanded_grid))

# Actual processing begins here
status_flags = [x > 100 for x in data_stream]  # Step 1: boolean tagging
paired_indices = list(enumerate(status_flags))  # Step 2: index-flag pairing

# Filter relevant indices where reading > 100
active_probes = [i for i, flag in paired_indices if flag]  # Step 3: extract active indices
filtered_data = [data_stream[i] for i in active_probes]  # Step 4: get corresponding readings

# Misleading intermediate calculation (dead end)
temp_analysis = [abs(x - 200) for x in filtered_data if x < 300]
adjustment_factor = sum(temp_analysis) / len(temp_analysis) if temp_analysis else 0  # distractor

# Real logic: count how many high readings are above median
median_reading = sorted(filtered_data)[len(filtered_data)//2]  # Step 5: find median
high_readings = list(filter(lambda x: x > median_reading, filtered_data))  # Step 6: filter above median

count_cycles = 0
for combo in itertools.combinations(high_readings, 2):  # Step 7: pairwise analysis
    if abs(combo[0] - combo[1]) > 50:
        count_cycles += 1  # Step 8: increment on significant difference

# Threshold logic based on dynamic condition
threshold_func = lambda x: x > (median_reading + 25)

# Final processing: apply threshold and compute diagnostic score
def process_readings(readings, threshold_fn):
    passed = [r for r in readings if threshold_fn(r)]  # Step 9: filter by dynamic threshold
    base_score = sum(passed)  # Step 10
    penalty = len(readings) - len(passed)  # Step 11
    return base_score - (penalty * 5)  # Step 12: final formula

final_diagnostic = process_readings(filtered_data, threshold_func)
print(f"Result: {final_diagnostic}")