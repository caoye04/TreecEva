def analyze_segments(data, threshold=0.75):
    """Irrelevant helper function for signal analysis."""
    anomalies = []
    for i, val in enumerate(data):
        if val > threshold * max(data):
            anomalies.append(i)
    return sorted(anomalies, reverse=True)


def compute_safety_margin(x, y):
    """Unused safety calculation."""
    return (x ** 2 + y ** 2) ** 0.5

# Simulated sensor data stream
temperature_readings = [23.5, 24.1, 22.8, 25.6, 26.7, 24.3, 23.9]
humidity_levels = [45, 48, 50, 55, 60, 52, 47]
pressure_samples = [1013, 1015, 1012, 1010, 1008, 1011, 1014]

# Distractor: complex but unused transformation chain
transformed = list(zip(
    [t * 1.8 + 32 for t in temperature_readings],
    humidity_levels,
    [round(p / 1013.25, 4) for p in pressure_samples]
))
analyzed_indices = analyze_segments(humidity_levels, 0.8)

# Core system state flags
system_modes = ['active', 'standby', 'active', 'fault', 'active', 'active', 'standby']
quality_flags = [1 if mode == 'active' else 0 for mode in system_modes]

# Performance counters with red herring computations
raw_counters = [100, 150, 200, 0, 300, 250, 180]
adjusted_counters = []
for idx, (raw, flag) in enumerate(zip(raw_counters, quality_flags)):
    if flag == 0:
        adjusted_counters.append(0)
    else:
        adjusted = raw * (0.95 + idx * 0.01)
        adjusted_counters.append(round(adjusted, 2))

# Unused bit manipulation decoy
bitmask = 0
for val in raw_counters:
    bitmask ^= int(val) << 1

# Critical data alignment using enumerate and zip
performance_data = []
for i, (counter, temp) in enumerate(zip(adjusted_counters, temperature_readings)):
    if quality_flags[i] == 1:
        score = counter * (1 + (temp - 24.0) / 100)
        performance_data.append(round(score, 3))

# Ghost variables - look important but unused in final result
diagnostic_trace = set()
for i, score in enumerate(performance_data):
    if score > 200:
        diagnostic_trace.add(f"HIGH_PERF_{i}")

baseline_ref = sum(temperature_readings) / len(temperature_readings)
reference_vector = [round(baseline_ref + i * 0.1, 2) for i in range(7)]

# Decoy aggregation functions
def aggregate_legacy(data_list):
    return sum(d * 0.8 for d in data_list if d > 100)

def calculate_robust_mean(values):
    sorted_vals = sorted(values)
    return sum(sorted_vals[1:-1]) / len(sorted_vals[1:-1])

# Real processing function buried among distractions
def process_metrics(flags, perf):
    total_weight = 0
    cumulative = 0
    
    # Multi-step weighted accumulation
    for index, (flag, value) in enumerate(zip(flags, perf)):
        if flag != 1:
            continue
        weight = 1 + (index % 3) * 0.5  # Weighting pattern
        intermediate = value * weight
        
        # Conditional boosting
        if index > 0 and perf[index-1] < value:
            intermediate *= 1.1
            
        cumulative += intermediate
        total_weight += weight
    
    if total_weight == 0:
        return 0
    
    final_avg = cumulative / total_weight
    
    # Final adjustment based on pattern in flags
    active_count = sum(flags)
    if active_count >= 4:
        final_avg += 10.0
    
    return round(final_avg, 3)

# Execution point of interest
final_score = process_metrics(quality_flags, performance_data)
print(f"Result: {final_score}")