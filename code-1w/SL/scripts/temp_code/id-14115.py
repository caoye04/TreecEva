from collections import defaultdict, Counter
import itertools

# Simulated sensor array data from medical diagnostic device
def collect_sensor_data():
    raw_signals = [127, 64, 32, 15, 8, 4, 2, 1]
    timestamped = {i: val for i, val in enumerate(raw_signals)}
    return timestamped

# Irrelevant helper: analyzes noise patterns (dead-end)
def analyze_noise_pattern(data):
    noise_floor = 0
    for k, v in data.items():
        if v % 7 == 0:
            noise_floor += v >> 2
    return noise_floor * 3.14  # Red herring

# Core transformation: extracts bit-weighted health signature
def extract_health_signature(sensor_data):
    signature = 0
    for i, val in sensor_data.items():
        if i % 2 == 0:
            signature += val ^ (i << 2)
        else:
            signature -= val & (i << 1)
    return signature

# Baseline calibration using historical averages (partially relevant)
def generate_baseline_readings():
    history = [95, 102, 98, 110, 108]
    avg = sum(history) / len(history)
    readings = defaultdict(float)
    for i, h in enumerate(history):
        readings[f'day_{i}'] = h * 0.95
    readings['calibration_offset'] = avg * 0.05
    return dict(readings)

# Decoy function: looks important but unused in final path
def compute_thermal_decay():
    temp_seq = [t**2 for t in range(5)]
    decay = 0
    for t in temp_seq:
        decay += t // (t + 1) or 1
    return decay

# Data fusion engine with distractor logic
def fuse_signal_streams(primary, secondary):
    fused = []
    for a, b in itertools.zip_longest(primary.values(), secondary.values(), fillvalue=1):
        fused.append((a + b) % 17)
    # Distractor: unused transformation branch
    if len(fused) > 10:
        return [x * 2 for x in fused]
    return fused

# Main processing pipeline
def process_metrics(health_sig, baselines):
    # Step 1: Normalize signature with modulo wrap
    normalized = abs(health_sig) % 1000
    
    # Step 2: Extract baseline magnitude
    base_total = sum(baselines.values())
    
    # Step 3: Apply synthetic gain factor (misleading intermediate)
    gain_factor = base_total / (normalized or 1)
    adjusted = normalized * 1.05
    
    # Step 4: Bit manipulation on adjusted value
    bit_probe = int(adjusted) ^ 0b110101
    bit_probe = (bit_probe << 2) & 0xFFFF
    
    # Step 5: Use Counter to simulate fault pattern matching
    digits = [int(d) for d in str(bit_probe)]
    freq = Counter(digits)
    mode_val = freq.most_common(1)[0][1]  # frequency of most common digit
    
    # Step 6: Inject decoy logic (never alters output)
    decoy_shift = 0
    for d in digits:
        if d in {0, 1, 7}:
            decoy_shift += d | 5
    decoy_shift = decoy_shift << 10  # buried and unused
    
    # Step 7: Final computation combining multiple concepts
    result = bit_probe - mode_val * 17
    
    # Step 8: Conditional adjustment based on parity (actually deterministic)
    if sum(digits) % 2 == 0:
        result -= 23
    else:
        result += 19
    
    # Step 9: Apply redundant scaling (fixed path)
    final_score = result * 2
    
    # Step 10: Final offset using set operations (distractor-heavy)
    ref_set = {1, 2, 4, 8, 16, 32}
    probe_set = {d for d in digits if d < 10}
    overlap = ref_set.intersection(probe_set)
    penalty = sum(overlap) * 3  # Looks meaningful, actually fixed
    
    final_diagnostic = final_score - penalty
    return final_diagnostic

# Orchestration sequence
if __name__ == '__main__':
    # Collect real data
    sensor_log = collect_sensor_data()
    
    # Generate derived values (some irrelevant)
    noise_analysis = analyze_noise_pattern(sensor_log)  # stored but unused
    health_signature = extract_health_signature(sensor_log)
    baseline_readings = generate_baseline_readings()
    
    # Fuse streams (result not used in final calculation)
    fused_diagnostics = fuse_signal_streams(sensor_log, baseline_readings)
    
    # Compute thermal (completely decoy)
    thermal_profile = compute_thermal_decay()
    
    # Critical execution point
    final_diagnostic = process_metrics(health_signature, baseline_readings)
    
    print(f"Result: {final_diagnostic}")