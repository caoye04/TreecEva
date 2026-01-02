from collections import defaultdict, Counter
import math

# Simulated environmental sensor data for air quality analysis
def generate_synthetic_data():
    readings = []
    for i in range(50):
        readings.append({
            'pm25': (i * 7) % 120 + (i % 3),
            'co2': 400 + (i * 15) % 800,
            'voc': max(0, 200 - (i * 4) % 250),
            'humidity': 30 + (i * 2) % 60
        })
    return readings

def calculate_airflow_resistance(duct_width, bends, material_smoothness=0.85):
    # Irrelevant calculation: HVAC system airflow resistance (dead path)
    base_resistance = duct_width * 1.5
    bend_penalty = bends * 0.7
    return (base_resistance + bend_penalty) / material_smoothness

def compute_filter_degradation_rate(initial_efficiency, cycles, temp_c):
    # Distractor function: not actually used in final computation
    degradation = initial_efficiency * (0.012 * cycles) * (1 + (temp_c - 20) * 0.02)
    return degradation if degradation < initial_efficiency else initial_efficiency

def normalize_readings(readings):
    # Normalize sensor values to [0,1] scale (used later)
    normalized = []
    for r in readings:
        norm_r = {
            'pm25': min(r['pm25'] / 120.0, 1.0),
            'co2': min((r['co2'] - 400) / 2000.0, 1.0) if r['co2'] > 400 else 0,
            'voc': min(r['voc'] / 500.0, 1.0),
            'humidity': abs(r['humidity'] - 50) / 50.0
        }
        normalized.append(norm_r)
    return normalized

def detect_anomalies(normalized_data):
    # Identify outlier readings (distractor - not used in answer)
    anomalies = []
    for idx, entry in enumerate(normalized_data):
        score = sum(entry.values())
        if score > 2.5:
            anomalies.append(idx)
    return anomalies

def build_threshold_map(norm_data):
    # Create dynamic thresholds based on data distribution
    pm25_vals = [d['pm25'] for d in norm_data]
    co2_vals = [d['co2'] for d in norm_data]
    voc_vals = [d['voc'] for d in norm_data]
    
    # Use Counter to find most frequent bucketed values
    pm25_bins = [int(v * 10) for v in pm25_vals]
    co2_bins = [int(v * 10) for v in co2_vals]
    
    pm25_freq = Counter(pm25_bins)
    co2_freq = Counter(co2_bins)
    
    # Dominant level detection (red herring)
    dominant_pm25 = pm25_freq.most_common(1)[0][0] / 10.0 if pm25_freq else 0.5
    
    # Actual threshold logic
    thresholds = {
        'pm25_high': sum(pm25_vals) / len(pm25_vals) + 0.1,
        'co2_high': sum(co2_vals) / len(co2_vals) + 0.15,
        'voc_high': sum(voc_vals) / len(voc_vals) + 0.1
    }
    
    # Unused derived metrics
    avg_spread = (thresholds['pm25_high'] + thresholds['co2_high']) / 2
    
    return thresholds

def evaluate_stability_factor(readings):
    # Complex but irrelevant stability metric
    diffs = [abs(r['pm25'] - readings[i-1]['pm25']) for i, r in enumerate(readings) if i > 0]
    if not diffs:
        return 0.0
    variance = sum((d - sum(diffs)/len(diffs))**2 for d in diffs) / len(diffs)
    return round(math.exp(-variance / 100), 4)

def analyze_filtration_efficiency(contaminants, thresholds):
    # Core logic: assess how well system maintains levels below thresholds
    compliant_count = 0
    total_points = 0
    
    for entry in contaminants:
        # Check each contaminant against adaptive thresholds
        pm25_ok = entry['pm25'] <= thresholds['pm25_high']
        co2_ok = entry['co2'] <= thresholds['co2_high']
        voc_ok = entry['voc'] <= thresholds['voc_high']
        
        # All must be satisfied for compliance
        if pm25_ok and co2_ok and voc_ok:
            compliant_count += 1
        total_points += 1
    
    # Efficiency score as percentage
    efficiency = (compliant_count / total_points) * 100 if total_points > 0 else 0
    
    # Apply non-linear transformation based on humidity correlation
    humidity_set = {round(entry['humidity'], 2) for entry in contaminants}  # set operation
    adjustment_factor = 1.0 + (len(humidity_set) * 0.02)  # more diversity = better stability
    adjusted_efficiency = efficiency * adjustment_factor
    
    # Final score with penalty for high CO2 mean
    co2_mean = sum(e['co2'] for e in contaminants) / len(contaminants)
    penalty = 0.5 if co2_mean > 0.6 else 0.0
    
    return adjusted_efficiency - penalty

# Main execution flow
data = generate_synthetic_data()
normalized_data = normalize_readings(data)
anomaly_indices = detect_anomalies(normalized_data)  # unused result

# Dead code path: simulate HVAC diagnostics
resistance = calculate_airflow_resistance(duct_width=12, bends=3)
degradation = compute_filter_degradation_rate(0.95, 250, 23)
stability = evaluate_stability_factor(data)

threshold_map = build_threshold_map(normalized_data)
contaminant_levels = [
    {
        'pm25': nd['pm25'],
        'co2': nd['co2'],
        'voc': nd['voc'],
        'humidity': nd['humidity']
    }
    for nd in normalized_data  # list comprehension
]

filtration_score = analyze_filtration_efficiency(contaminant_levels, threshold_map)

# Print final answer
print(f"Result: {filtration_score}")