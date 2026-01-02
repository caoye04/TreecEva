def analyze_signal(samples, threshold=0.75):
    normalized = [round(x / max(samples), 3) for x in samples]
    outliers = [i for i, v in enumerate(normalized) if v > threshold]
    compression_map = {i: (v * 100) for i, v in enumerate(normalized)}
    return outliers, compression_map


def generate_checksum(sequence):
    checksum = 0
    for i, val in enumerate(sequence):
        if i % 2 == 0:
            checksum += val * 3
        else:
            checksum += val
    return checksum % 101


def transform_coordinates(coords):
    # Irrelevant transformation chain
    transformed = []
    for x, y in coords:
        angle = (x + y) % 360
        radius = (x**2 + y**2) ** 0.5
        transformed.append((round(radius * angle, 2), abs(x - y)))
    return transformed

# Simulated sensor readings
sensor_readings = [120, 150, 98, 200, 176, 160, 143]

# Step 1: Analyze signal for anomalies
anomalies, mapping = analyze_signal(sensor_readings)

# Distractor: Coordinate system unrelated to main logic
dummy_coords = [(2, 3), (5, 7), (11, 13)]
spatial_data = transform_coordinates(dummy_coords)

# Step 2: Build processing chain with decoy operations
buffer_pool = []
for idx in range(8):
    temp_entry = {}
    temp_entry['id'] = idx
    temp_entry['active'] = idx in anomalies
    temp_entry['weight'] = idx * 1.5 if idx in anomalies else idx * 0.8
    temp_entry['flagged'] = str(idx) in [hex(a)[2:] for a in anomalies]  # Red herring
    buffer_pool.append(temp_entry)

# Misleading diagnostic trail
false_indicators = []
for entry in buffer_pool:
    if 'weight' in entry and entry['weight'] > 5.0:
        false_indicators.append(entry['id'] * 2)  # Decoy accumulation

# Real data path begins here
sequence_a = [len(anomalies), sum(anomalies), generate_checksum(anomalies)]
sequence_b = [sensor_readings[i] for i in anomalies if i < len(sensor_readings)]
combined_signals = zip(sequence_a, sequence_b)

# Processing chain construction
processing_chain = []
for i, (a, b) in enumerate(combined_signals):
    record = {
        'index': i,
        'value': (a + b) // (i + 1),
        'meta': pow(a, b, 17) if b > 0 else 0  # Modular exponentiation
    }
    processing_chain.append(record)

# Auxiliary dictionary operations (mix of relevant and irrelevant)
data_tags = {f"tag_{i}": f"level_{v['value'] % 4}" for i, v in enumerate(processing_chain)}
enriched = {d['index']: d['value'] for d in processing_chain}

# Diagnostic computation with string manipulation red herring
temp_diagnostics = []
for k, v in enriched.items():
    tag_val = int(data_tags[f"tag_{k}"][-1])
    # String-based distraction
    bin_rep = ''.join(bin(v).split('b'))
    padded = bin_rep.zfill(8)
    flipped = padded[::-1]
    interpreted = int(flipped, 2)
    # Only this part actually contributes
    temp_diagnostics.append(v + tag_val - len(padded))

# Final aggregation function
def aggregate_metrics(chain, diagnostics):
    base_score = sum(d['value'] for d in chain)
    bonus = len([d for d in chain if d['meta'] > 5])
    penalty = 0
    
    # Nested conditional decoy
    for d in chain:
        if d['index'] > 10:
            penalty += d['value']  # Never executes
        elif d['value'] < 0:
            penalty += abs(d['value'])
    
    # Critical distractor: fake complex adjustment
    adjustment_factor = 0.0
    history_log = ""
    for i in range(len(diagnostics)):
        history_log += f"{diagnostics[i]:.0f}"
    if '999' in history_log:
        adjustment_factor = -5.5
    
    # Actual result computation
    raw_total = base_score + bonus - penalty
    final_shift = sum(int(b) for b in bin(raw_total)[:8])  # First 8 bits only
    return raw_total + final_shift

# Execute critical statement
final_diagnostic = aggregate_metrics(processing_chain, temp_diagnostics)
print(f"Result: {final_diagnostic}")