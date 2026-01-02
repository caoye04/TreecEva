import math

# Simulated sensor array data from environmental monitoring system
temperature_readings = [23.5, 24.1, 22.9, 25.3, 26.0, 24.8, 23.7]
humidity_readings = [45, 47, 50, 44, 49, 52, 46]
pressure_readings = [1013, 1011, 1015, 1009, 1018, 1012, 1014]

# Irrelevant preprocessing: unused transformation chain
def transform_sequence(data, func=lambda x: x):
    return [func(x) for x in data if x > 0]

scaled_temps = transform_sequence(temperature_readings, lambda x: x * 1.02)
offset_humidity = transform_sequence(humidity_readings, lambda x: x + 3)

# Decoy analysis function (never called)
def compute_thermal_index(temp, hum):
    index = 0
    for t, h in zip(temp, hum):
        index += t * (h / 100) ** 0.5
    return round(index, 2)

# Unused statistical red herring
correlation_proxy = sum(t * h for t, h in zip(temperature_readings, humidity_readings)) / len(temperature_readings)

# Signal processing pipeline with embedded logic
baseline_offset = 0.87
smoothing_factor = 0.91

# Simulate raw signal filtering (partially relevant)
filtered_signals = []
for i in range(len(temperature_readings)):
    filtered_value = (
        temperature_readings[i] * 0.6 +
        humidity_readings[i] * 0.03 +
        (pressure_readings[i] - 1000) * 0.01
    )
    filtered_signals.append(filtered_value)

# Generate time-series weights (distractor with partial relevance)
time_weights = [math.exp(-smoothing_factor * i) for i in range(7)]
weighted_sum = sum(w * s for w, s in zip(time_weights, filtered_signals))
normalization = sum(time_weights)
adjusted_baseline = weighted_sum / normalization - baseline_offset

# Create diagnostic flags (mixed relevance)
exceedance_flags = [1 if t > 24.5 else 0 for t in temperature_readings]
critical_periods = sum(exceedance_flags)

# Dummy state tracker (dead code path)
current_state = 'STANDBY'
state_log = []
for flag in exceedance_flags:
    if flag and current_state == 'STANDBY':
        current_state = 'ACTIVE'
    state_log.append(current_state)

# Data window segmentation (irrelevant)
window_size = 3
segmented_data = [
    filtered_signals[i:i+window_size] 
    for i in range(0, len(filtered_signals), window_size)
]

# Primary processing chain - core logic buried in noise
processing_chain = []
for i, sig in enumerate(filtered_signals):
    # Non-linear transformation with conditional modulation
    if humidity_readings[i] > 48:
        processed = sig * math.log(pressure_readings[i] - 1000 + 1)
    else:
        processed = sig * math.sqrt(temperature_readings[i])
    
    # Bit manipulation as obscure normalization (actually used)
    int_component = int(abs(processed) * 100) & 0xFFFF  # Keep lower 16 bits
    fractional_contribution = int_component % 89  # Prime modulus for dispersion
    processing_chain.append(fractional_contribution)

# Diagnostic accumulator with red herrings
intermediate_diagnostics = {
    'peak_deviation': max(processing_chain) - min(processing_chain),
    'phase_shift': sum(1 for a, b in zip(processing_chain, processing_chain[1:]) if b < a),
    'harmonic_mean_proxy': len(processing_chain) / sum(1/v if v != 0 else 0.01 for v in processing_chain),
    'unused_entropy': -sum((v/100) * math.log(v/100) for v in processing_chain if v > 0)
}

# Actual critical computation hidden among decoys
diagnostic_score = 0
for i, val in enumerate(processing_chain):
    if i % 2 == 0:
        diagnostic_score += val * (i + 1)
    else:
        diagnostic_score -= val // (i + 1)

# Final aggregation with misleading structure
def aggregate_metrics(chain, diagnostics):
    base = sum(chain) // len(chain)
    modifier = 0
    
    # Irrelevant conditionals
    if diagnostics['peak_deviation'] > 50:
        modifier += 10
    if diagnostics['phase_shift'] > 3:
        modifier -= 5
    
    # ACTUAL determining factor (non-obvious)
    for i, c in enumerate(chain):
        if c > base and i in [1, 3, 5]:
            modifier += 2
    
    return base + modifier

# Critical execution point
final_diagnostic = aggregate_metrics(processing_chain, intermediate_diagnostics)

# Output requirement
print(f"Target result: {final_diagnostic}")