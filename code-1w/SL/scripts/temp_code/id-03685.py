import math

# Simulated sensor data processing for a biomedical device
raw_signals = [98.7, 102.3, 95.1, 110.4, 89.2, 101.0, 96.8, 104.5]
baseline_shift = 2.1
adjusted_readings = [x - baseline_shift for x in raw_signals]

# Irrelevant signal smoothing (distractor)
smoothed = []
for i in range(len(adjusted_readings)):
    if i == 0:
        smoothed.append(adjusted_readings[i])
    else:
        smoothed.append((adjusted_readings[i] + adjusted_readings[i-1]) / 2)

# Noise threshold filtering (partially relevant but misleading)
noise_floor = 90.0
filtered_data = [x for x in adjusted_readings if x > noise_floor]

# Core health metrics computation (critical path)
def compute_stability_index(data):
    mean_val = sum(data) / len(data)
    variance = sum((x - mean_val) ** 2 for x in data) / len(data)
    return math.sqrt(variance) if variance > 0 else 0.0

stability_score = compute_stability_index(adjusted_readings)

# Decoy function - looks important but unused in final path
def calculate_robustness_metric(signal, factor=0.9):
    return sum(math.tanh(x * factor) for x in signal)

robustness_proxy = calculate_robustness_metric(raw_signals)  # Dead-end computation

# Threshold logic with red herring conditions
warning_thresholds = {
    'high_risk': 102.0,
    'elevated': 98.0,
    'caution_zone': 95.0,
    'noise_ignore': 90.0
}

# Misleading multi-condition block (not actually used)
classification = ''
if stability_score > 5.0:
    classification = 'unstable'
elif stability_score > 3.0:
    classification = 'moderate'
else:
    classification = 'stable'  # Correct path leads here implicitly

# Auxiliary transformation (irrelevant list comp)
normalized = [round((x - min(adjusted_readings)) / (max(adjusted_readings) - min(adjusted_readings)), 3) for x in adjusted_readings]

# Key diagnostic parameters (mixed usage)
health_data = [x for x in adjusted_readings if x >= warning_thresholds['caution_zone']]

# Unused risk scoring matrix (decoy structure)
risk_matrix = [[0 for _ in range(3)] for _ in range(3)]
for i in range(3):
    for j in range(3):
        risk_matrix[i][j] = (i + 1) * (j + 1) * stability_score

# Critical threshold set (used in final analysis)
thresholds = {
    'critical': 100.0,
    'monitor': 97.0
}

# Central analysis function with nested logic
def analyze_metrics(metrics, limits):
    count_above_critical = 0
    total_concern = 0.0
    
    for val in metrics:
        if val > limits['critical']:
            count_above_critical += 1
            total_concern += val - limits['critical']
        elif val > limits['monitor']:
            total_concern += (val - limits['monitor']) * 0.5
    
    # Complex adjustment using stability from earlier
    adjustment_factor = 1.0 + (stability_score / 10.0)
    
    # Final composite score (this is the real answer)
    raw_diagnostic = count_above_critical * 100 + total_concern * adjustment_factor
    
    # Red herring: secondary check that doesn't affect outcome
    outlier_count = len([x for x in metrics if x < 92 or x > 108])
    if outlier_count > 2:
        raw_diagnostic *= 1.1  # Never triggered in this case
    
    return int(raw_diagnostic)

# Execution point of interest
final_diagnostic = analyze_metrics(health_data, thresholds)
print(f"Result: {final_diagnostic}")