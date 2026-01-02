import itertools

# Simulated sensor data preprocessing with red herrings
def acquire_signal():
    raw_samples = [i * 0.7 + ((i % 3) ** 2) for i in range(18)]
    offset_correction = sum([x for x in raw_samples if x > 5]) / 7  # Distractor
    filtered_noise = list(map(lambda x: x * 0.9, raw_samples))
    return filtered_noise

# Irrelevant auxiliary function (dead path)
def calibrate_device(mode="auto"):
    calibration_matrix = [[i ^ j for j in range(6)] for i in range(6)]
    checksum = sum(itertools.chain(*calibration_matrix)) % 100
    return False  # Never used

# Core transformation with embedded distractors
def preprocess_signal(signal):
    amplified = [s * 1.2 for s in signal]
    decimated = amplified[::3]  # Take every third sample
    
    # Distractor: energy calculation not used later
    window_energy = [x**2 for x in decimated]
    avg_energy = sum(window_energy) / len(window_energy) if window_energy else 0
    
    # Bit manipulation red herring
    magic_shift = (len(decimated) << 2) ^ 5
    dummy_mask = magic_shift & 0xFF
    
    # Actual relevant transformation
    normalized = [(x - min(decimated)) / (max(decimated) - min(decimated)) for x in decimated]
    scaled_integers = [int(x * 1000) for x in normalized]
    return scaled_integers

# Secondary analysis with conditional logic and decoy control flow
def compute_health_index(data):
    if len(data) == 0:
        return -1
    
    # Summation with modular arithmetic distraction
    total = sum(data)
    mod_cycle = total % 7
    cycle_map = {i: total >> i for i in range(7)}  # Unused mapping
    
    # Real logic: count values above median threshold
    sorted_data = sorted(data)
    median_val = sorted_data[len(sorted_data)//2]
    critical_count = len([v for v in data if v > median_val + 50])
    
    # Decoy branching
    if mod_cycle in {3, 5}:
        adjustment = sum([i * 2 for i in range(mod_cycle)])  # Dead code
    elif mod_cycle < 4:
        adjustment = (mod_cycle ** 2) * 10  # Also irrelevant
    else:
        adjustment = 0  # Placeholder to mislead
    
    return critical_count * 100  # Only this matters

# Final diagnostic with tuple unpacking and conditional expression
def analyze_signal(data):
    base_score = compute_health_index(data)
    
    # Destructuring assignment (partly irrelevant)
    first, *middle, last = data
    peak_to_peak = last - first
    
    # Conditional expression with misleading alternative
    secondary_metric = peak_to_peak * 2 if base_score > 200 else peak_to_peak // 4
    
    # Real final computation
    trend_bias = sum(1 for a, b in zip(data, data[1:]) if b > a) - sum(1 for a, b in zip(data, data[1:]) if b < a)
    
    # Key combination
    final_value = base_score + (secondary_metric // 3) + (trend_bias * 10)
    
    # Dummy dictionary construction (distractor)
    diagnostics = {
        'raw_length': len(data),
        'first_sample': first,
        'checksum': (first ^ last) & 0xFFFF,
        'dummy_flag': False
    }
    
    return final_value

# Execution flow
if __name__ == "__main__":
    signal = acquire_signal()
    processed_data = preprocess_signal(signal)
    
    # Variables introduced to distract
    baseline_ref = sum(processed_data[:5]) / 5
    fluctuation_index = max(processed_data) - min(processed_data)
    entropy_approx = len(set(bin(x)[2:] for x in processed_data))  # Fake complexity
    
    final_diagnostic = analyze_signal(processed_data)
    print(f"Result: {final_diagnostic}")