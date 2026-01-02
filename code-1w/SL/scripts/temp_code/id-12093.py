import itertools

# Simulated sensor readings from deep-space array (irrelevant raw data)
raw_readings = [0.12, 0.34, 0.25, 0.67, 0.89, 0.55, 0.44, 0.73]

# Irrelevant preprocessing: noise floor correction (dead path)
def apply_noise_floor(data, floor=0.1):
    return [max(x - floor, 0) for x in data]

def generate_combinations(values):
    # Distractor: generates all 2-combinations but unused
    return list(itertools.combinations(values, 2))

def integrate_background_flux(sequence):
    # Misleading function: looks relevant but not used in final calculation
    running_total = 0.0
    for i, val in enumerate(sequence):
        running_total += val * (i + 1) / 100
    return running_total

# Real signal processing chain
def extract_peak_signals(readings, threshold=0.4):
    return [x for x in readings if x > threshold]

def normalize_signals(peaks, norm_factor):
    return [p / norm_factor for p in peaks]

def compute_quantum_efficiency(normed_signals):
    # Quantum efficiency model based on normalized inputs
    efficiency = 0.0
    for s in normed_signals:
        efficiency += s ** 2 * 0.75
    return efficiency

def calculate_stellar_flux(dataset, calib):
    # Core logic begins here — actual answer depends on this path
    filtered = [x for x in dataset if x > 0.5]  # Only values above 0.5 matter
    adjusted = [f * 1.5 for f in filtered]     # Boost each valid reading
    
    # Apply cumulative decay factor across sequence
    decayed = []
    for idx, val in enumerate(adjusted):
        decay_factor = 0.9 ** idx
        decayed.append(val * decay_factor)
    
    # Aggregate total energy proxy
    total_energy = sum(decayed)
    
    # Secondary transformation: harmonic dampening
    dampened_components = []
    for e in decayed:
        if e > 1.0:
            dampened_components.append(1.0)
        else:
            dampened_components.append(e)
    
    dampened_sum = sum(dampened_components)
    
    # Final non-linear calibration mapping
    flux = (dampened_sum * calib) ** 1.1
    
    # Introduce red herring intermediate
    pseudo_entropy = len(decayed) * 0.33
    info_density = flux / (pseudo_entropy + 1) if pseudo_entropy > 0 else flux
    
    # Final result computed here
    return int(flux * 1000) / 1000  # Round to 3 decimal places

# Unused legacy function (decoy)
def legacy_flux_calc(arr):
    return sum(x**1.5 for x in arr)

# Spurious data structure (distractor)
system_logs = {
    'timestamp': '2024-05-17',
    'status': 'nominal',
    'readings_processed': 8,
    'anomaly_count': 0
}

# Actual observed scientific data (relevant input)
observed_data = [0.15, 0.22, 0.58, 0.61, 0.77, 0.43, 0.81, 0.92, 0.34, 0.68]

# Calibration constant from satellite instrument specs
calibration_factor = 2.3

# Dead code path using itertools (misdirection)
combinations_of_noise = generate_combinations(raw_readings[:4])

# Background integration on irrelevant data
baseline_drift = integrate_background_flux(raw_readings)

# Signal extraction on real data
strong_signals = extract_peak_signals(observed_data, threshold=0.55)

# Normalization using calibration factor
normalized_peaks = normalize_signals(strong_signals, calibration_factor)

# Efficiency computation (looks important, but not used in final answer)
quantum_efficiency = compute_quantum_efficiency(normalized_peaks)

# Critical execution point
final_flux = calculate_stellar_flux(observed_data, calibration_factor)

# Print result as required
print(f"Result: {final_flux}")