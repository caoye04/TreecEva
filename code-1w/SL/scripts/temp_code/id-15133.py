import math

# Simulated sensor data processing with embedded diagnostics
def collect_readings():
    raw = [127, 255, 83, 191, 64]
    offset = 3
    calibrated = [(x + offset) % 256 for x in raw]
    return calibrated

# Irrelevant helper: checksum for legacy systems (dead path)
def compute_legacy_checksum(data):
    acc = 0
    for val in data:
        acc = (acc + val * 3) % 257
    return acc  # Never used

# Distraction: network simulation (no actual effect)
def simulate_handshake():
    handshake_code = 0xDEAD
    retries = 3
    while retries > 0:
        handshake_code ^= retries
        retries -= 1
    return handshake_code  # Unused result

# Core transformation: frequency extraction via bit manipulation and scaling
def extract_frequency(signal):
    freq = 0
    for sample in signal:
        if sample > 100:
            high_bits = (sample >> 4) & 0x0F
            low_bits = sample & 0x0F
            freq += high_bits ^ low_bits  # XOR variation enhances entropy
    return freq * 1.5

# Secondary analysis: amplitude weighting (partially relevant)
def calculate_weighting(data):
    total = sum(d ** 0.5 for d in data if d % 2 == 1)
    normalized = round(total / len(data), 3)
    return normalized if normalized > 5 else 10.0

# Tertiary red herring: temperature compensation (called but result ignored)
def apply_temp_compensation(value, temp=23):
    factor = 1 + (temp - 20) * 0.015
    adjusted = value * factor
    if adjusted > 100:
        adjusted = 99.9
    return adjusted  # Result not used in final logic

# Data refinement using conditional expression and string-based flag parsing
def refine_data(raw_list, mode_flag="boost"):
    threshold = 90
    # Use string method to determine processing path
    use_enhanced = mode_flag.lower().strip() == "boost"
    
    processed = []
    for item in raw_list:
        # Conditional expression with bitwise twist
        corrected = item if item < threshold else ((item & 0x7F) + 10)
        enhanced = corrected * 2 if use_enhanced and corrected < 120 else corrected
        processed.append(int(enhanced))
    
    # Dead code: shadow copy
    shadow = [p * 0.95 for p in processed]  # Computed but unused
    
    return processed

# Complex diagnostic analyzer combining multiple concepts
def analyze_signal(dataset):
    # Step 1: frequency from transformed data
    base_freq = extract_frequency(dataset)
    
    # Step 2: weighting factor
    weight = calculate_weighting(dataset)
    
    # Step 3: dummy compensation (misleading call)
    dummy_val = apply_temp_compensation(base_freq, temp=25)
    
    # Step 4: boolean logic with short-circuit and comparisons
    is_stable = len(dataset) >= 5 and all(x > 50 for x in dataset) or False
    is_spikey = any(x > 200 for x in dataset)
    
    # Step 5: lambda-based dynamic adjustment
    adjuster = lambda x, w: x * w if x < 300 else x + w
    adjusted_metric = adjuster(base_freq, weight)
    
    # Step 6: control flow with early exit red herring
    if is_spikey:
        return int(adjusted_metric) - 50  # Not taken
    elif not is_stable:
        return -1  # Not taken
    
    # Step 7: final computation with integer division and rounding
    interim = int(adjusted_metric // 1.8)
    
    # Step 8: final XOR-based diagnostic signature
    signature = 0
    for i, val in enumerate(dataset):
        signature ^= (val + i) & 0xFF
    
    # Final result: combination of metric and signature
    final_score = (interim + signature) & 0xFFFF  # Ensure within 16-bit
    
    return final_score

# Orchestration function with decoy calls
def run_diagnostics():
    # Collect and refine data
    raw_data = collect_readings()  # [130, 258 % 256 = 2, 86, 194, 67] -> [130, 2, 86, 194, 67]
    processed_data = refine_data(raw_data, "boost ")
    
    # Irrelevant network handshake
    _ = simulate_handshake()
    
    # Legacy checksum computed but ignored
    _ = compute_legacy_checksum(processed_data)
    
    # Critical statement
    final_diagnostic = analyze_signal(processed_data)
    
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Execute
run_diagnostics()