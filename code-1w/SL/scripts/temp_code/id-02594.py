import math

# Simulated sensor data from a distributed environmental monitoring system
temperature_readings = [23.4, 24.1, 22.8, 25.6, 26.7, 24.3, 23.9, 25.1]
humidity_readings = [45, 48, 50, 55, 60, 53, 49, 51]
pressure_readings = [1013, 1015, 1012, 1010, 1008, 1011, 1014, 1016]

# Irrelevant auxiliary arrays (distractors)
aux_timestamps = [1623456789 + i*300 for i in range(8)]
dummy_flags = [bool(i % 3) for i in range(8)]
fake_checksums = [sum(humidity_readings[:i+1]) * 0.7 for i in range(8)]

# Data normalization function (partially relevant)
def normalize(data):
    mean_val = sum(data) / len(data)
    return [(x - mean_val) / mean_val * 100 for x in data]

# Heavily obfuscated transformation chain with red herrings
def transform_stream(stream, mode='standard'):
    if mode == 'standard':
        # Real processing: apply logarithmic scaling
        processed = [math.log(x + 1) for x in stream]
        # Distractor: unused conditional path
        if len(stream) > 10:
            return [x * 1.5 for x in processed]
        return processed
    elif mode == 'debug':
        # Dead code path — never reached
        return [x * 2 for x in stream]
    else:
        return stream

# Misleading diagnostic routine with decoy outputs
def generate_diagnostics(data_set):
    peak = max(data_set)
    variance = sum((x - sum(data_set)/len(data_set))**2 for x in data_set) / len(data_set)
    entropy = -sum((x/sum(data_set)) * math.log(x/sum(data_set)) for x in data_set if x > 0)
    # Decoy values that look important but aren't used later
    saturation_level = (peak / 30.0) * 100 if peak > 20 else 0
    stability_index = 1 / (variance + 1)
    return {'entropy': entropy, 'variance': variance, 'peak': peak}

# Core data processing pipeline
normalized_temp = normalize(temperature_readings)
transformed_humidity = transform_stream(humidity_readings)

# Complex list comprehension combining multiple sources (key operation)
processing_chain = [
    normalized_temp[i] * 0.6 + \
    transformed_humidity[i] * 0.3 + \
    math.sin(pressure_readings[i] % 10) * 0.1
    for i in range(len(temperature_readings))
]

# Unused alternative computation path (dead logic)
if len(aux_timestamps) != len(processing_chain):
    alt_chain = [x * 1.2 for x in processing_chain]
    correction_factor = 0.95
else:
    correction_factor = 1.0  # Neutral factor, distractor

# Another irrelevant transformation
shifted_pressure = [p - 1000 for p in pressure_readings]
scaled_shifted = [p * 0.01 for p in shifted_pressure]

# Generate side diagnostics (only one field matters later)
diagnostics = generate_diagnostics(temperature_readings)

# Decoy aggregation functions
def fake_aggregate_v1(seq, meta):
    return sum(seq) * meta.get('variance', 1.0)

def fake_aggregate_v2(seq, meta):
    return sum(x**2 for x in seq) / (meta.get('peak', 1) + 1)

# Actual critical function — determines final answer
def aggregate_metrics(chain, meta):
    base_score = sum(chain)
    penalty = meta['variance'] * 0.5
    # The real formula
    result = (base_score - penalty) * 100
    # Distractor: unused conditional mutation
    if result > 100:
        result += 10  # Never reached due to actual values
    return result

# Execute key statement
final_diagnostic = aggregate_metrics(processing_chain, diagnostics)

# Print result as required
print(f"Target result: {final_diagnostic}")