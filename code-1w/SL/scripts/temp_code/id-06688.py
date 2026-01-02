import math

# Simulated sensor data processing with embedded diagnostics
def collect_readings():
    raw_samples = [0.1, 0.4, 0.9, 1.6, 2.5, 3.6, 4.9, 6.4, 8.1, 10.0]
    offset = 0.05
    adjusted = [x + offset for x in raw_samples]
    return adjusted

# Irrelevant helper - distractor function
def calculate_entropy(data):
    total = 0.0
    for x in data:
        if x > 0: total -= x * math.log(x)
    return total  # unused later

# Data transformation pipeline
def filter_noise(signal, threshold=0.5):
    filtered = []
    for val in signal:
        if val >= threshold:
            filtered.append(val ** 0.5)
    return filtered

# Symbolic feature extraction (mix of string and numeric)
def extract_signatures(values):
    signatures = []
    for v in values:
        code_point = int(v * 10) % 26 + ord('A')
        char_id = chr(code_point)
        # Conditional expression used here
        status_flag = 'OK' if v > 2 else 'LOW'
        signatures.append(f'{char_id}:{status_flag}')
    return signatures

# Secondary analysis with red herring logic
def assess_stability(indices):
    trend_score = 0
    for i in range(1, len(indices)):
        if indices[i] > indices[i-1]:
            trend_score += 1
        else:
            trend_score -= 0.5
    # This function looks important but isn't part of final result
    return abs(trend_score) > 3

# Core diagnostic computation
def compute_coherence(mag_vals):
    sum_sq = sum([v**2 for v in mag_vals])
    linear_sum = sum(mag_vals)
    n = len(mag_vals)
    if n == 0: return 0
    return (sum_sq / n) ** 0.5 - (linear_sum / n)

# Higher-level processor with multiple steps
def generate_profile(clean_signal):
    profile_data = {}
    
    # Distractor block: complex but unused structure
    temp_grid = [[i+j for j in range(3)] for i in range(3)]
    checksum = sum([sum(row) for row in temp_grid])  # dead end
    
    # Actual relevant computations
    magnitude = [abs(x) for x in clean_signal]
    active_segments = [m for m in magnitude if m > 1.0]
    
    coherence = compute_coherence(active_segments)
    
    # String manipulation side-channel
    label_base = "DIAG-X"
    version_tag = label_base.replace('X', f'{len(active_segments)}')
    
    profile_data['coherence'] = coherence
    profile_data['label'] = version_tag
    profile_data['count'] = len(active_segments)
    
    return profile_data

# Final analyzer combining multiple concepts
def analyze_signal(data_packet):
    # Extract numeric component
    values = [float(d.split(':')[0]) for d in data_packet if ':' in d]
    
    # Character counting distraction
    all_chars = ''.join(data_packet)
    unique_chars = len(set(all_chars))  # looks useful, not actually used
    
    # Linear search for control flag
    critical_index = -1
    for idx, item in enumerate(data_packet):
        if 'Z:OK' in item:
            critical_index = idx
            break
    
    # Main computation path
    if critical_index == -1:
        base_score = sum(values) * 0.7
    else:
        base_score = sum(values[:critical_index]) * 0.9
    
    adjustment = math.sin(math.pi * len(values) / 4)
    final_score = base_score + adjustment
    
    return int(final_score * 100) / 100  # rounded to two decimals

# Execution flow with layered interference
if __name__ == '__main__':
    # Step 1: Collect raw input
    readings = collect_readings()
    
    # Step 2: Filter out low-amplitude noise
    purified = filter_noise(readings, threshold=0.6)
    
    # Step 3: Extract symbolic tags (string manipulation)
    tags = extract_signatures(purified)
    
    # Step 4: Generate full diagnostic profile (contains decoy operations)
    profile = generate_profile(purified)
    
    # Step 5: Assess system stability (red herring call)
    is_stable = assess_stability(purified)  # result ignored
    
    # Step 6: Compute entropy for no reason (dead-end computation)
    _ = calculate_entropy(purified)  # completely irrelevant
    
    # Step 7: Introduce a fake emergency override (distractor logic)
    emergency_mode = False
    if len(tags) > 5 and 'D:OK' in tags:
        emergency_mode = True  # never used
    
    # Step 8: Inject Z:OK tag to influence control flow
    tags.append('Z:OK')  # crucial for conditional logic later
    
    # Step 9: Process finalized data structure
    processed_data = tags  # this becomes input to final analysis
    
    # Step 10: Run final diagnostic (KEY STATEMENT)
    final_diagnostic = analyze_signal(processed_data)
    
    # Output target result
    print(f"Result: {final_diagnostic}")