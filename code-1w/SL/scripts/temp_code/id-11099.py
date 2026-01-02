import itertools

# Simulate industrial thermal system with mixed operational loads
def calculate_base_resistance(temperature):
    return (temperature * 0.37) + 2.1

def deprecated_voltage_compensation(voltage, threshold=120):
    # Dead code path - never called
    if voltage > threshold:
        return voltage * 0.9
    return voltage

def filter_anomalous_readings(readings):
    # Irrelevant filtering function - distractor
    return [r for r in readings if 10 <= r <= 100]

def integrate_stability_coefficients(data, window=3):
    # Unused smoothing logic - red herring
    result = []
    for i in range(len(data)):
        start = max(0, i - window)
        avg = sum(data[start:i+1]) / (i - start + 1)
        result.append(round(avg, 2))
    return result

def compute_harmonic_load_profile(phases):
    # Misleading energy computation - not used in final result
    harmonics = []
    for p in phases:
        harmonic = 0
        for i in range(1, 6):
            harmonic += (p / i) * ((-1) ** i)
        harmonics.append(round(harmonic, 3))
    return harmonics

def detect_peaks(signal, threshold=0.75):
    # Decoy function - simulates signal analysis
    return [i for i, s in enumerate(signal) if s > threshold * max(signal)]

def accumulate_momentary_surges(transients, tolerance=5):
    # Intermediate distraction calculation
    surge_total = 0
    for t in transients:
        if t % 2 == 0:
            surge_total += t // tolerance
        else:
            surge_total += t % tolerance
    return surge_total * 0.1  # Diverting but irrelevant

def analyze_thermal_response(load_sequence, efficiency_ratio):
    base_temp = 25
    resistance = calculate_base_resistance(base_temp)
    
    # Core relevant logic begins
    adjusted_loads = [int(l * efficiency_ratio) for l in load_sequence]
    
    # Redundant transformation - looks important but partially unused
    normalized = [min(max(x, 0), 100) for x in adjusted_loads]
    
    # Key processing: find dominant frequency in load pattern
    frequency_map = {}
    for val in normalized:
        freq = len([x for x in normalized if x == val])
        frequency_map[val] = freq
    
    # Determine modal load intensity
    modal_intensity = max(frequency_map, key=frequency_map.get)
    
    # Apply decay factor based on repetition count
    repetition_decay = frequency_map[modal_intensity]
    decayed_intensity = modal_intensity / (1 + repetition_decay * 0.05)
    
    # Compute phase-weighted shift using itertools cycle simulation
    cyclic_phases = list(itertools.islice(itertools.cycle([0.8, 1.1, 0.9]), len(load_sequence)))
    weighted_shift = sum(decayed_intensity * phase for phase in cyclic_phases[:len(load_sequence)])
    
    # Final capacity determination - depends only on specific derived values
    base_capacity = 500
    thermal_factor = 2.3
    adjustment_bands = [10, 25, 50]
    
    # Conditional adjustment (only one branch matters)
    if decayed_intensity > 30:
        band_index = 2
    elif decayed_intensity > 15:
        band_index = 1
    else:
        band_index = 0
    
    dynamic_offset = adjustment_bands[band_index]
    
    # Actual answer computation
    thermal_capacity = int(base_capacity + (weighted_shift * thermal_factor) - dynamic_offset)
    
    return thermal_capacity

# Irrelevant global variables - distractions
system_voltages = [110, 115, 122, 118, 125]
efficiency_logs = {'t1': 0.88, 't2': 0.91, 't3': 0.87}
baseline_metrics = {'stability': 0.94, 'jitter': 1.2, 'drift': 0.05}

# Input data - transient_loads and efficiency_factor are actually used
transient_loads = [42, 63, 42, 81, 42, 55, 63]
efficiency_factor = 1.15

# Secondary irrelevant computation
harmonic_profile = compute_harmonic_load_profile([1.0, 1.5, 1.2])
anomaly_filtered = filter_anomalous_readings([5, 15, 105, 50, 200])
surge_accumulation = accumulate_momentary_surges(transient_loads)

# Main execution point
thermal_capacity = analyze_thermal_response(transient_loads, efficiency_factor)

# Print result as required
print(f"Result: {thermal_capacity}")