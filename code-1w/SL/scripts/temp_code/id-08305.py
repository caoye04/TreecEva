from collections import defaultdict, Counter
import math

# Simulated IoT sensor data processing with diagnostic analysis
def collect_sensor_readings():
    readings = [
        ('temp', 36.8), ('hr', 74), ('spo2', 98),
        ('temp', 37.1), ('hr', 76), ('spo2', 97),
        ('temp', 37.5), ('hr', 80), ('spo2', 96),
        ('temp', 38.2), ('hr', 88), ('spo2', 95)
    ]
    return readings

def build_patient_profile(readings):
    profile = defaultdict(list)
    for sensor, value in readings:
        profile[sensor].append(value)
    
    # Irrelevant aggregation
    stats = {}
    for k, v in profile.items():
        stats[k + '_avg'] = sum(v) / len(v)
        stats[k + '_peak'] = max(v)
    
    # Distractor: unused complex structure
    decoy_matrix = [[i * j for j in range(5)] for i in range(5)]
    checksum = 0
    for row in decoy_matrix:
        for val in row:
            checksum ^= val  # Bitwise red herring
    
    return profile

def compute_therapeutic_index(data):
    # Fake calculation path
    baseline = {"metabolic_rate": 1.0, "vaso_dilation": 0.0}
    adjustment = 0
    for i in range(40):  # Loop with no real effect
        adjustment += (i * 0.01) if i % 5 == 0 else 0
    
    # Actual relevant but obscured logic
    temps = data['temp']
    elevated_count = sum(1 for t in temps if t > 37.0)
    return elevated_count * 1.5  # Hidden contribution

def evaluate_stress_markers(profile):
    hr_values = profile['hr']
    variability = sum(abs(hr_values[i+1] - hr_values[i]) for i in range(len(hr_values)-1))
    
    # Decoy statistical moment
    mean_hr = sum(hr_values) / len(hr_values)
    variance = sum((x - mean_hr) ** 2 for x in hr_values) / len(hr_values)
    skewness_proxy = sum((x - mean_hr) ** 3 for x in hr_values)  # Unused
    
    # Real logic buried here
    stress_score = 0
    if variability > 10:
        stress_score += 3
    if max(hr_values) >= 85:
        stress_score += 2
    return stress_score

def assess_oxygen_efficiency(profile):
    spo2_vals = profile['spo2']
    trend = sum(spo2_vals[i] < spo2_vals[i+1] for i in range(len(spo2_vals)-1))
    efficiency = 5 if trend <= 1 else 2  # Improving = bad? Contradictory hint
    
    # Fake ML-inspired block
    weights = [0.1, 0.3, 0.5, 0.7]
    bias = 0.0
    for w in weights:
        bias += math.log(abs(w) + 1e-8)  # Red herring computation
    
    return efficiency

def analyze_metrics(health_data, thresholds):
    # Core integration function with critical logic
    index = compute_therapeutic_index(health_data)
    stress = evaluate_stress_markers(health_data)
    oxy = assess_oxygen_efficiency(health_data)
    
    # Multiple distractions below
    summary = Counter()
    for k in health_data:
        summary[k + '_count'] = len(health_data[k])
    
    # Dead code path
    if False:
        temp_peaks = [t for t in health_data['temp'] if t > 40.0]
        summary['danger_count'] = len(temp_peaks)
    
    # Key logic embedded among noise
    base = index + stress
    modifier = 1
    if oxy < 4:
        modifier *= 2
    elif stress > 4:
        modifier *= 1.5
    
    intermediate = base * modifier
    
    # Final transformation
    final_diagnostic = int(intermediate + 0.5)  # Round to nearest int
    
    # Useless bit manipulation distraction
    flag = 0b1010
    for _ in range(3):
        flag = (flag << 1) ^ 0b1101
    
    return final_diagnostic

# Main execution flow
if __name__ == '__main__':
    raw_readings = collect_sensor_readings()
    patient_data = build_patient_profile(raw_readings)
    
    # Thresholds not actually used but look important
    clinical_thresholds = {
        'fever': 38.0,
        'tachycardia': 100,
        'hypoxia': 92
    }
    
    # Trigger point for question
    final_diagnostic = analyze_metrics(patient_data, clinical_thresholds)
    
    # Additional distraction: unused dictionary operations
    metadata_log = {}
    metadata_log['timestamp'] = '2023-08-17'
    metadata_log['version'] = 'v2.3-alpha'
    metadata_log['diagnostics'] = {'level': 'deep', 'scope': 'full'}
    metadata_log.update({'validated': False})
    
    print(f"Result: {final_diagnostic}")