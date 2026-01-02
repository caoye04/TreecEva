from collections import defaultdict, Counter
import math

# Simulated sensor data from a distributed environmental monitoring system
temperature_readings = [23.4, 24.1, 22.7, 25.3, 26.0, 24.8, 23.9, 22.1, 21.5, 20.8]
humidity_readings = [45, 47, 50, 55, 60, 62, 58, 54, 50, 48]
pressure_readings = [1013, 1015, 1012, 1010, 1008, 1007, 1009, 1011, 1014, 1016]

# Irrelevant auxiliary data (distractor)
legacy_sensor_ids = ['LGS001', 'LGS002', 'LGS003']
device_firmware_map = defaultdict(lambda: 'unknown')
for sid in legacy_sensor_ids:
    device_firmware_map[sid] = 'v2.1'

# Benchmark thresholds (used later)
benchmark_thresholds = {
    'temp_stability': 1.5,
    'humidity_rise_limit': 15,
    'pressure_drift': 10
}

# Metric computation engine
def analyze_variability(data, window_size=3):
    """Calculates rolling variance (distraction: not directly used in final path)"""
    variances = []
    for i in range(len(data) - window_size + 1):
        window = data[i:i+window_size]
        mean = sum(window) / len(window)
        variance = sum((x - mean) ** 2 for x in window) / len(window)
        variances.append(round(variance, 3))
    return variances

# Distractor function - looks important but unused
def compute_entropy(values):
    counts = Counter(values)
    total = len(values)
    entropy = 0
    for count in counts.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 4)

# Core logic for trend detection
def extract_trend_segments(data, threshold=1.0):
    """Splits data into segments based on rate of change."""
    segments = []
    current_segment = [data[0]]
    
    for i in range(1, len(data)):
        if abs(data[i] - data[i-1]) > threshold:
            if current_segment:
                segments.append(current_segment)
            current_segment = [data[i]]
        else:
            current_segment.append(data[i])
    
    if current_segment:
        segments.append(current_segment)
    
    return segments

# Misleading intermediate calculation (red herring)
apparent_anomalies = []
for i, temp in enumerate(temperature_readings):
    if temp > 25 and humidity_readings[i] < 50:
        apparent_anomalies.append(i)

# Real processing begins here
metric_set = {
    'stability': temperature_readings,
    'response_curve': humidity_readings,
    'robustness': pressure_readings
}

benchmark_data = defaultdict(dict)
benchmark_data['stability']['target'] = 24.0
benchmark_data['stability']['tolerance'] = 2.0
benchmark_data['response_curve']['baseline'] = 50
benchmark_data['response_curve']['drift_allowed'] = 10
benchmark_data['robustness']['reference'] = 1010

# Secondary distractor: unused complex structure
class DataValidator:
    def __init__(self, rules):
        self.rules = rules
        self.errors = []
    
    def validate(self, readings):
        # This function is never called
        for r in readings:
            if not self.rules.get('min', float('-inf')) < r < self.rules.get('max', float('inf')):
                self.errors.append(r)
        return len(self.errors) == 0

validator = DataValidator({'min': 0, 'max': 30})

# Key transformation pipeline
def calculate_deviation_penalty(readings, target, tolerance):
    """Computes penalty score based on deviation from target beyond tolerance."""
    base_penalty = 0
    consecutive_breach = 0
    
    for val in readings:
        if abs(val - target) > tolerance:
            base_penalty += 1
            consecutive_breach += 1
        else:
            consecutive_breach = 0
    
    # Apply compounding for sustained issues
    return base_penalty * (1 + 0.1 * consecutive_breach)

def aggregate_metrics(metrics, refs):
    """Combines multiple metric scores into weighted performance index."""
    score_components = defaultdict(float)
    
    # Process stability (temperature)
    temp_target = refs['stability']['target']
    temp_tol = refs['stability']['tolerance']
    temp_penalty = calculate_deviation_penalty(metrics['stability'], temp_target, temp_tol)
    score_components['stability_score'] = max(100 - temp_penalty * 5, 0)
    
    # Process response curve (humidity)
    hum_baseline = refs['response_curve']['baseline']
    hum_drift = refs['response_curve']['drift_allowed']
    hum_trend_segments = extract_trend_segments(metrics['response_curve'], threshold=3.0)
    hum_penalty = len(hum_trend_segments) - 1  # More segments = more instability
    score_components['response_score'] = max(90 - hum_penalty * 4, 0)
    
    # Process robustness (pressure)
    press_reference = refs['robustness']['reference']
    press_changes = [abs(pressure_readings[i] - pressure_readings[i-1]) for i in range(1, len(pressure_readings))]
    press_volatility = sum(1 for pc in press_changes if pc > 3)
    score_components['robustness_score'] = max(100 - press_volatility * 10, 0)
    
    # Hidden dependency: combinatorics-based weighting
    n_metrics = len(score_components)
    total_weight = sum(math.comb(n_metrics, i+1) for i in range(n_metrics))  # 1+2+3=6
    
    final_index = 0
    weights = [1, 2, 3]  # Increasing importance
    for i, key in enumerate(sorted(score_components.keys())):
        final_index += score_components[key] * weights[i]
    
    normalized = final_index / total_weight
    return round(normalized, 2)

# Decoy function that appears related but is unused
def deprecated_evaluation(met, ref):
    return sum(len(str(v)) for v in met.values()) + sum(len(ref.keys()))

# Main evaluation function
def evaluate_performance(metric_set, benchmark_data):
    aggregated = aggregate_metrics(metric_set, benchmark_data)
    
    # Final adjustment based on set operations (core concept)
    temp_set = set(int(t) for t in temperature_readings)
    hum_set = set(humidity_readings)
    common_extremes = temp_set.intersection(hum_set)
    
    adjustment_factor = 1.0
    if common_extremes:
        max_common = max(common_extremes)
        if max_common > 45:
            adjustment_factor = 0.95
        else:
            adjustment_factor = 1.05
    
    adjusted_score = aggregated * adjustment_factor
    
    # Introduce irrelevant bitwise manipulation (distractor)
    magic_constant = 0x1F
    masked = int(adjusted_score) & magic_constant
    inverted = magic_constant ^ masked
    # But do NOT use these in final result
    
    # Final clamping and rounding
    final_value = min(max(round(adjusted_score, 2), 0), 100)
    return final_value

# Execution point of interest
final_score = evaluate_performance(metric_set, benchmark_data)

# Print result as required
print(f"Result: {final_score}")