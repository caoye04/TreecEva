from collections import defaultdict, Counter
import math

# Simulated quantum sensor readings and system diagnostics
def collect_sensor_data():
    readings = []
    for i in range(180):
        phase = math.sin(math.radians(i)) * math.cos(math.radians(i * 1.5))
        noise = (i ** 0.5) % 1
        readings.append(round(phase + noise * 0.1, 4))
    return readings

def apply_calibration(data, factor=0.987):
    # Irrelevant calibration function (not actually used in final path)
    return [x * factor for x in data]

def compute_entropy(seq):
    # Misleading entropy calculation (dead code path)
    counter = Counter(seq)
    total = len(seq)
    entropy = -sum((count / total) * math.log2(count / total) for count in counter.values())
    return round(entropy, 4)

def extract_patterns(data):
    # Extracts rising/falling edge patterns - partially relevant
    transitions = []
    for i in range(1, len(data)):
        if data[i] > data[i-1] + 0.01:
            transitions.append(1)
        elif data[i] < data[i-1] - 0.01:
            transitions.append(-1)
        else:
            transitions.append(0)
    return transitions

def detect_anomalies(patterns):
    # Detects anomaly sequences in transition patterns
    anomalies = 0
    for i in range(len(patterns) - 3):
        window = patterns[i:i+4]
        if window == [1, -1, 1, -1]:  # Oscillation pattern
            anomalies += 1
    return anomalies

def evaluate_stability_score(transitions):
    # Another decoy function - never called
    score = 0
    for t in transitions:
        if t == 0:
            score += 0.1
    return round(score, 3)

def aggregate_diagnostics(flags):
    # Processes system flags using defaultdict (red herring)
    report = defaultdict(int)
    for flag in flags:
        report[flag] += 1
    # Key line: only 'CRITICAL' matters
    return report['CRITICAL']

def analyze_quantum_coherence(readings):
    # Real but distracting analysis
    coherent_segments = 0
    segment_sum = 0.0
    for val in readings:
        segment_sum += val
        if abs(segment_sum) > 0.5:
            coherent_segments += 1
            segment_sum = 0.0
    return coherent_segments

def generate_diagnostic_summary(coherence, anomalies, critical_count):
    # Complex transformation with distractor logic
    base_score = coherence * 17
    adjustment = anomalies * 3
    penalty = critical_count * 50
    
    # Obscure normalization rule
    temp = base_score + adjustment - penalty
    if temp < 0:
        temp = abs(temp) * 1.5
    
    # Final transformation
    result = int((temp * 1.23) + 7)
    
    # Dead branch - never executed due to logic
    if result == 42:
        result = 0  # Easter egg that doesn't trigger
    
    return result

def analyze_system_state(readings, flags):
    # Core logic with distractions
    
    # Step 1: Extract patterns from raw data
    patterns = extract_patterns(readings)
    
    # Step 2: Detect oscillation anomalies
    anomaly_count = detect_anomalies(patterns)
    
    # Step 3: Count critical flags
    critical_flag_count = flags.count('CRITICAL')
    
    # Step 4: Analyze coherence (actually used)
    coherence_units = analyze_quantum_coherence(readings)
    
    # Step 5: Generate summary (this is where answer is computed)
    final_score = generate_diagnostic_summary(coherence_units, anomaly_count, critical_flag_count)
    
    # Distractor variables
    stability_metric = sum(1 for x in patterns if x == 0)
    entropy_value = compute_entropy(readings[:50])
    calibration_offset = 0.987
    system_age_years = 7
    maintenance_cycles = 42
    
    # Unused intermediate results
    unused_report = aggregate_diagnostics(flags)
    dummy_lambda = lambda x: x ** 2 - x
    processed_data = list(map(dummy_lambda, [1, 2, 3]))  # Dead computation
    
    # Zip and enumerate usage (meaningful but obscured)
    indexed_patterns = list(enumerate(zip(patterns[::5], patterns[1::5])))
    pattern_pairs = [p for i, p in indexed_patterns if i % 3 == 0]
    
    # Final diagnostic is based on the summary
    final_diagnostic = final_score
    
    # More red herrings
    security_token = 'SEC-789XYZ'
    last_reboot = '2023-11-05'
    firmware_version = 'v2.4.1'
    
    return final_diagnostic

# Main execution flow
if __name__ == '__main__':
    # Collect real data
    quantum_readings = collect_sensor_data()
    
    # System flag log (contains distractions)
    system_flags = [
        'NORMAL', 'NORMAL', 'WARNING', 'NORMAL',
        'CRITICAL', 'NORMAL', 'INFO', 'WARNING',
        'CRITICAL', 'CRITICAL', 'NORMAL', 'NORMAL',
        'DIAGNOSTIC', 'CALIBRATING', 'CRITICAL'  # 4 CRITICAL
    ]
    
    # Spurious data collection
    temperature_logs = [22.1, 22.3, 21.9, 22.0, 22.5, 23.1, 22.8]
    pressure_samples = [101.3, 101.5, 101.2, 101.8, 102.1]
    
    # Irrelevant preprocessing
    normalized_temps = [t - 20 for t in temperature_logs]
    adjusted_pressures = [p * 1.001 for p in pressure_samples]
    
    # Key execution point
    final_diagnostic = analyze_system_state(quantum_readings, system_flags)
    
    # Output result
    print(f"Result: {final_diagnostic}")