import math

# Simulated astronomical observation data
observed_data = [127, 83, 156, 201, 94, 133, 178, 65]
calibration_map = {'gain': 0.87, 'offset': 3.2, 'threshold': 75}

# Irrelevant auxiliary variables (distractors)
dark_current_noise = [12, 9, 15, 8, 11, 10, 13, 7]
bias_frame = [2.1, 2.3, 2.0, 2.4, 2.2, 2.1, 2.3, 2.0]
temporal_weights = [0.9, 1.1, 0.95, 1.05, 0.98, 1.02, 0.99, 1.01]

# Unused function - red herring
def apply_fourier_filter(signal):
    """Unused transform - misleading path"""
    return [math.sin(x / 10) for x in signal]

# Decoy processing chain
processed_noise = []
for i, val in enumerate(dark_current_noise):
    adjusted = val * bias_frame[i] + temporal_weights[i]
    processed_noise.append(round(adjusted, 2))

# Dummy correlation matrix (dead code path)
correlation_matrix = []
for i in range(len(observed_data)):
    row = []
    for j in range(len(observed_data)):
        if i == j:
            row.append(1.0)
        else:
            row.append(round(math.cos((i - j) * 0.4), 3))
    correlation_matrix.append(row)

# Real processing begins here — deeply nested and interwoven with distractors
def extract_valid_signals(data, config):
    filtered = []
    for idx, reading in enumerate(data):
        # Apply calibration only if above threshold
        if reading > config['threshold']:
            calibrated = (reading - config['offset']) * config['gain']
            if calibrated > 0:
                # Additional check: must correspond to odd indices in original stream
                if idx % 2 == 1:
                    # Introduce minor bit manipulation as obfuscation
                    shifted = int(calibrated) >> 1
                    inverted = 255 ^ shifted  # bitwise complement within byte
                    back_shifted = inverted << 1
                    # Only use transformed value if passes parity check
                    if bin(back_shifted).count('1') % 2 == 0:
                        filtered.append(back_shifted % 100)
                    else:
                        filtered.append(int(calibrated))
                else:
                    filtered.append(int(calibrated))
    return filtered

# Secondary transformation involving zip and enumerate
# This part looks important but only used conditionally
auxiliary_scaling = [1.03, 0.98, 1.01, 0.99]


def combine_with_reference(primary_list, scale_factors):
    result = []
    # Misleading use of zip and enumerate — not actually altering final output
    for i, (val, factor) in enumerate(zip(primary_list, scale_factors * 2)):
        temp_val = val * factor
        # Simulate checksum that isn't actually used
        checksum = sum([int(c) for c in str(int(temp_val))])
        if checksum > 5:
            result.append(temp_val + i)
        else:
            result.append(temp_val - i)
    return result

# Core calculation function
# Uses combinatorics implicitly via index selection

def calculate_stellar_flux(observations, calib):
    # Step 1: Extract valid signals using complex criteria
    candidates = extract_valid_signals(observations, calib)
    
    # Step 2: Compute combinatorial pairing count (real logic)
    n = len(candidates)
    if n < 2:
        pair_count = 0
    else:
        pair_count = (n * (n - 1)) // 2  # C(n,2)
    
    # Step 3: Aggregate magnitude (this is where real answer comes from)
    total_magnitude = 0
    for i, mag in enumerate(candidates):
        contribution = mag * math.log(mag + 10)  # stabilizing log
        if i % 3 == 0:
            contribution *= 0.9
        elif i % 3 == 1:
            contribution *= 1.05
        total_magnitude += contribution
    
    # Final flux depends on both pair_count and total_magnitude
    flux_base = total_magnitude * (1 + pair_count / 100)
    
    # Red herring: attempt to normalize with unused structures
    try:
        from math import gamma
        correction = gamma(len(correlation_matrix)) if len(correlation_matrix) > 0 else 1
        flux_base /= correction  # This does nothing significant
    except:
        pass
    
    # Actual final computation
    final_value = int(flux_base * 100) / 100.0  # Round to two decimals
    
    return final_value

# Execution point of interest
final_flux = calculate_stellar_flux(observed_data, calibration_map)

# Print result for evaluation
print(f"Target result: {final_flux}")