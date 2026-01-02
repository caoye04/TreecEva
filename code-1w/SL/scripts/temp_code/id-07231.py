import math

# Simulated sensor data processing with embedded diagnostics
def collect_readings():
    raw_samples = [i * 0.5 + (i % 7) for i in range(30)]
    filtered = [x for x in raw_samples if x > 5 and x < 12]
    normalized = [round(x / max(filtered), 3) for x in filtered]
    return normalized

# Irrelevant auxiliary function – dead code path (red herring)
def deprecated_calibrate(data):
    adjustment = sum(data) / len(data)
    return [d - adjustment for d in data]

# Data transformation involving slicing and noise injection
def apply_window(signal):
    windowed = signal[5:] + signal[:5]  # Circular shift using slicing
    noise_floor = [math.sin(i * 0.3) * 0.1 for i in range(len(windowed))]
    perturbed = [round(a + b, 3) for a, b in zip(windowed, noise_floor)]
    return perturbed

# Misleading pattern matcher – never actually used in execution (decoy)
def detect_anomaly(sequence):
    threshold = 0.85
    anomalies = []
    for idx, val in enumerate(sequence):
        if abs(val - 0.5) > threshold:
            anomalies.append(idx)
    return anomalies

# Core recursive pattern analyzer
def analyze_pattern(seq):
    if len(seq) <= 1:
        return seq[0] if seq else 0
    
    mid = len(seq) // 2
    left_half = seq[:mid]
    right_half = seq[mid:]
    
    # Recursive analysis with bitwise influence
    left_val = analyze_pattern(left_half)
    right_val = analyze_pattern(right_half)
    
    # Weighted fusion with XOR-based modulation
    weight = (mid % 9) or 1
    combined = (left_val * 0.6) + (right_val * 0.4)
    modulated = combined ^ int(weight * 100)  # Bitwise XOR with scaled weight
    return round(modulated, 3)

# Secondary processing chain – appears relevant but unused (distraction)
def compute_entropy(data):
    freq_map = {}
    for x in data:
        key = int(x * 10)
        freq_map[key] = freq_map.get(key, 0) + 1
    total = len(data)
    entropy = -sum((count / total) * math.log2(count / total) for count in freq_map.values())
    return round(entropy, 3)

# Orchestration with red herrings and decoy variables
def main_pipeline():
    # Step 1: Collect and transform sensor readings
    readings = collect_readings()  # Initial dataset
    
    # Decoy assignment – looks important but unused later
    baseline_reference = sum(readings) / len(readings)
    
    # Step 2: Apply non-trivial transformation using slicing
    transformed_data = apply_window(readings)
    
    # Fake branching – condition always false (misleading control flow)
    if sum(transformed_data) < 0:
        transformed_data = deprecated_calibrate(transformed_data)
    
    # Redundant sorting – result not used
    sorted_diagnostic = sorted(transformed_data, reverse=True)
    temp_analysis = [x for x in sorted_diagnostic if x > 0.5]
    
    # Actual critical computation
    final_diagnostic = analyze_pattern(transformed_data)
    
    # Multiple irrelevant print statements (simulating debugging noise)
    # print(f'Debug: baseline={baseline_reference}')
    # print(f'Debug: entropy_score={compute_entropy(readings)}')
    # print(f'Debug: detected anomalies={detect_anomaly(transformed_data)}')
    
    # Final output
    print(f'Target result: {final_diagnostic}')

if __name__ == '__main__':
    main_pipeline()