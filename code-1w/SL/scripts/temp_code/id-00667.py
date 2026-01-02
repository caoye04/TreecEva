import itertools

# Sensor network diagnostic simulation with noise filtering and anomaly detection

def collect_sensor_data():
    raw_readings = [
        (101, 23.4, 1), (102, 24.1, 0), (103, 22.8, 1), (104, 25.6, 1),
        (105, 19.3, 0), (106, 26.7, 1), (107, 20.2, 1), (108, 27.1, 0),
        (109, 28.3, 1), (110, 21.9, 1)
    ]
    return raw_readings

# Irrelevant helper - dead code path (distractor)
def legacy_calibrate(x):
    return (x * 1.02) + 0.5 if x < 25 else (x * 0.98) - 0.3

# Unused transformation chain (red herring)
def transform_sequence(seq):
    acc = 0
    transformed = []
    for i, val in enumerate(seq):
        if i % 2 == 0:
            acc += val ** 0.5
        else:
            acc -= val / 2
        transformed.append(acc * 1.1)
    return [round(t, 2) for t in transformed]

# Decoy function that looks important but is never called
def compute_aggregate_integrity(data_list):
    checksum = 0
    for item in data_list:
        sensor_id, temp, status = item
        checksum ^= int(temp * 10)
        checksum = (checksum + sensor_id) % 97
    return checksum * len(data_list)

# Real processing begins here
sensor_data = collect_sensor_data()

# Extract temperatures and statuses using zip (relevant)
temperatures = [t for _, t, _ in sensor_data]
statuses = [s for _, _, s in sensor_data]

# Create enumerated index map (partially relevant)
index_map = {i: temp for i, temp in enumerate(temperatures)}

# Apply moving average filter (3-point) - relevant preprocessing
smoothed = []
for i in range(1, len(temperatures) - 1):
    avg = (temperatures[i-1] + temperatures[i] + temperatures[i+1]) / 3
    smoothed.append(round(avg, 2))

# Misleading intermediate statistic (distractor)
spike_count = sum(1 for i in range(1, len(temperatures)) if abs(temperatures[i] - temperatures[i-1]) > 3.0)

# Generate all pairwise temperature differences (overkill - distractor)
pair_diffs = list(itertools.combinations(temperatures, 2))
avg_pair_gap = round(sum(abs(a - b) for a, b in pair_diffs) / len(pair_diffs), 2)

# Real filtering: find readings where temp > 25 and status active
filtered_data = [(sid, t, s) for sid, t, s in sensor_data if t > 25.0 and s == 1]

# Build threshold map using set logic on indices (relevant)
high_temp_indices = {i for i, t in enumerate(temperatures) if t > 25.0}
active_status_indices = {i for i, s in enumerate(statuses) if s == 1}
valid_indices = high_temp_indices & active_status_indices  # Set intersection

threshold_map = {}
base_threshold = 25.5
for idx in sorted(valid_indices):
    adjustment = 0.3 if idx % 2 == 0 else -0.2
    threshold_map[idx] = base_threshold + adjustment
    base_threshold += 0.1  # Drift over time

# Secondary decoy structure (unused)
status_transitions = []
for i in range(1, len(statuses)):
    if statuses[i] != statuses[i-1]:
        status_transitions.append((i-1, i, statuses[i-1], statuses[i]))

# Core processing function (called once)
def process_readings(readings, thresholds):
    results = []
    # Simulate multi-stage diagnostic
    stage1 = {sid: round((temp - 20) * 2) for sid, temp, s in readings}
    
    # Introduce bit manipulation for 'health score' (relevant)
    for (sid, temp, s), (idx, thresh) in zip(readings, enumerate(thresholds.values())):
        raw_score = int(temp * 2)
        masked = raw_score & 63  # Keep low 6 bits
        shifted = masked >> 2
        parity = bin(shifted).count('1') % 2
        fused = (shifted ^ int(thresh)) | (parity << 5)
        results.append(fused)
    
    # Final aggregation
    cumulative = 0
    for r in results:
        cumulative = (cumulative * 1.1) + r  # Weighted accumulation
    
    # Dead calculation branch inside function (distractor)
    if len(results) > 10:
        backup = sum(results) / len(results)
    else:
        backup = sum(r ** 0.5 for r in results)  # Never used
    
    return int(round(cumulative))

# Key statement
final_diagnostic = process_readings(filtered_data, threshold_map)

# Output result
print(f"Result: {final_diagnostic}")