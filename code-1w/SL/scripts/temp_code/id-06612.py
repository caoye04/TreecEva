import math

# Simulated sensor data from multiple sources
temperature_readings = [23.4, 25.1, 22.8, 24.6, 26.0, 23.9, 24.1]
humidity_readings = [56, 61, 59, 55, 62, 58, 60]
pressure_readings = [1013, 1015, 1012, 1014, 1016, 1011, 1013]

# Irrelevant baseline calibration (distractor)
baseline_offset = sum([0.1 * i for i in range(7)]) / 7
adjusted_temps = [t + 0.5 for t in temperature_readings]
scaled_humidity = [h * 1.01 for h in humidity_readings]

# Decoy processing function (dead path)
def analyze_pattern(data):
    return sum(d ** 2 for d in data if d > len(data))

# Unused transformation chain (red herring)
transform_chain = list(map(lambda x: x * 1.8 + 32, temperature_readings))  # Fahrenheit conversion (unused)

# Bit manipulation simulation for signal integrity check (partially relevant)
def checksum_signal(values):
    total = 0
    for v in values:
        scaled = int(v * 10)
        total ^= scaled  # XOR accumulation
    return total & 0xFF  # Keep within byte range

# Diagnostic flags from subsystems (mixed relevance)
signal_checksum = checksum_signal(pressure_readings)
diagnostic_flags = {
    'temp_stable': all(abs(temperature_readings[i] - temperature_readings[i+1]) < 1.5 
                     for i in range(len(temperature_readings)-1)),
    'humidity_spike': any(h > 60 for h in humidity_readings),
    'pressure_anomaly': abs(min(pressure_readings) - max(pressure_readings)) > 5,
    'checksum_valid': signal_checksum % 2 == 1
}

# Irrelevant combinatorics on indices (distractor)
index_pairs = [(i, j) for i in range(5) for j in range(i+1, 6)]
pair_count_metric = sum(1 for p in index_pairs if (p[0] + p[1]) % 3 == 0)

# Core processing chain with slicing and conditional logic
window_size = 3
rolling_averages = [
    sum(temperature_readings[i:i+window_size]) / window_size
    for i in range(len(temperature_readings) - window_size + 1)
]

# Identify transitions using slicing and comparison
cooling_phase = [
    rolling_averages[i] > rolling_averages[i+1] 
    for i in range(len(rolling_averages)-1)
]
heating_phase = [
    rolling_averages[i] < rolling_averages[i+1]
    for i in range(len(rolling_averages)-1)
]

# Early termination condition (simulated fault detection)
fault_detected = False
for i, temp in enumerate(temperature_readings):
    if temp > 25.0 and humidity_readings[i] > 59:
        fault_detected = True
        break

if fault_detected:
    # Secondary validation
    valid_fault = diagnostic_flags['humidity_spike'] and not diagnostic_flags['temp_stable']
    if valid_fault:
        base_score = 850
    else:
        base_score = 420
else:
    base_score = 100

# Complex data transformation pipeline (relevant core)
processing_chain = [
    {'raw': t, 'idx': i, 'weight': 0.9 + (i * 0.01)} 
    for i, t in enumerate(adjusted_temps)
]

# Weighted contribution calculation with lambda and slicing
weight_func = lambda item: item['raw'] * item['weight']
weighted_sum = sum(weight_func(item) for item in processing_chain[:5])
penalty = sum(1 for hp in heating_phase if hp) * 12.5

# Diagnostics aggregation from multiple sources (mix of relevant/irrelevant)
diagnostics = [
    base_score,
    signal_checksum * 3.1,
    len(cooling_phase) * 100,
    pair_count_metric * -5,  # Distractor influence
    math.log(signal_checksum + 1) * 10
]

# Final integration with conditional override
final_diagnostic = aggregate_metrics(processing_chain, diagnostics) if not fault_detected else base_score - int(penalty)

# Simulated metrics aggregator (core logic)
def aggregate_metrics(chain, diagnostics):
    primary = sum(item['raw'] * item['weight'] for item in chain) / len(chain)
    secondary = sum(d for d in diagnostics if d > 0) / len(diagnostics)
    adjustment = math.sin(math.pi * len(cooling_phase) / 10)
    return (primary * 10) + secondary + (adjustment * 100)

# Reset final_diagnostic after definition to simulate reprocessing
if 'final_diagnostic' in locals():
    final_diagnostic = aggregate_metrics(processing_chain, diagnostics)

# Output result
Target result: {final_diagnostic}