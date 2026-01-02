def analyze_signal(samples):
    filtered = [x for x in samples if abs(x) > 0.5]
    return [x * 1.05 for x in filtered]

samples = [0.1, 0.8, -0.6, 1.2, -3.0, 0.4, 2.5]
processed = analyze_signal(samples)

def compute_checksum(sequence):
    checksum = 0
    for idx, val in enumerate(sequence):
        checksum += idx * val
    return checksum

# Irrelevant helper (dead function - red herring)
def normalize(vector):
    mag = sum(x**2 for x in vector) ** 0.5
    return [x / mag for x in vector] if mag else vector

# Unused transformation path (distractor)
temp_scaled = [x * 2 for x in processed[:3]]
offset_correction = sum(temp_scaled) - len(temp_scaled)

# Core data structures with mixed relevance
trend_data = []
for i, val in enumerate(processed):
    trend_data.append((i, val ** 2 if val > 0 else -val))

# Decoy mapping (looks important but unused in final result)
status_flags = {i: 'ACTIVE' if v > 1 else 'STANDBY' for i, v in enumerate(processed)}

# Real threshold logic (critical path)
threshold_map = {}
for k in range(len(processed)):
    if k % 2 == 0:
        threshold_map[k] = 1.5 + k * 0.1
    else:
        threshold_map[k] = 0.8

# Simulated metadata (irrelevant container)
metadata_log = []
for i in range(3):
    metadata_log.append({
        'index': i,
        'raw': samples[i],
        'processed': processed[i] if i < len(processed) else None,
        'flag': status_flags.get(i, 'UNKNOWN')
    })

# Auxiliary counting (misleading intermediate)
event_count = 0
for val in processed:
    if val > 1.0:
        event_count += 1

# Bit manipulation decoy (complex but unused)
bit_encoded = 0
for i in range(len(processed)):
    if i % 3 == 0:
        bit_encoded |= (1 << i)

# Real aggregation function
def aggregate_metrics(data, thresholds):
    total = 0.0
    for index, value in data:
        thresh = thresholds.get(index, 1.0)
        if value > thresh:
            total += value * 0.9
        elif value < -thresh:
            total -= value * 0.3
    return int(total)  # Final deterministic integer

# Key statement
final_diagnostic = aggregate_metrics(trend_data, threshold_map)

# Output requirement
print(f"Result: {final_diagnostic}")