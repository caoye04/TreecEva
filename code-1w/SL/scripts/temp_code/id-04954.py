import math

# Simulated aerospace telemetry processing with decoy diagnostics

def analyze_vibration(freq, amplitude):
    # Irrelevant vibration analysis (dead-end function)
    if freq > 500:
        return amplitude * math.sin(freq / 100)
    else:
        return amplitude * math.cos(freq / 50)


def compute_efficiency(thrust, fuel_rate):
    # Misleading efficiency metric (not used in final result)
    base = thrust / max(fuel_rate, 0.1)
    penalty = 0.95 if thrust < 800 else 1.0
    return base * penalty

# Red herring sensor calibration table
calibration_map = {
    'temp': lambda x: x * 1.02 + 3.1,
    'pressure': lambda x: x * 0.98 - 2.5,
    'vibration_x': lambda x: abs(x) ** 0.5,
    'vibration_y': lambda x: abs(x) ** 0.7,
    'flow_rate': lambda x: round(x, 2)
}

# Unused historical thresholds (distractor data)
historical_limits = [
    {'phase': 'ascent', 'max_temp': 850, 'max_pressure': 200},
    {'phase': 'cruise', 'max_temp': 700, 'max_pressure': 150},
    {'phase': 'descent', 'max_temp': 600, 'max_pressure': 100}
]

# Core diagnostic processor
engine_data = [
    {'sensor_id': 'ENG-01A', 'reading': 437, 'mode': 'primary'},
    {'sensor_id': 'ENG-02B', 'reading': 291, 'mode': 'backup'},
    {'sensor_id': 'ENG-03C', 'reading': 582, 'mode': 'primary'},
    {'sensor_id': 'ENG-04D', 'reading': 356, 'mode': 'backup'}
]

# Decoy transformation chain
transform_chain = [
    lambda x: x << 1,
    lambda x: x ^ 255,
    lambda x: x + 100,
    lambda x: x % 97
]

# Apply meaningless transforms to create distraction
obfuscated = []
for entry in engine_data:
    val = entry['reading']
    for func in transform_chain:
        val = func(val)  # This transformed value is never used
    obfuscated.append(val)

# Real processing begins here — heavily masked by prior noise
working_set = []
for record in engine_data:
    raw = record['reading']
    # Only primary mode sensors contribute to final diagnostic
    if record['mode'] == 'primary':
        # Apply modular arithmetic and bit manipulation
        processed = (raw * 3) % 887
        processed = processed ^ 137  # XOR mask
        working_set.append(processed)

# Secondary filter: only values above median affect final result
median_val = sorted(working_set)[len(working_set) // 2]
filtered = [x for x in working_set if x > median_val]

# Final aggregation uses dictionary-based frequency counting (relevant)
frequency_count = {}
for val in filtered:
    freq_key = val % 50
    frequency_count[freq_key] = frequency_count.get(freq_key, 0) + 1

# Critical calculation: sum of weighted frequencies
weight_fn = lambda k, v: (k * v) if (k + v) % 3 == 0 else 0
weighted_sum = sum(weight_fn(k, v) for k, v in frequency_count.items())

# Secondary term using trigonometric smoothing on original primaries
primary_readings = [r['reading'] for r in engine_data if r['mode'] == 'primary']
amplitude_mod = sum(math.cos(math.pi * r / 180) for r in primary_readings)
smoothed_amp = int(amplitude_mod * 100)

# Final diagnostic combines both components
final_diagnostic = weighted_sum + smoothed_amp

# Irrelevant print statements (simulating debug output)
print(f"Vibration analysis: {analyze_vibration(620, 45)}")
print(f"Efficiency score: {compute_efficiency(880, 3.2)}")
print(f"Obfuscated values: {obfuscated}")
print(f"Calibration status: {calibration_map['temp'](100)}")

# ONLY this line matters for the answer
print(f"Target result: {final_diagnostic}")