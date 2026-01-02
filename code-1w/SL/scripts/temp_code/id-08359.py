import math

def preprocess_sensor_data(raw_readings):
    filtered = [x for x in raw_readings if x > 0]
    baseline = sum(filtered) / len(filtered) if filtered else 0
    adjusted = [x * 0.98 + baseline * 0.02 for x in filtered]
    return adjusted

def evaluate_safety_margin(temp, pressure):
    if temp < 200:
        return "LOW"
    elif temp < 400:
        if pressure > 80:
            return "MEDIUM"
        return "LOW"
    else:
        if pressure > 90:
            return "HIGH"
        elif pressure > 70:
            return "MEDIUM"
        return "LOW"

def compute_redundancy_score(nodes):
    active = 0
    for node in nodes:
        if node.get('status') == 'active' and node.get('latency', 100) < 50:
            active += 1
    total = len(nodes)
    return active / total if total else 0

def simulate_failover_system(config_matrix):
    outcomes = []n    for row in config_matrix:
        outcome = 1
        for val in row:
            outcome *= (val % 7) + 1
        outcomes.append(outcome)
    return outcomes

def calculate_thermal_output(stages):
    peak = 0
    cumulative = 0
    for stage in stages:
        temp_mod = stage['temperature'] * stage['duration']
        if stage['mode'] == 'turbo':
            temp_mod *= 1.4
        elif stage['mode'] == 'eco':
            temp_mod *= 0.7
        cumulative += temp_mod
        if temp_mod > peak:
            peak = temp_mod
    efficiency_ratio = 0.85 + (len(stages) * 0.01)
    base_output = cumulative * efficiency_ratio
    adjustment_factor = math.sin(math.pi / (len(stages) + 1))
    final_output = base_output * adjustment_factor
    return final_output

def analyze_calibration_sequence(seq):
    result = 0
    for i, val in enumerate(seq):
        if i % 3 == 0:
            result += val ** 2
        elif i % 3 == 1:
            result -= val // 2
        else:
            result += abs(val - 10)
    return result

# Irrelevant sensor simulation data (distraction)
raw_sensor_input = [23.1, -1.0, 45.6, 0.0, 67.8, 12.3, 89.0, -5.5, 34.2]
processed_data = preprocess_sensor_data(raw_sensor_input)
safety_status = evaluate_safety_margin(350, 85)

# Dummy system configuration matrix (dead path)
config_matrix = [
    [3, 1, 4],
    [1, 5, 9],
    [2, 6, 5]
]
sim_results = simulate_failover_system(config_matrix)

# Node cluster state (irrelevant to thermal output)
node_pool = [
    {'id': 'A1', 'status': 'active', 'latency': 30},
    {'id': 'A2', 'status': 'inactive', 'latency': 90},
    {'id': 'B1', 'status': 'active', 'latency': 60},
    {'id': 'C3', 'status': 'active', 'latency': 20}
]
reliability_score = compute_redundancy_score(node_pool)

# Critical process stages affecting thermal output
process_stages = [
    {'temperature': 200, 'duration': 3, 'mode': 'normal'},
    {'temperature': 300, 'duration': 2, 'mode': 'turbo'},
    {'temperature': 150, 'duration': 4, 'mode': 'eco'},
    {'temperature': 250, 'duration': 2, 'mode': 'normal'}
]

# Calibration sequence for unrelated subsystem (distractor)
calibration_pattern = [8, 12, 5, 10, 7]
calibration_result = analyze_calibration_sequence(calibration_pattern)

# Key computation: Thermal capacity derived from process stages
thermal_capacity = calculate_thermal_output(process_stages)

# Print final target result
print(f"Result: {thermal_capacity}")