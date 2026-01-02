import math

# Simulated sensor data processing with diagnostic analysis
def acquire_signal():
    raw_samples = [i * 0.1 for i in range(100)]
    return list(map(lambda x: math.sin(x) + 0.5 * math.cos(3*x), raw_samples))

# Irrelevant transformation - decoy function
def deprecated_filter(data):
    temp = [x for x in data if x > 0]
    smoothed = []
    for i in range(len(temp)):
        if i == 0 or i == len(temp)-1:
            smoothed.append(temp[i])
        else:
            smoothed.append((temp[i-1] + temp[i] + temp[i+1]) / 3)
    return smoothed  # Never used

# Data normalization (relevant)
def normalize_signal(signal):
    min_val, max_val = min(signal), max(signal)
    if max_val - min_val == 0:
        return [0] * len(signal)
    return [(x - min_val) / (max_val - min_val) for x in signal]

# Frequency domain approximation (relevant)
def compute_spectral_energy(signal):
    energy = 0
    for i, x in enumerate(signal):
        phase = math.sin(i * 0.5)
        magnitude = abs(x)
        energy += magnitude * (1 + phase) if phase > 0 else magnitude * (1 - phase)
    return energy / len(signal)

# Character pattern extraction from metadata - red herring
def extract_headers():
    headers = ['A', 'B', 'C', 'D']
    code_map = {h: ord(h) * 2 for h in headers}
    checksum = sum(v % 7 for v in code_map.values())  # Distractor computation
    return ''.join(headers), checksum  # Unused return

# Core transformation pipeline
def transform_signal(signal):
    # Apply moving window integration
    integrated = []
    window_size = 5
    for i in range(len(signal) - window_size + 1):
        segment = signal[i:i + window_size]
        integral = sum(segment) * 0.1  # Riemann approx
        integrated.append(integral)
    
    # Decoy bit manipulation - looks important but unused
    masked_values = []
    for x in integrated:
        bits = int(x * 1000) & 0xFF
        flipped = bits ^ 0xAA
        masked_values.append(flipped | 0x0F)
    
    # Actual relevant transformation
    return [x * 1.25 for x in integrated[:80]]  # Truncate and scale

# Diagnostic analyzer (target function)
def analyze_pattern(data):
    threshold = 0.75
    above_count = len([x for x in data if x > threshold])
    below_count = len([x for x in data if x < threshold * 0.5])
    
    # Complex conditional expression with nested logic
    base_score = above_count * 2 - below_count
    adjustment = 0
    
    # Misleading control flow with dead branches
    if len(data) % 7 == 0:
        adjustment += 10
    elif len(data) > 1000:  # Impossible condition
        adjustment -= 5
    else:
        adjustment = -3  # Always taken but looks suspicious
    
    # Critical calculation path
    if base_score > 0:
        adjustment += int(math.log(base_score + 1) * 4)
    
    final_score = base_score + adjustment
    
    # Redundant set operation - distractor
    unique_segments = set([int(x * 10) for x in data])
    overlap_check = len(unique_segments.intersection({1, 2, 5, 7, 8}))
    dummy_correction = overlap_check * 0.3  # Computed but not used
    
    return final_score

# Secondary data processor - dead end
def generate_report(signal):
    report_data = {}
    report_data['peak'] = max(signal)
    report_data['entropy'] = -sum([x * math.log(abs(x) + 1e-8) for x in signal])
    report_data['class'] = 'TYPE_A' if report_data['peak'] > 0.5 else 'TYPE_B'
    return report_data  # Never called

# Main execution flow
if __name__ == '__main__':
    # Step 1: Acquire raw signal
    sensor_input = acquire_signal()
    
    # Step 2: Normalize (relevant)
    calibrated_signal = normalize_signal(sensor_input)
    
    # Step 3: Extract headers - irrelevant side computation
    metadata, meta_checksum = extract_headers()  # Result ignored
    temp_flag = meta_checksum > 10
    
    # Step 4: Transform signal (relevant)
    transformed_data = transform_signal(calibrated_signal)
    
    # Step 5: Compute spectral energy (partially relevant for context)
    energy_profile = compute_spectral_energy(calibrated_signal)
    
    # Step 6: Analyze pattern - KEY STATEMENT
    final_diagnostic = analyze_pattern(transformed_data)
    
    # Print result as required
    print(f"Target result: {final_diagnostic}")