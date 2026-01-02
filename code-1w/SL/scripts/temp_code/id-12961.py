from collections import defaultdict, Counter
import math

# Simulated sensor data: timestamp -> readings
raw_readings = [
    (1001, {'temp': 36.8, 'hr': 72, 'spo2': 98}),
    (1002, {'temp': 37.1, 'hr': 75, 'spo2': 97}),
    (1003, {'temp': 37.4, 'hr': 79, 'spo2': 96}),
    (1004, {'temp': 37.6, 'hr': 83, 'spo2': 95}),
    (1005, {'temp': 38.0, 'hr': 88, 'spo2': 93}),
    (1006, {'temp': 38.3, 'hr': 92, 'spo2': 92}),
    (1007, {'temp': 38.7, 'hr': 96, 'spo2': 91}),
    (1008, {'temp': 39.0, 'hr': 100, 'spo2': 90})
]

# Irrelevant baseline catalog (distractor)
baseline_catalog = {
    'normal': {'range_temp': (36.1, 37.2), 'range_hr': (60, 100)},
    'elevated': {'range_temp': (37.3, 38.0), 'range_hr': (80, 110)},
    'high': {'range_temp': (38.1, 40.0), 'range_hr': (90, 120)}
}

# Real threshold rules (used in logic)
def get_thresholds(severity):
    base = {'temp': 38.0, 'hr': 90, 'spo2': 92}
    if severity == 'critical':
        base['temp'] += 0.5
        base['hr'] -= 5
        base['spo2'] += 3
    return base

def analyze_trend(data_list):
    trend_scores = defaultdict(float)
    temp_changes = []
    hr_changes = []
    
    for i in range(1, len(data_list)):
        prev = data_list[i-1][1]
        curr = data_list[i][1]
        temp_changes.append(curr['temp'] - prev['temp'])
        hr_changes.append(curr['hr'] - prev['hr'])
    
    # Compute average change rates
    avg_temp_change = sum(temp_changes) / len(temp_changes)
    avg_hr_change = sum(hr_changes) / len(hr_changes)
    
    # Heuristic scoring (not used directly but looks important)
    trend_scores['worry_index'] = avg_temp_change * 2 + avg_hr_change * 0.5
    
    # Actual signal: count how many consecutive entries exceed base thresholds
    sustained_count = 0
    for entry in data_list:
        reading = entry[1]
        if reading['temp'] > 37.5 and reading['hr'] > 85 and reading['spo2'] < 94:
            sustained_count += 1
        else:
            sustained_count = 0  # reset if broken
    
    trend_scores['sustained_abnormal'] = sustained_count
    return trend_scores

# Data transformation pipeline (mixed use)
def normalize_readings(raw):
    result = []
    for ts, values in raw:
        norm_vals = {k: round(v, 1) for k, v in values.items()}
        # Add synthetic feature (unused distractor)
        norm_vals['temp_bin'] = int((norm_vals['temp'] - 35) * 10)
        result.append((ts, norm_vals))
    return result

# Decoy function - appears useful but unused
def compute_bmi(weight_kg, height_m):
    return round(weight_kg / (height_m ** 2), 2)

# Another decoy - complex but irrelevant
class RiskAssessor:
    def __init__(self):
        self.weights = {'temp': 0.4, 'hr': 0.35, 'spo2': -0.25}
    
    def score(self, vitals):
        return sum(v * self.weights[k] for k, v in vitals.items())

# Core processing function with key logic hidden among distractions
def process_metrics(data_sequence, criteria):
    window_size = 4
    alerts = 0
    history_log = []
    cumulative_stress = 0.0
    
    # Simulate rolling window analysis
    for i in range(len(data_sequence)):
        window = data_sequence[max(0, i - window_size + 1):i + 1]
        
        # Compute rolling statistics
        temps = [pt[1]['temp'] for pt in window]
        hrs = [pt[1]['hr'] for pt in window]
        spo2s = [pt[1]['spo2'] for pt in window]
        
        avg_temp = sum(temps) / len(temps)
        peak_hr = max(hrs)
        min_spo2 = min(spo2s)
        
        # Trigger condition based on combined criteria
        if (avg_temp > criteria['temp'] and 
            peak_hr > criteria['hr'] and 
            min_spo2 < criteria['spo2']):
            alerts += 1
            
        # Distractor: build fake log
        log_entry = f"W{len(window)}: T{avg_temp:.1f}/H{peak_hr}/S{min_spo2}"
        history_log.append(log_entry.upper())
        
        # Hidden accumulator: only odd-indexed windows contribute
        if i % 2 == 1:
            stress_factor = avg_temp * (peak_hr / (min_spo2 + 1))
            cumulative_stress += stress_factor
    
    # Final decision logic (non-obvious)
    # The answer is derived from cumulative_stress rounded to nearest integer
    final_score = int(round(cumulative_stress))
    
    # Other variables that look important but aren't the answer
    summary_stats = Counter(history_log)
    diagnostic_code = hash(str(summary_stats)) % 1000
    
    return final_score

# Preparation steps
health_data = normalize_readings(raw_readings)
target_thresholds = get_thresholds('standard')  # Default call

# Override for actual needed threshold
thresholds = {'temp': 37.8, 'hr': 87, 'spo2': 93}

# Critical execution point
final_diagnostic = process_metrics(health_data, thresholds)

# Print result as required
print(f"Target result: {final_diagnostic}")