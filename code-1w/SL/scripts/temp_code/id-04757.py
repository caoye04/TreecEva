from collections import defaultdict
import math

# Simulated sensor data aggregation (irrelevant but realistic distractor)
sensor_logs = [
    'TEMP:72.1|HUM:45|PRESS:30.12',
    'TEMP:73.5|HUM:47|PRESS:30.05',
    'TEMP:69.8|HUM:52|PRESS:30.22'
]

# Parse logs into structured format (partially relevant preprocessing)
def parse_log_entry(entry):
    fields = entry.split('|')
    parsed = {}
    for f in fields:
        k, v = f.split(':')
        parsed[k] = float(v)
    return parsed

# Irrelevant transformation: convert to string summaries
def summarize_conditions(data_list):
    summaries = []
    for record in data_list:
        temp = record.get('TEMP', 0)
        hum = record.get('HUM', 0)
        if temp > 70:
            cond = 'warm'
        elif temp < 70:
            cond = 'cool'
        else:
            cond = 'neutral'
        summaries.append(f'It was {cond} with {hum}% humidity')
    return summaries

# Decoy function: appears useful but unused
def calculate_stress_index(readings):
    stress = 0
    for r in readings:
        stress += abs(r.get('TEMP', 70) - 70) * r.get('HUM', 50)
    return stress / len(readings) if readings else 0

# Core health metric processor (actually used)
def analyze_risk_level(value, baseline, severity_map):
    deviation = abs(value - baseline)
    for limit, level in sorted(severity_map.items()):
        if deviation <= limit:
            return level
    return max(severity_map.values())

# Real processing chain
baseline_temps = defaultdict(lambda: 70.0)
baseline_temps['core'] = 98.6
baseline_temps['ambient'] = 75.0

# Complex conditional mapping (mixed logic and arithmetic)
thresh_map = {
    1.0: 1,
    2.5: 2,
    5.0: 3,
    10.0: 4
}

# Simulated incoming health packet (mix of relevant and irrelevant fields)
health_data = [
    {'patient_id': 'A1001', 'core_temp': 101.2, 'heart_rate': 88, 'o2_sat': 97},
    {'patient_id': 'A1002', 'core_temp': 96.1, 'heart_rate': 62, 'o2_sat': 95},
    {'patient_id': 'A1003', 'core_temp': 103.5, 'heart_rate': 110, 'o2_sat': 88}
]

# Dead code path: never invoked
obsolete_fields = ['resp_rate', 'glucose']
legacy_transform = lambda x: x * 0.85 + 12

# Auxiliary diagnostic calculator (some components used, others not)
def extract_vital_signs(records):
    signs = []
    for r in records:
        # Extract only core_temp for actual use
        vital = {
            'temp': r['core_temp'],
            'hr': r['heart_rate'],  # Collected but unused
            'o2': r['o2_sat']      # Collected but unused
        }
        signs.append(vital)
    return signs

# Main processing pipeline
vital_signs = extract_vital_signs(health_data)

# Bit manipulation red herring (no actual impact)
def obfuscate_id(patient_id):
    if not patient_id.startswith('A'):
        return patient_id
    num_part = int(patient_id[1:])
    masked = (num_part ^ 0xFF) + 1234
    return f"X{masked}"

# Map patient IDs using decoy function (result unused)
encoded_ids = [obfuscate_id(d['patient_id']) for d in health_data]

# Actual risk analysis engine
def process_metrics(signs, thresholds):
    total_risk = 0.0
    critical_count = 0
    
    for sign in signs:
        # Only temperature is analyzed
        risk_level = analyze_risk_level(sign['temp'], 98.6, thresholds)
        total_risk += risk_level
        
        # Additional logic: flag extreme cases
        if sign['temp'] > 102.0:
            # Apply multiplicative surge
            surge_factor = (sign['temp'] - 102.0) / 2.0
            total_risk += math.ceil(surge_factor)
            critical_count += 1
    
    # Final diagnostic combines multiple concepts
    adjustment = 3 if critical_count >= 2 else (1 if critical_count == 1 else 0)
    base_score = total_risk * 100
    final_score = base_score + (adjustment * 50)
    
    # String method distraction (meaningless formatting)
    label = f"DX-{int(final_score)}".upper().replace('DX', 'DIAG')
    
    # Return only numeric component as answer
    return int(final_score)

# Execute key statement
final_diagnostic = process_metrics(vital_signs, thresh_map)

# Print result for extraction
print(f"Result: {final_diagnostic}")