import math

# Simulated quantum sensor array diagnostics with red herrings
def preprocess_readings(raw_data):
    processed = []
    noise_floor = 0.003
    scaling_factor = 1.76
    for x in raw_data:
        if x > noise_floor:
            processed.append(math.log(x) * scaling_factor)
    return processed

# Legacy function - not used but looks relevant
def deprecated_analysis(seq):
    return sum([x ** 0.5 for x in seq if x % 2 == 0])

# Core system state analyzer
def analyze_system_state(buffer, mask):
    temp_result = 0
    critical_threshold = 184.3
    secondary_limit = 92.1
    adjustment = 0.0

    # Irrelevant normalization path (dead logic due to fixed condition)
    normalize = False
    if sum(buffer) % 7 == 0 and False:  # Always skipped
        adjustment = sum(buffer) / len(buffer)
        normalize = True

    # Bit manipulation decoy
    masked_ints = [mask & int(abs(x)) % 256 for x in buffer]
    xor_fingerprint = 0
    for val in masked_ints:
        xor_fingerprint ^= val

    # Real computation begins here
    filtered = [x for x in buffer if x > critical_threshold]
    
    # Secondary filter based on modulo pattern
    refined = []
    for val in filtered:
        if (int(val) % 11 == 0) or (int(val * 0.73) % 4 == 0):
            refined.append(val)

    # Tertiary constraint using lambda-based filtering
    energy_lambda = lambda e: math.sin(e / 100) > 0.4
    high_energy_nodes = list(filter(energy_lambda, refined))

    # Compute base diagnostic score
    base_score = 0
    for node in high_energy_nodes:
        base_score += int(node / 10)

    # Apply conditional multiplier based on tuple unpacking result
    flags = (len(high_energy_nodes) > 2, xor_fingerprint < 150, base_score % 5 == 0)
    flag_a, flag_b, flag_c = flags

    multiplier = 1
    if flag_a and not flag_c:
        multiplier = 3
    elif flag_b:
        multiplier = 2
    else:
        multiplier = 1

    # Final adjustment using min/max balance
    if len(high_energy_nodes) > 0:
        peak = max(high_energy_nodes)
        trough = min(high_energy_nodes)
        stability_index = (peak - trough) / peak
        if stability_index < 0.45:
            adjustment = 17.8
        else:
            adjustment = -9.4
    else:
        adjustment = -25.1

    # Actual final computation (key path)
    temp_result = base_score * multiplier + int(adjustment)

    # Distractor: complex unused calculation
    spectral_sum = 0
    for i in range(len(buffer)):
        spectral_sum += buffer[i] * math.cos(i * math.pi / 4)
    # This is never used

    # Final diagnostic output
    final_diagnostic = int(temp_result + 107)  # Offset added deterministically
    return final_diagnostic


# Initialization data
base_readings = [12.7, 45.2, 91.8, 185.3, 203.6, 177.1, 198.4, 211.9, 88.3]
quantum_buffer = [x * 1.37 for x in base_readings]
fault_mask = 219  # Hex: 0xDB

# Unused but plausible-looking preprocessing
processed_sensors = preprocess_readings(base_readings)
spectral_metrics = [abs(math.tanh(x/100)) for x in quantum_buffer]

# Key execution point
final_diagnostic = analyze_system_state(quantum_buffer, fault_mask)
print(f"Result: {final_diagnostic}")