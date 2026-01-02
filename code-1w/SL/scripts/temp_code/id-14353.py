def preprocess_entry(entry):
    # Irrelevant transformation
    return (entry[0], entry[1] ** 0.5)


def validate_checksum(record):
    # Dead function: not used in main logic
    return sum(record) % 7 == 0

# Simulated sensor readings over time
timestamps = [100, 101, 102, 103, 104]
sensor_a = [85, 92, 88, 96, 89]
sensor_b = [76, 79, 85, 81, 88]
sensor_c = [201, 198, 205, 197, 203]

# Irrelevant scaling
scaled_a = [val * 1.05 for val in sensor_a]
scaled_b = [val + 2 for val in sensor_b]

# Distractor data structures
auxiliary_map = {i: chr(65 + (i % 26)) for i in range(5)}
dummy_matrix = [[i*j for j in range(4)] for i in range(4)]

# Real health indicators
health_logs = list(zip(timestamps, sensor_a, sensor_b, sensor_c))

# Thresholds for anomaly detection
thresholds = {
    'temp_high': 90,
    'voltage_critical': 200,
    'stability_window': 3,
    'min_readings': 4
}

# Misleading intermediate calculation
apparent_failure_rate = len([x for x in sensor_c if x > 200]) / len(sensor_c)

# Unused recursive helper
def calculate_entropy(data, depth=0):
    if depth >= 3 or len(data) == 0:
        return 0.0
    mid = len(data) // 2
    return 1 + calculate_entropy(data[:mid], depth + 1)

# Core analysis with red herrings
def analyze_system_state(logs, config):
    alert_count = 0
    recent_alerts = []
    
    # Nesting Level 1: Main loop
    for idx, entry in enumerate(logs):
        timestamp = entry[0]
        temp = entry[1]
        stability = entry[2]
        voltage = entry[3]
        
        # Decoy condition (never triggers due to data)
        if temp < 0:
            raise RuntimeError("Impossible temperature")
        
        # Nesting Level 2: Primary checks
        if voltage > config['voltage_critical']:
            # Nesting Level 3
            if temp > config['temp_high']:
                alert_count += 2
                recent_alerts.append((timestamp, 'CRITICAL'))
            else:
                alert_count += 1
                if stability > 80:
                    # Contradictory path: stability reduces alert weight
                    alert_count -= 1
                    
        # Distraction block: plausible but irrelevant
        predicted_next = temp * 1.02
        if predicted_next > 95 and idx < len(logs) - 1:
            pass  # No effect

    # Distractor aggregation
    average_gap = sum(timestamps[i+1] - timestamps[i] for i in range(len(timestamps)-1)) / (len(timestamps) - 1)
    
    # Key logic: only this matters
    sustained_high_temp = 0
    for temp in sensor_a:
        if temp > thresholds['temp_high']:
            sustained_high_temp += 1
    
    # Final decision tree (Nesting Level 3)
    if sustained_high_temp >= thresholds['stability_window']:
        base_score = 850
        adjustment = 0
        # Nesting Level 4
        for reading in sensor_c:
            if reading > 200:
                adjustment += 15
        final_diagnostic = base_score + adjustment
    else:
        final_diagnostic = 400 + alert_count * 50
    
    # Red herring return alternative
    metadata_flag = len(recent_alerts) > 0 and average_gap == 1.0
    
    return int(final_diagnostic)  # Actual answer source

# Spurious pre-analysis
baseline_risk = calculate_entropy(sensor_a)

# Key execution point
final_diagnostic = analyze_system_state(health_logs, thresholds)

# Output requirement
print(f"Result: {final_diagnostic}")