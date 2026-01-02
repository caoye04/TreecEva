import itertools

# Simulated sensor readings with noise and redundant channels
temperature_readings = [23.4, 24.1, 22.9, 25.0, 23.8, 24.2]
humidity_readings = [45, 47, 46, 50, 48, 49]
pressure_readings = [1013, 1012, 1014, 1015, 1011, 1013]

# Irrelevant auxiliary data (distractor)
def useless_transform(data):
    return [x * 1.05 + 3 for x in data]

def apply_noise_reduction(data):
    smoothed = [data[0]]
    for i in range(1, len(data) - 1):
        smoothed.append(sum(data[i-1:i+2]) / 3)
    smoothed.append(data[-1])
    return smoothed

# Misleading performance metric (dead path)
class LegacyScorer:
    def __init__(self):
        self.baseline = 100
    
    def score(self, val):
        return abs(val - self.baseline) * 0.1

# Core system: Data quality metrics
def calculate_stability(readings):
    diffs = [abs(readings[i] - readings[i-1]) for i in range(1, len(readings))]
    return round(sum(diffs) / len(diffs), 4)

def calculate_outlier_ratio(readings):
    mean_val = sum(readings) / len(readings)
    variance = sum((x - mean_val)**2 for x in readings) / len(readings)
    std_dev = variance ** 0.5
    outliers = [x for x in readings if abs(x - mean_val) > 2 * std_dev]
    return len(outliers) / len(readings)

def generate_combinations(dimensions):
    # Use of itertools - relevant but indirect contribution
    return list(itertools.product(*dimensions))

# Red herring function that looks important but unused
def compute_entropy(data):
    from math import log
    freq_map = {}
    for x in data:
        freq_map[x] = freq_map.get(x, 0) + 1
    total = len(data)
    entropy = 0
    for count in freq_map.values():
        p = count / total
        entropy -= p * log(p, 2)
    return entropy

# Another decoy: complex transformation with no downstream use
temp_enhanced = [round(t * 1.02, 2) for t in temperature_readings]
humid_enhanced = [h + 2 if h < 48 else h - 1 for h in humidity_readings]

# Apply real signal processing
stable_temp = apply_noise_reduction(temperature_readings)
stable_humid = apply_noise_reduction(humidity_readings)

# Compute diagnostic metrics (some used, some not)
metrics = {
    'temp_stability': calculate_stability(stable_temp),
    'humid_stability': calculate_stability(stable_humid),
    'pressure_outlier_rate': calculate_outlier_ratio(pressure_readings),
    'temp_outlier_rate': calculate_outlier_ratio(temperature_readings),
    'baseline_drift': abs(temperature_readings[-1] - temperature_readings[0]),
    'redundant_metric_x': len([p for p in pressure_readings if p > 1012]),
    'placeholder_flag': False
}

# Simulate historical correlation grid (complex but irrelevant structure)
dim_sets = [
    ['A', 'B'],
    ['X', 'Y', 'Z'],
    ['α', 'β']
]
config_space = generate_combinations(dim_sets)  # Computation with no effect

# Key logic buried in distraction
adjustment_factor = 0.85
if metrics['temp_stability'] < 0.5:
    adjustment_factor *= 0.9
else:
    adjustment_factor *= 1.1

if metrics['humid_stability'] > 0.6:
    adjustment_factor *= 1.2

# Hidden dependency on outlier rates
outlier_penalty = (metrics['temp_outlier_rate'] + metrics['pressure_outlier_rate']) * 50

# Critical evaluation function
def evaluate_performance(metrix):
    base = 1000
    # Real scoring logic
    stability_bonus = (0.5 - metrix['temp_stability']) * 100
    stability_bonus += (0.5 - metrix['humid_stability']) * 80
    
    # Penalty for drift
    drift_penalty = metrix['baseline_drift'] * 10
    
    # Outlier components interact nonlinearly
    total_penalty = drift_penalty + outlier_penalty
    
    # Final composition
    score = base + stability_bonus - total_penalty
    score *= adjustment_factor
    
    # Final clamping and rounding
    return int(round(score))

# Trigger point: what is final_score after this?
final_score = evaluate_performance(metrics)

print(f"Result: {final_score}")