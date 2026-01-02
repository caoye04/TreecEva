def analyze_signal_strength(signal, threshold=50):
    if signal > threshold:
        return 'strong'
    return 'weak'


def evaluate_compatibility(a, b):
    return (a + b) % 7 == 0


def transform_value(x):
    temp = x * 2 + 1
    temp = temp ^ 5
    temp = (temp >> 1) + (temp << 2)
    return temp & 0xFF

# Irrelevant helper function (dead code path)
def deprecated_util(val):
    return val ** 2 % 19

# Unused constant (distractor)
MAX_BUFFER_SIZE = 8192

# Simulated sensor readings (mixed data)
sensor_data = [12, 18, 22, 35, 47, 50, 63]
calibration_offset = 3
adjusted_readings = []

for raw in sensor_data:
    adjusted = raw + calibration_offset
    adjusted_readings.append(adjusted)

# Misleading intermediate calculation (not used in final result)
total_adjustment = sum([x - calibration_offset for x in adjusted_readings])

# Composite transformation chain
transformed_chain = []
for val in adjusted_readings:
    transformed = transform_value(val)
    if transformed % 3 == 0:
        transformed = int(transformed * 1.5)
    transformed_chain.append(transformed)

# Conditional expression with tuple unpacking
status_flags = [
    ('OK', 'ERROR')[transformed < 100] if val > 40 else 'UNKNOWN'
    for val, transformed in zip(sensor_data, transformed_chain)
]

# Distractor: unused dictionary with plausible-looking metrics
health_metrics = {
    'stability': len([x for x in transformed_chain if x > 50]),
    'variance': sum(transformed_chain) / len(transformed_chain) - min(transformed_chain),
    'peak_load': max(transformed_chain) // 2,
    'deprecated_mode': deprecated_util(len(sensor_data))
}

# Core logic disguised among distractions
primary_signals = [x for x, s in zip(transformed_chain, sensor_data) if s >= 47]

# Bit manipulation and logical filtering
evaluated_pairs = []
for i in range(len(primary_signals)):
    for j in range(i+1, len(primary_signals)):
        if evaluate_compatibility(primary_signals[i], primary_signals[j]):
            evaluated_pairs.append((primary_signals[i], primary_signals[j]))

# Case conversion on status flags (plausible but irrelevant)
status_text = ''.join(status_flags).lower()

# Final processing with conditional expression
consensus = 'valid' if len(evaluated_pairs) >= 2 else 'invalid'

# Key computation: combines arithmetic, bit ops, and filtered data
aggregate = 0
for p in evaluated_pairs:
    aggregate += (p[0] ^ p[1]) + (p[0] & p[1])

scaling_factor = 1.75 if consensus == 'valid' else 0.25

# Critical execution point
final_diagnostic = int(aggregate * scaling_factor + len(status_text))

print(f"Result: {final_diagnostic}")