from collections import defaultdict
from itertools import combinations

# System health monitoring simulation with signal processing

def generate_baseline(size):
    return [i * 0.5 + (i % 7) for i in range(size)]

def apply_filter(signal, factor=1.1):
    return [x * factor if x > 0 else x for x in signal]

def compute_moving_avg(data, window=3):
    smoothed = []
    for i in range(len(data)):
        start = max(0, i - window + 1)
        segment = data[start:i+1]
        smoothed.append(sum(segment) / len(segment))
    return smoothed

def detect_spikes(signal, multiplier=2.5):
    mean_val = sum(signal) / len(signal)
    spikes = []
    for idx, val in enumerate(signal):
        if val > mean_val * multiplier:
            spikes.append((idx, val))
    return spikes  # Unused distractor path

def evaluate_stability(risk_profile):
    score = 0
    for level in risk_profile:
        score += level ** 0.8
    return score  # Dead function - not used in main logic

# Irrelevant diagnostic routine (distractor)
def legacy_diagnostic(x):
    temp = 0
    for i in range(len(x)):
        if i % 3 == 0:
            temp ^= int(x[i])
    return temp

# Core analysis logic
signal_raw = generate_baseline(12)
filtered_signal = apply_filter(signal_raw, factor=1.15)
avg_corrected = compute_moving_avg(filtered_signal, window=4)

# Threshold configuration map (meaningful structure)
threshold_map = defaultdict(lambda: 0.0)
threshold_map.update({
    'critical': 9.7,
    'warning': 6.3,
    'info': 3.1
})

# Simulated event triggers (unused - red herring)
event_log = []
for val in avg_corrected:
    if val > threshold_map['critical']:
        event_log.append(('CRITICAL', val))
    elif val > threshold_map['warning']:
        event_log.append(('WARNING', val))

# Signal masking via slicing and transformation
masked_region = avg_corrected[3:9]
scaled_mask = [x * 1.05 for x in masked_region]

# Decoy statistical computation
combo_stats = []
for r in range(2, 4):
    for combo in combinations(scaled_mask, r):
        combo_stats.append(sum(combo) / len(combo))

# Actual pattern analyzer used in final result
def analyze_pattern(seq, thresholds):
    cumulative = 0.0
    adjustment = thresholds['info'] * 0.25
    
    for i, value in enumerate(seq):
        if i % 2 == 0 and value > thresholds['warning']:
            cumulative += value * 0.3
        elif value < thresholds['info']:
            cumulative -= adjustment * 0.1
        else:
            cumulative += adjustment * (i % 4) * 0.05
            
        # Nested conditional manipulation
        if i > 2:
            if cumulative > 5.0:
                cumulative -= thresholds['info'] * 0.05
            elif i % 5 == 0:
                cumulative += 0.12

    # Final nonlinear transformation
    if cumulative > 10:
        return int(cumulative * 1.1)
    else:
        return int(cumulative * 1.3)

# Secondary derived sequence (distraction)
derived_features = [round(x**0.5, 2) for x in filtered_signal if x > 4.0]

# Key execution point
final_diagnostic = analyze_pattern(signal_sequence=avg_corrected, threshold_map=threshold_map)

# Additional noise variables
aggregated_diagnostics = sum([len(event_log), len(combo_stats)]) // 2
normalization_factor = sum(derived_features) if derived_features else 1.0

# Output target result
print(f"Result: {final_diagnostic}")