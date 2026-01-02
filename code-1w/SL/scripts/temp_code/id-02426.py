def process_sensor(x, mode='standard'):
    if mode == 'inverted':
        return (x >> 1) ^ 0xAA
    return (x << 2) | 0x55

# Simulated sensor readings from environmental array
temperature_readings = [23, 18, 31, 44, 27]
humidity_readings = [45, 62, 53, 77, 38]
pressure_readings = [1013, 1009, 1015, 1020, 1005]

# Irrelevant transformation chain (distraction)
encoded_temps = [process_sensor(t, 'inverted') for t in temperature_readings]
scaled_humidity = [(h * 1.2 + 7) // 1 for h in humidity_readings]
pressure_checksum = sum(p & 0xFF for p in pressure_readings)

# Core data processing chain (relevant)
def transform_value(val):
    return val ^ (val << 3) & 0xFFFF

def recursive_reduce(seq, depth=0):
    if depth >= 3 or len(seq) == 1:
        return seq[0]
    reduced = [(seq[i] + seq[i+1]) * (i+1) % 97 for i in range(0, len(seq)-1, 2)]
    return recursive_reduce(reduced, depth + 1)

# Distractor: unused complex function
def decoy_analysis(data):
    magnitude = sum(d ** 2 for d in data) ** 0.5
    phase_shift = [d * magnitude % 17 for d in data]
    return sorted(phase_shift, reverse=True)[::2]

# Real processing path
raw_signals = list(map(lambda x: transform_value(x + 10), temperature_readings))
baseline_offset = sum(raw_signals) % 89

# Complex conditional mutation (mixed logic)
if baseline_offset > 50:
    raw_signals = [r ^ 0x33 for r in raw_signals]
elif baseline_offset < 30:
    raw_signals = [r | 0x1F for r in raw_signals]
else:
    raw_signals = [r + 5 for r in raw_signals]

processing_chain = []
for idx, val in enumerate(raw_signals):
    temp_val = val
    if idx % 2 == 0:
        temp_val = (temp_val & 0x7F) | (idx << 4)
    else:
        temp_val ^= (idx * 13)
    
    # Nested transformation with bit manipulation
    for shift in [1, 2]:
        temp_val ^= (temp_val >> shift)
    
    # Dead code branch (misleading)
    if temp_val < 0:
        temp_val = abs(temp_val)
        temp_val = process_sensor(temp_val, 'inverted')
    
    processing_chain.append(temp_val)

# Secondary distractor: unused accumulator
cumulative_index = 0
for reading in humidity_readings:
    cumulative_index += (reading * 3 + 5) % 11

# Actual answer computation path
def aggregate_metrics(chain, offset):
    total = 0
    for i, c in enumerate(chain):
        contribution = c
        if i % 3 == 0:
            contribution = (contribution * 2) & 0xFFFF
        elif i % 3 == 1:
            contribution = contribution ^ (offset * 7)
        else:
            contribution = (contribution + offset) % 1000
        total += contribution * (i + 1)
    return total ^ 0xAAAA

# Key statement
final_diagnostic = aggregate_metrics(processing_chain, baseline_offset)

# Red herring variables
validation_token = (final_diagnostic ^ 0x5555) % 997
audit_trace = [final_diagnostic % i for i in range(2, 10) if final_diagnostic % i < 5]

# Output result
print(f"Result: {final_diagnostic}")