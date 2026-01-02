import math

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 22.8, 25.0, 26.3, 23.9, 24.4, 25.1]
humidity_readings = [45.2, 47.8, 44.1, 50.3, 52.0, 46.7, 48.9, 51.2]
pressure_readings = [1013, 1015, 1012, 1008, 1005, 1010, 1014, 1016]

# Irrelevant auxiliary measurements (distractor)
sound_levels = [32, 35, 30, 40, 45, 38, 36, 41]  # Decoy sensor data
light_intensity = [800, 850, 780, 900, 950, 870, 830, 910]  # Not used in logic

# Preprocessing: Normalize temperature and humidity into health index
normalized_temps = [(t - 20) / 5 for t in temperature_readings if t > 20]
normalized_humid = [h / 100 for h in humidity_readings]

# Composite environmental score (intermediate distractor)
event_scores = [
    round((temp_idx * 0.6) + (humid_idx * 0.4), 3)
    for temp_idx, humid_idx in zip(normalized_temps, normalized_humid)
]

# Threshold configuration map for anomaly detection (critical)
threshold_map = {
    'high_temp': 24.5,
    'low_humid': 45.0,
    'pressure_drop': -5,
    'stability_window': 3
}

# Misleading transformation chain (dead path)
def compute_entropy(values):
    total = sum(values)
    probs = [v / total for v in values]
    return -sum(p * math.log2(p) for p in probs if p > 0)

entropy_val = compute_entropy([1, 2, 3])  # Unused result

# Data fusion engine with red herring operations
def filter_anomalies(data, limit):
    anomalies = []
    for i in range(len(data)):
        if data[i] > limit:
            anomalies.append(i)
            break
    return anomalies + [len(data)]  # Artificial padding

# Spurious call with unused return
spurious_detections = filter_anomalies(temperature_readings, 30.0)

# Core processing pipeline
def smooth_signal(signal, window=2):
    smoothed = []
    for i in range(len(signal)):
        start = max(0, i - window)
        end = min(len(signal), i + window + 1)
        avg = sum(signal[start:end]) / (end - start)
        smoothed.append(avg)
    return smoothed

# Apply smoothing to relevant data
smoothed_temps = smooth_signal(temperature_readings)
smoothed_humid = smooth_signal(humidity_readings)

# Construct paired observation tuples
paired_observations = list(zip(smoothed_temps, smoothed_humid, pressure_readings))

# Extract only readings where temperature exceeds dynamic threshold
dynamic_threshold = sum(smoothed_temps) / len(smoothed_temps) + 0.5
filtered_pairs = [
    (t, h, p) for t, h, p in paired_observations
    if t > threshold_map['high_temp'] and p < 1014
]

# Secondary filtering based on humidity trend
reference_humid = sum(smoothed_humid) / len(smoothed_humid)
stable_readings = [
    item for item in filtered_pairs
    if abs(item[1] - reference_humid) < 3.0
]

# Transform into deviation-based features
processed_data = []
for temp, humid, press in stable_readings:
    temp_dev = temp - threshold_map['high_temp']
    press_dev = press - 1013
    score = (temp_dev * 2.0) - abs(press_dev)
    if humid < threshold_map['low_humid']:
        score += 1.5
    processed_data.append(round(score, 4))

# Fake machine learning model (decoy)
class DummyPredictor:
    def __init__(self):
        self.weight = 0.5
    
    def predict(self, x):
        return [self.weight * val for val in x]

predictor = DummyPredictor()
predictions = predictor.predict(processed_data)  # Never used

# Actual diagnostic logic hidden among distractions
def analyze_readings(features, config):
    if not features:
        return -999.0
    
    base = sum(features)
    penalty = 0
    
    # Hidden logic step 1: count positive spikes
    spike_count = sum(1 for f in features if f > 1.0)
    if spike_count >= config['stability_window']:
        penalty += 20
    
    # Hidden logic step 2: check dominance of high values
    high_feature_ratio = sum(1 for f in features if f > 1.5) / len(features)
    if high_feature_ratio > 0.6:
        base *= 1.2
    
    # Hidden logic step 3: phase shift detection (simulated)
    ordered = sorted(features, reverse=True)
    decay_ratio = ordered[0] / ordered[-1] if ordered[-1] != 0 else 0
    if decay_ratio > 3:
        base -= 15
    
    # Hidden logic step 4: parity adjustment
    even_index_sum = sum(features[i] for i in range(0, len(features), 2))
    if even_index_sum > sum(features):
        base += 5.5
    
    return round(base - penalty, 4)

# Critical execution point
final_diagnostic = analyze_readings(processed_data, threshold_map)

# Output result as required
print(f"Result: {final_diagnostic}")