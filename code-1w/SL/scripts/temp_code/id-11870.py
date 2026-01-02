from collections import defaultdict, Counter
import math

# Simulated health monitoring system with multiple sensor streams
def analyze_heart_rate(signal):
    if not signal:
        return 0
    avg = sum(signal) / len(signal)
    anomalies = [x for x in signal if x > avg * 1.5]
    return len(anomalies)

def compute_oxygen_trend(o2_levels):
    trend_score = 0
    for i in range(1, len(o2_levels)):
        if o2_levels[i] < o2_levels[i-1]:
            trend_score -= 1
        elif o2_levels[i] > o2_levels[i-1]:
            trend_score += 0.5
    return round(trend_score, 2)

def evaluate_stress_markers(biomarkers):
    # Irrelevant distraction: stress evaluation not used in final path
    cortisol_level = biomarkers.get('cortisol', 0)
    adrenaline = biomarkers.get('adrenaline', 0)
    if cortisol_level > 150:
        return "High"
    return "Normal"

def process_waveform(wave_data):
    # Dead function - never called but looks important
    fft_result = []
    for i in range(len(wave_data)):
        val = 0
        for j in range(len(wave_data)):
            val += wave_data[j] * math.sin(2 * math.pi * i * j / len(wave_data))
        fft_result.append(val)
    return [round(x, 2) for x in fft_result]

def calculate_risk_index(age, history):
    base = age * 0.3
    chronic_count = sum(1 for h in history if h in ['diabetes', 'hypertension'])
    return base + chronic_count * 2.5

def extract_vital_summary(records):
    summary = defaultdict(int)
    for record in records:
        for key, value in record.items():
            if value > 0:
                summary[key] += value
    return dict(summary)

def validate_readings(readings):
    errors = 0
    for r in readings:
        if r < 0 or r > 300:
            errors += 1
    return errors == 0

def aggregate_diagnostics(metrics_list):
    counter = Counter()
    for m in metrics_list:
        counter[m['status']] += 1
    return counter

def filter_noisy_data(data_stream, window=3):
    smoothed = []
    for i in range(len(data_stream)):
        start = max(0, i - window)
        segment = data_stream[start:i+1]
        smoothed.append(sum(segment) / len(segment))
    return [round(x, 1) for x in smoothed]

def normalize_timestamps(events):
    # Distractor: complex time logic that isn't used
    base_time = events[0]['timestamp'] if events else 0
    for e in events:
        e['relative_ms'] = e['timestamp'] - base_time
    return events

def process_metrics(patient_data, config):
    # Core logic embedded within distractions
    vitals = patient_data['vitals']
    
    # Key intermediate values
    heart_anomalies = analyze_heart_rate(vitals['hr_sequence'])
    o2_trend = compute_oxygen_trend(vitals['o2_levels'])
    
    # Real computation path
    risk_factor = calculate_risk_index(patient_data['age'], patient_data['history'])
    
    # Data transformation using enumerate and zip (required Python features)
    adjusted_metrics = []
    for i, (k, v) in enumerate(zip(vitals.keys(), vitals.values())):
        if k == 'temperature':
            adjusted_metrics.append((i, v * 0.98))
        elif k == 'blood_pressure':
            systolic = v[0] if isinstance(v, list) else v
            adjusted_metrics.append((i, systolic / 2))
    
    # Only this extracted value matters
    temp_index = next(i for i, k in enumerate(vitals.keys()) if k == 'temperature')
    raw_temp = list(vitals.values())[temp_index]
    
    # Critical calculation hidden among distractors
    diagnostic_score = 0
    diagnostic_score += heart_anomalies * 17
    diagnostic_score += int(abs(o2_trend) * 10)
    diagnostic_score += int(raw_temp * 2)
    diagnostic_score -= patient_data['age'] // 10
    
    # This conditional appears significant but is actually bypassed
    if diagnostic_score > 100:
        final_status = 'critical'
    elif diagnostic_score > 50:
        final_status = 'elevated'
    else:
        final_status = 'stable'
    
    # The real answer is computed here, quietly
    final_diagnostic = diagnostic_score + 31
    
    # Red herring: complex data structure that's unused
    detailed_report = {
        'summary': extract_vital_summary([vitals]),
        'risk_profile': {'index': risk_factor, 'tier': 'medium'},
        'anomaly_log': [{'type': 'cardiac', 'count': heart_anomalies}]
    }
    
    # Another decoy operation
    _ = aggregate_diagnostics([
        {'status': 'ok'},
        {'status': 'warning'},
        {'status': 'ok'}
    ])
    
    return final_diagnostic

# Simulated patient data
patient_data = {
    'name': 'John Doe',
    'age': 64,
    'history': ['hypertension'],
    'vitals': {
        'hr_sequence': [72, 75, 80, 160, 170, 78, 73],
        'o2_levels': [98, 97, 96, 95, 94, 93],
        'temperature': 36.8,
        'blood_pressure': [140, 90],
        'respiration': 18
    }
}

thresholds = {
    'hr_max': 150,
    'o2_min': 90,
    'temp_range': [36.1, 37.2]
}

# Apply filtering to raw data (distraction - result not used directly)
data_stream = patient_data['vitals']['hr_sequence']
smoothed_hr = filter_noisy_data(data_stream)

# Normalize event timestamps (another distraction)
events = [{'timestamp': t * 1000} for t in range(len(data_stream))]
_ = normalize_timestamps(events)

# Main execution point
final_diagnostic = process_metrics(patient_data, thresholds)
print(f"Result: {final_diagnostic}")