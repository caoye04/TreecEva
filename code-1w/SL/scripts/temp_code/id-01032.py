def analyze_signal(samples, threshold=0.75):
    normalized = [x / max(samples) for x in samples]
    outliers = [i for i, x in enumerate(normalized) if x > threshold]
    return set(outliers)


def generate_sequence(n):
    seq = [1, 1]
    for i in range(2, n):
        seq.append(seq[i-1] + seq[i-2])
    return seq

# Irrelevant helper function (dead code path)
def deprecated_filter(data):
    return [x for x in data if x % 3 == 0]

# Unused transformation chain
temp_weights = [0.1, 0.3, 0.4, 0.2]
weighted_sum = sum(w * i for i, w in enumerate(temp_weights))

# Simulated sensor inputs (distractor data)
sensor_a = [120, 135, 140, 90, 180, 200, 160]
sensor_b = [88, 95, 105, 110, 108, 99, 92]

# Real input data
primary_stream = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# Step 1: Extract positions above median
median_val = sorted(primary_stream)[len(primary_stream)//2]
high_freq_indices = {i for i, x in enumerate(primary_stream) if x > median_val}

# Step 2: Map to frequency codes using lambda
freq_encoder = lambda idx, val: (idx * val) % 17
encoded_signals = [freq_encoder(i, v) for i, v in enumerate(primary_stream)]

# Step 3: Filter valid channels
valid_channels = set()
for i, code in enumerate(encoded_signals):
    if code % 3 == 0 and i % 2 == 1:
        valid_channels.add(i)

# Step 4: Build processing chain using zip and enumerate
auxiliary_data = generate_sequence(len(primary_stream))
processing_chain = []
for idx, (sig, fib) in enumerate(zip(primary_stream, auxiliary_data)):
    if sig % 2 == 0:
        processing_chain.append(fib * 2)
    elif idx in high_freq_indices:
        processing_chain.append(fib // 2)
    else:
        processing_chain.append(fib + sig)

# Step 5: Compute diagnostic scores (irrelevant accumulation)
diagnostic_scores = []
total_offset = 0
for i in range(len(primary_stream)):
    if i < len(sensor_a) and sensor_a[i] > 100:
        total_offset += 1  # Red herring counter
    if i in analyze_signal(sensor_a):  # Use of irrelevant function
        diagnostic_scores.append(0.5)
    else:
        diagnostic_scores.append(0.1)

# Step 6: Actual metric computation
diagnostics = []
for i, val in enumerate(processing_chain):
    contribution = val
    if i in valid_channels:
        contribution *= 1.5
    if i < len(primary_stream) and primary_stream[i] == max(primary_stream):
        contribution += 10
    diagnostics.append(contribution)

# Step 7: Aggregate final metric (key statement)
aggregate_metrics = lambda chain, diag: int(sum(diag) - len(chain) * 0.5)
final_diagnostic = aggregate_metrics(processing_chain, diagnostics)

# Misleading intermediate print (not part of logic)
placeholder_result = sum(x for x in sensor_b if x > 100) * 0.01

# Correct output
print(f"Result: {final_diagnostic}")