from collections import defaultdict, Counter
import math

# Simulated sensor data stream (temperature, heart rate, steps)
sensor_readings = [
    (36.7, 72, 8900), (37.1, 75, 9100), (36.9, 74, 8700),
    (37.2, 78, 9300), (36.8, 73, 8500), (37.0, 76, 9000),
    (37.3, 79, 9400), (36.6, 71, 8800), (37.5, 81, 9600),
    (37.4, 80, 9500), (36.5, 70, 8400), (37.6, 82, 9700)
]

# Irrelevant baseline metrics (distractor)
baseline_stats = {
    'avg_temp': 36.8,
    'avg_hr': 74.5,
    'step_goal': 10000
}

# Misleading transformation: normalize steps to 0-1 scale (unused later)
normalized_steps = [round(steps / 10000, 3) for _, _, steps in sensor_readings]

# Extract temporal trends (red herring: not used in final logic)
temp_trend = [sensor_readings[i][0] - sensor_readings[i-1][0] for i in range(1, len(sensor_readings))]
hr_trend = [sensor_readings[i][1] - sensor_readings[i-1][1] for i in range(1, len(sensor_readings))]

# Build health data structure with slicing and grouping
health_data = defaultdict(list)
for i, (temp, hr, steps) in enumerate(sensor_readings):
    time_block = i // 3  # Group by every 3 readings
    health_data[time_block].append((temp, hr, steps))

# Decoy function that looks important but is never called
def analyze_anomaly_pattern(data):
    anomaly_score = 0
    for block in data.values():
        temps = [x[0] for x in block]
        if max(temps) - min(temps) > 0.8:
            anomaly_score += 1
    return anomaly_score

# Unused statistical summary (dead code path)
summary_stats = {}
for block_id, readings in health_data.items():
    temps = [r[0] for r in readings]
    heart_rates = [r[1] for r in readings]
    steps_count = [r[2] for r in readings]
    summary_stats[block_id] = {
        'temp_range': round(max(temps) - min(temps), 2),
        'hr_stddev': round((sum((x - sum(heart_rates)/len(heart_rates))**2 for x in heart_rates)/len(heart_rates))**0.5, 2),
        'total_steps': sum(steps_count)
    }

# Thresholds for health evaluation (key parameters)
thresholds = {
    'fever_temp': 37.4,
    'elevated_hr': 77,
    'active_steps': 9000
}

# Auxiliary lambda functions for dynamic checks
is_fever = lambda t: t >= thresholds['fever_temp']
is_elevated = lambda hr: hr >= thresholds['elevated_hr']
is_active = lambda s: s >= thresholds['active_steps']

# Composite scoring with bit manipulation (complex reasoning)
def evaluate_risk_level(temp, hr, steps):
    # Bit 0: fever risk
    # Bit 1: high heart rate risk
    # Bit 2: low activity risk
    risk_flags = 0
    if is_fever(temp):
        risk_flags |= 1
    if is_elevated(hr):
        risk_flags |= 2
    if not is_active(steps):
        risk_flags |= 4
    
    # Apply arbitrary weight based on combination
    if risk_flags == 0:
        return 0  # No risk
    elif risk_flags & 1 and risk_flags & 2:
        return 3  # High risk if fever + elevated HR
    elif risk_flags & 4:
        return 1  # Low risk if only inactivity
    else:
        return 2  # Moderate risk

# Process each block with distractor counters
decision_trace = []
risk_counter = Counter()
useless_counter = Counter()  # Fills up with irrelevant events

for block_id in sorted(health_data.keys()):
    block = health_data[block_id]
    block_scores = []
    
    for temp, hr, steps in block:
        score = evaluate_risk_level(temp, hr, steps)
        block_scores.append(score)
        
        # Irrelevant logging (distractor)
        if temp > 37.0:
            useless_counter['warm_temp'] += 1
        if hr < 75:
            useless_counter['low_hr'] += 1
        if steps < 8500:
            useless_counter['low_step_day'] += 1
    
    avg_score = sum(block_scores) / len(block_scores)
    decision_trace.append((block_id, avg_score))

# Compute stability metric across blocks (not used in final answer)
stability = 0.0
if len(decision_trace) > 1:
    variations = [abs(decision_trace[i][1] - decision_trace[i-1][1]) for i in range(1, len(decision_trace))]
    stability = round(sum(variations) / len(variations), 4)

# Critical computation: count how many individuals exceed fever threshold
# Each block represents a different person (assumption embedded in logic)
fever_count = 0
for block in health_data.values():
    # Only one reading per person needed to trigger
    if any(is_fever(temp) for temp, _, _ in block):
        fever_count += 1

# Secondary condition: must have elevated HR in last recorded measurement
confirmed_cases = 0
for block in health_data.values():
    last_reading = block[-1]  # Use latest in block
    temp, hr, steps = last_reading
    if is_fever(temp) and is_elevated(hr):
        confirmed_cases += 1

# Final diagnostic using XOR-based validation (bit manipulation)
# Ensures both criteria are satisfied simultaneously
individual_count = len(health_data)
base_diagnostic = fever_count * 1000
adjustment_factor = (confirmed_cases << 2)  # Left shift as complexity distractor

# Core logic: use XOR to detect discrepancy between initial and confirmed cases
consistency_check = fever_count ^ confirmed_cases

# Final formula combines multiple concepts
final_diagnostic = base_diagnostic - adjustment_factor + (consistency_check * 50)

# Additional red herring: string-based encoding of results (unused)
status_map = {0: 'stable', 1: 'monitor', 2: 'alert', 3: 'critical'}
encoded_status = ''.join([status_map.get(int(s % 4), 'unknown')[0] for _, s in decision_trace])

# Print target result
print(f"Result: {final_diagnostic}")