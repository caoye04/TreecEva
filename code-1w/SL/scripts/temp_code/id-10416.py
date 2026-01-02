import math

# Sensor calibration constants (irrelevant to final result but look important)
CALIBRATION_OFFSETS = {'sensor_a': 0.02, 'sensor_b': -0.01, 'sensor_c': 0.05}
def calibrate(value, sensor):
    return value + CALIBRATION_OFFSETS.get(sensor, 0)

def generate_sequence(n):
    # Dead-end function: generates Fibonacci-like sequence but never used
    seq = [1, 1]
    for i in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq

def evaluate_stability(risk_factor, history):
    # Distractor logic: looks meaningful but unused
    if risk_factor > 0.7:
        return sum(history) / len(history) > 0.5
    return False

# Simulated raw sensor inputs
raw_readings = [
    {'time': 0, 'temp': 36.5, 'pulse': 75, 'oximetry': 98},
    {'time': 1, 'temp': 37.1, 'pulse': 82, 'oximetry': 97},
    {'time': 2, 'temp': 38.3, 'pulse': 95, 'oximetry': 96},
    {'time': 3, 'temp': 38.7, 'pulse': 103, 'oximetry': 94},
    {'time': 4, 'temp': 39.0, 'pulse': 110, 'oximetry': 93}
]

# Irrelevant transformation: creates a set but not used in main path
unique_temps = {round(record['temp']) for record in raw_readings}

# Predefined thresholds for analysis (used later)
threshold_map = {
    'fever': (37.5, 39.5),
    'tachycardia': (90, float('inf')),
    'hypoxemia': (0, 95)
}

# Conditional expression with distractor variables
status_flags = [
    'critical' if r['temp'] > 39 or r['pulse'] > 100 else 'moderate'
    for r in raw_readings
]

# Unused recursive function - red herring
def binary_search(arr, low, high, target):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, low, mid - 1, target)
    else:
        return binary_search(arr, mid + 1, high, target)

# Main processing pipeline
processed_data = []
for reading in raw_readings:
    entry = {
        'timestamp': reading['time'],
        'vitals': {
            'temperature': reading['temp'],
            'heart_rate': reading['pulse'],
            'oxygen_sat': reading['oximetry']
        },
        'flags': {}
    }
    
    # Evaluate conditions using threshold map
    temp = reading['temp']
    pulse = reading['pulse']
    o2 = reading['oximetry']
    
    # Direct assignments with conditional expressions
    entry['flags']['fever'] = threshold_map['fever'][0] <= temp <= threshold_map['fever'][1]
    entry['flags']['tachycardia'] = pulse >= threshold_map['tachycardia'][0]
    entry['flags']['hypoxemia'] = o2 < threshold_map['hypoxemia'][1]
    
    # Composite condition (relevant only if all three are true)
    entry['flags']['triage_high'] = all([
        entry['flags']['fever'],
        entry['flags']['tachycardia'],
        entry['flags']['hypoxemia']
    ])
    
    processed_data.append(entry)

# Secondary analysis: counts how many readings triggered triage_high
triage_count = sum(1 for d in processed_data if d['flags']['triage_high'])

# Irrelevant combinatorics computation - looks sophisticated but unused
from itertools import combinations
candidate_pairs = list(combinations([d['timestamp'] for d in processed_data], 2))

# Another decoy variable
baseline_avg = sum(d['vitals']['temperature'] for d in processed_data[:2]) / 2

# Core diagnostic logic (depends on triage_count and static map)
def analyze_readings(data, thresholds):
    # Extract all triage_high flags
    active_flags = [rec['flags']['triage_high'] for rec in data]
    
    # Compute severity score based on pattern
    severity = 0
    for i, flag in enumerate(active_flags):
        if flag:
            # Weighted by time (later = more severe)
            severity += (i + 1) * 25
    
    # Additional penalty if fever range is exceeded at end
    last_temp = data[-1]['vitals']['temperature']
    if last_temp > thresholds['fever'][1]:
        severity += 50
    
    # Diagnostic mapping via dictionary lookup
    diagnosis_map = {0: 100, 25: 200, 50: 300, 75: 400, 100: 500, 125: 600}
    mapped_value = diagnosis_map.get(severity, 0)
    
    # Final transformation
    normalized = int(math.sqrt(mapped_value ** 2 / 2.5) if mapped_value else 0)
    
    # Final diagnostic value
    return normalized + 13

# Execute key statement
final_diagnostic = analyze_readings(processed_data, threshold_map)

# Print result as required
print(f"Result: {final_diagnostic}")