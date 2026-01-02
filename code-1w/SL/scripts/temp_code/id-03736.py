from collections import defaultdict
import math

# Simulate sensor data aggregation and performance scoring
def collect_sensor_data(nodes):
    data = defaultdict(list)
    for node in nodes:
        if node.startswith('S'):
            data['temperature'].append(len(node) * 1.5)
        elif node.startswith('P'):
            data['pressure'].append(len(node) ** 1.2)
        else:
            data['auxiliary'].append(hash(node) % 100)
    return data

# Misleading auxiliary computation (not used in final score)
def compute_thermal_gradient(data):
    temps = data['temperature']
    if len(temps) < 2:
        return 0.0
    return sum(temps[i+1] - temps[i] for i in range(len(temps)-1)) / (len(temps) - 1)

# Core metric processor
def normalize_metrics(raw):
    normalized = {}
    for key, values in raw.items():
        if values:
            avg = sum(values) / len(values)
            if key == 'temperature':
                normalized[key] = max(0, (avg - 20) / 10)
            elif key == 'pressure':
                normalized[key] = min(1, avg / 100)
            else:
                normalized[key] = len(values) * 0.1
        else:
            normalized[key] = 0.0
    return normalized

# Weighted evaluation with red herring variables
def evaluate_performance(metrics, weights):
    base = 0.0
    adjustment = 0.0
    temp_score = metrics.get('temperature', 0) * weights.get('temperature', 0)
    press_score = metrics.get('pressure', 0) * weights.get('pressure', 0)
    
    # Irrelevant intermediate calculation (distractor)
    aux_score = metrics.get('auxiliary', 0) * 0.25  # Not included in final weight
    adjustment += math.sin(aux_score) if aux_score > 0 else 0
    
    base += temp_score + press_score
    
    # Apply non-linear bonus for balanced performance (real logic)
    if metrics.get('temperature', 0) > 0.5 and metrics.get('pressure', 0) > 0.5:
        base *= 1.15
    
    return int(base * 100) / 100  # Round to two decimals

# Main execution
nodes_list = ['S1', 'S2', 'P1', 'P2', 'X1', 'X2', 'X3']
raw_data = collect_sensor_data(nodes_list)
scores = normalize_metrics(raw_data)

# Dead code path (never executed but present)
if False:
    debug_info = compute_thermal_gradient(raw_data)
    print(f'Debug: {debug_info}')

weights_scheme = {
    'temperature': 40,
    'pressure': 60,
    'calibration': 10  # Unused weight (misleading)
}

# Key statement
final_score = evaluate_performance(scores, weights_scheme)
print(f'Result: {final_score}')