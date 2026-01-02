from collections import defaultdict, Counter

# Simulated system telemetry data
telemetry_stream = [
    (100, 'temp', 75.3), (101, 'cpu', 82.1), (102, 'temp', 68.9),
    (103, 'disk', 91.2), (104, 'temp', 77.4), (105, 'cpu', 85.0),
    (106, 'temp', 70.2), (107, 'net', 44.8), (108, 'temp', 78.1)
]

# Parse raw stream into structured logs
temp_log = []
cpu_log = []
disk_log = []
base_offset = 100
scale_factor = 1.05

for entry in telemetry_stream:
    seq, sensor_type, reading = entry
    adjusted_seq = seq - base_offset
    scaled_reading = reading * scale_factor
    
    if sensor_type == 'temp':
        temp_log.append(scaled_reading)
    elif sensor_type == 'cpu':
        cpu_log.append(scaled_reading)
    elif sensor_type == 'disk':
        disk_log.append(scaled_reading)

# Misleading diagnostic: average CPU usage above threshold
high_cpu_count = 0
cpu_average = sum(cpu_log) / len(cpu_log) if cpu_log else 0
for val in cpu_log:
    if val > 80:
        high_cpu_count += 1

# Irrelevant statistical moment calculation (distractor)
cpu_variance = 0
if len(cpu_log) > 1:
    mean_cpu = cpu_average
    cpu_variance = sum((x - mean_cpu) ** 2 for x in cpu_log) / len(cpu_log)

# Dead code path: network packet analysis (unused)
packet_stats = defaultdict(int)
for entry in telemetry_stream:
    _, s_type, _ = entry
    packet_stats[s_type] += 1
    if s_type == 'net':
        # Simulate checksum (never used)
        raw_val = entry[2]
        checksum = int(raw_val * 100) ^ 0xFF

# Unused helper function (red herring)
def analyze_packet_flow(packets):
    flow_summary = Counter()
    for p_type in packets:
        flow_summary[p_type] += 1
    return flow_summary

# Another distraction: hypothetical disk degradation model
disk_wear_level = 0
for usage in disk_log:
    if usage > 90:
        disk_wear_level += (usage - 90) * 1.5

# Core logic: temperature trend analysis with conditional weighting
def process_metrics(temps, threshold):
    if not temps:
        return 0
    
    # Compute moving differences
    diffs = [temps[i+1] - temps[i] for i in range(len(temps)-1)]
    rising_trend = sum(1 for d in diffs if d > 0)
    falling_trend = sum(1 for d in diffs if d < 0)
    
    # Apply conditional weights based on trend dominance
    trend_score = rising_trend - falling_trend
    base_threshold = threshold * 1.05
    
    # Use conditional expression for dynamic adjustment
    adjustment = 1.2 if trend_score > 0 else 0.8
    
    avg_temp = sum(temps) / len(temps)
    
    # Secondary check: detect oscillation pattern
    oscillations = 0
    for i in range(1, len(diffs)):
        if diffs[i-1] * diffs[i] < 0:  # sign change
            oscillations += 1
    
    # Oscillation penalty
    oscillation_factor = 0.9 if oscillations >= 2 else 1.0
    
    # Final diagnostic combines average, trend, and stability
    diagnostic_value = (avg_temp + trend_score * adjustment) * oscillation_factor
    
    # Normalize against base reference (derived from sequence logic)
    sequence_span = len(temps)
    normalization_base = sequence_span if sequence_span > 3 else 1
    normalized_diagnostic = diagnostic_value / normalization_base
    
    return int(round(normalized_diagnostic))

# Misleading intermediate: peak detection (not used in final result)
peak_temp = max(temp_log) if temp_log else 0
recent_spikes = [t for t in temp_log if t > 77]

# Key execution point
base_threshold = 75
final_diagnostic = process_metrics(temp_log, base_threshold)

# Output target result
print(f"Result: {final_diagnostic}")