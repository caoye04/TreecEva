import math

# Simulated biomedical signal processing system with diagnostic logic

def analyze_waveform(signal_samples):
    if not signal_samples:
        return 0
    mean_val = sum(signal_samples) / len(signal_samples)
    variance = sum((x - mean_val) ** 2 for x in signal_samples) / len(signal_samples)
    return math.sqrt(variance)

# Irrelevant helper (decoy function - never called)
def legacy_filter(data):
    return [x * 0.9 for x in data if x > 5]

# Signal conditioning chain (some steps are red herrings)
def preprocess_signal(raw_input):
    filtered = [x for x in raw_input if x >= 0]  # Remove negatives
    normalized = [x / max(filtered) for x in filtered] if filtered else []
    smoothed = []
    for i in range(len(normalized)):
        window = normalized[max(0, i-2):i+3]
        smoothed.append(sum(window) / len(window))
    return smoothed

# Diagnostic rules engine
def evaluate_risk_level(bpm, variability, age_factor):
    base_score = bpm * 0.3 + variability * 2.5
    adjusted = base_score * (1 + 0.05 * age_factor)
    if adjusted < 40: return 'LOW'
    elif adjusted < 60: return 'MODERATE'
    else: return 'HIGH'

# Data fusion module using sets and lambdas
fusion_kernel = lambda a, b, c: (a * 0.4) + (b * 0.3) + (c * 0.3)

# Complex state tracker (mostly irrelevant)
class MonitoringState:
    def __init__(self):
        self.history = []
        self.alert_count = 0
        self.last_update = None
    
    def update(self, val):
        self.history.append(val)
        self.last_update = val

# Unused class - dead code path distraction
class CalibrationProfile:
    def __init__(self, level):
        self.level = level
        self.sequence = [i**2 for i in range(level)]
    
    def validate(self, readings):
        return all(r > self.level for r in readings)

# Main processing pipeline
health_data = {
    'heart_rate': [72, 75, 78, 74, 76],
    'resp_rate': [16, 18, 17, 16, 19],
    'o2_levels': [98, 97, 98, 96, 97],
    'neural_activity': [-0.2, 0.5, 0.7, -0.1, 0.9, 1.2, 0.8],
    'age': 45,
    'baseline_stress': 3.2
}

# Threshold configuration (critical)
thresholds = {
    'hr_max': 100,
    'variability_cap': 8.0,
    'o2_min': 95
}

# Auxiliary computations (many are distractions)
hr_mean = sum(health_data['heart_rate']) / len(health_data['heart_rate'])
dummy_correction = (lambda x: x * 1.05)(hr_mean - 70)

# Set-based anomaly detection (partially relevant)
abnormal_hr = {x for x in health_data['heart_rate'] if x > thresholds['hr_max']}
o2_set = set(health_data['o2_levels'])
anomaly_flags = abnormal_hr.union({x for x in o2_set if x < thresholds['o2_min']})
flag_count = len(anomaly_flags)  # Used later

# Signal processing chain
processed_neural = preprocess_signal(health_data['neural_activity'])
neural_variability = analyze_waveform(processed_neural) if processed_neural else 0.0

# Risk scoring with multiple branches
risk_category = evaluate_risk_level(
    hr_mean,
    neural_variability,
    health_data['age'] / 10
)

# Decoy calculations with misleading intermediate values
phantom_metric = 0
for i in range(5):
    phantom_metric += (i * hr_mean) % 17
phantom_metric = int(math.sin(phantom_metric) * 100)

# Data transformation using dictionary operations
transformed = {}
for k, v in health_data.items():
    if isinstance(v, list):
        transformed[k + '_stats'] = {
            'mean': sum(v) / len(v),
            'range': max(v) - min(v)
        }

# Core diagnostic logic - where answer is determined
compliance_set = {1, 2, 3, 4, 5}
coverage_set = {3, 4, 5, 6, 7}
overlap = compliance_set.intersection(coverage_set)
system_weight = len(overlap) * 0.2

metric_a = transformed['heart_rate_stats']['mean']
metric_b = transformed['o2_levels_stats']['mean'] * 0.1
metric_c = neural_variability * 5

# Final integration using lambda and set-derived weight
final_diagnostic = fusion_kernel(metric_a, metric_b, metric_c) + (system_weight * flag_count)

# Print result as required
print(f"Result: {final_diagnostic}")