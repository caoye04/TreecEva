from collections import defaultdict, Counter
import math

# Simulated sensor data from engine diagnostics
def get_engine_diagnostics():
    return [
        {'rpm': 3200, 'temp': 88.5, 'vibration': 0.45, 'load': 76},
        {'rpm': 4100, 'temp': 95.2, 'vibration': 0.67, 'load': 88},
        {'rpm': 3800, 'temp': 91.0, 'vibration': 0.55, 'load': 82},
        {'rpm': 4400, 'temp': 98.7, 'vibration': 0.72, 'load': 94},
        {'rpm': 3600, 'temp': 89.3, 'vibration': 0.49, 'load': 79}
    ]

# Irrelevant helper - analyzes vibration frequency (not used in final calculation)
def analyze_vibration_spectrum(data):
    bins = defaultdict(int)
    for entry in data:
        mag = entry['vibration']
        freq_band = int(mag * 10) % 5
        bins[freq_band] += 1
    return dict(bins)

# Misleading transformation - looks important but unused
def compute_load_efficiency(data):
    total_load = sum(d['load'] for d in data)
    efficiency_curve = [math.sin(d['rpm']/1000) * d['load'] for d in data]
    return sum(efficiency_curve) / len(efficiency_curve) if efficiency_curve else 0

# Decoy function that appears related but is never called
def estimate_fuel_consumption(rpm, load):
    base_rate = 0.05
    surge = math.log(load + 1) * 0.02
    return base_rate + (rpm / 10000) * surge

# Core calculation chain
def extract_operational_windows(data):
    windows = []
    for i, d in enumerate(data):
        if d['temp'] > 90:
            power_factor = d['load'] * math.sqrt(d['rpm'] / 1000)
            # Bit manipulation red herring
            encoded = (int(power_factor) << 2) ^ 0xAA
            windows.append({'index': i, 'rating': power_factor, 'code': encoded})
    return windows

# Another distraction: statistical outlier detection (unused)
def find_outliers(data, key='temp', threshold=0.5):
    values = [d[key] for d in data]
    mean = sum(values) / len(values)
    std = math.sqrt(sum((x - mean)**2 for x in values) / len(values))
    return [i for i, x in enumerate(values) if abs(x - mean) > threshold * std]

# Real processing begins here
def aggregate_performance_metrics(data):
    metrics = defaultdict(float)
    temp_sum = 0.0
    
    for idx, reading in enumerate(data):
        temp_sum += reading['temp']
        # Conditional expression with zip usage
        status_flag = 'high' if reading['load'] > 80 else 'normal'
        metrics[f'load_{status_flag}'] += 1

    avg_temp = temp_sum / len(data)
    metrics['avg_temperature'] = avg_temp

    # Use of enumerate and zip in a meaningful but partially distracting way
    labels = ['A', 'B', 'C', 'D', 'E']
    for i, (label, entry) in enumerate(zip(labels, data)):
        if i % 2 == 0:
            metrics['even_index_rpm'] += entry['rpm']
        else:
            metrics['odd_index_temp'] += entry['temp']

    # This count matters for later logic
    hot_cycles = sum(1 for d in data if d['temp'] > 90)
    metrics['stress_count'] = hot_cycles

    return metrics

# The actual relevant function buried among distractions
def calculate_thermal_rating(metrics):
    base = metrics['avg_temperature']
    stress_factor = metrics['stress_count']
    
    # Real formula path
    adjustment = 0
    if stress_factor >= 2:
        adjustment = 12.5
    elif stress_factor == 1:
        adjustment = 5.0
    else:
        adjustment = 0
    
    # Final computation
    rating = (base * 1.8) + adjustment  # Convert to weighted thermal scale
    
    # Dead code branch - misleading
    if rating < 100:
        fallback = math.exp(base / 20)
        # This is never executed but looks important
        rating = fallback * 1.2
    
    return rating

# Unused complex data structure - decoy
class EngineProfile:
    def __init__(self, readings):
        self.readings = readings
        self.signature = self._generate_signature()
    
    def _generate_signature(self):
        return ''.join(f'{r["rpm"]%100:02.0f}' for r in self.readings)

# Main execution flow
data_samples = get_engine_diagnostics()

# Irrelevant transformations
vib_analysis = analyze_vibration_spectrum(data_samples)
efficiency_score = compute_load_efficiency(data_samples)
outlier_indices = find_outliers(data_samples)

# Partially relevant processing
engine_metrics = aggregate_performance_metrics(data_samples)

# Critical statement: what is the value of thermal_capacity here?
thermal_capacity = calculate_thermal_rating(engine_metrics)

# More distractions below
profile = EngineProfile(data_samples)
final_diagnostic = {
    'unit_id': 'ENG-XR4',
    'status': 'STABLE',
    'capacity_checksum': int(thermal_capacity) ^ 0xFFFF,
    'timestamp': '2023-11-05T10:30:00Z'
}

print(f"Result: {thermal_capacity}")