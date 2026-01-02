import math

# Sensor simulation data (irrelevant initialization)
temp_offsets = [0.1, -0.2, 0.5, 0.0, -0.3]
humidity_bias = (1.2, 0.8, 1.5, 0.9, 1.1)

# Irrelevant helper function (dead code path)
def normalize_sensor(x):
    return (x - min(temp_offsets)) / (max(temp_offsets) - min(temp_offsets))

# Unused calibration matrix
calibration_matrix = [[i * j for j in range(3)] for i in range(3)]

# Real signal processing begins here
raw_signals = [
    [12, 15, 14, 13, 16],
    [20, 18, 22, 19, 21],
    [8, 7, 9, 6, 10],
    [25, 24, 26, 23, 27]
]

# Apply irrelevant smoothing filter (partially distracting)
smoothed = []
for seq in raw_signals:
    smoothed_seq = []
    for i in range(len(seq)):
        left = max(0, i-1)
        right = min(len(seq), i+2)
        window_avg = sum(seq[left:right]) / (right - left)
        smoothed_seq.append(round(window_avg, 1))
    smoothed.append(smoothed_seq)

# Misleading transformation chain
transform_chain = lambda x: x ** 0.5 if x > 5 else x
mapped_data = [[transform_chain(val) for val in row] for row in smoothed]

# Distractor: unused frequency analysis
dominant_freqs = []
for idx, series in enumerate(mapped_data):
    peak = max(series)
    if idx % 2 == 0:
        dominant_freqs.append(peak * 1.5)
    else:
        dominant_freqs.append(peak * 0.7)

# Core diagnostic logic (hidden among noise)
processed_data = []
for readings in raw_signals:
    # Extract key features
    avg_reading = sum(readings) / len(readings)
    variance = sum((x - avg_reading) ** 2 for x in readings) / len(readings)
    peak_to_avg_ratio = max(readings) / avg_reading
    
    # Hidden threshold logic
    if variance > 4.0:
        category = 'unstable'
    elif peak_to_avg_ratio > 1.4:
        category = 'spiky'
    else:
        category = 'stable'
    
    processed_data.append({
        'mean': avg_reading,
        'variance': variance,
        'ratio': peak_to_avg_ratio,
        'class': category
    })

# Decoy aggregation (looks important but unused)
avg_variance = sum(p['variance'] for p in processed_data) / len(processed_data)
overall_stability = 'high' if avg_variance < 3.0 else 'low'

# Actual analysis function
threshold_map = {'stable': 10, 'spiky': 25, 'unstable': 40}

def analyze_readings(diag_list):
    base_score = 0
    for entry in diag_list:
        base_score += threshold_map[entry['class']]
    
    # Secondary adjustment based on mean distribution
    means = [d['mean'] for d in diag_list]
    mean_range = max(means) - min(means)
    
    if mean_range > 10:
        base_score += 15
    elif mean_range > 5:
        base_score += 5
    
    # Final nonlinear transformation (critical step)
    adjusted = int((base_score * 1.8) - (len(diag_list) * 2.5))
    
    # Red herring: unused entropy calculation
    entropy = sum(-p['variance']/10 * math.log(p['variance']/10 + 1e-8) for p in diag_list)
    
    return adjusted

# Execution point of interest
final_diagnostic = analyze_readings(processed_data)

# Print result as required
print(f"Result: {final_diagnostic}")