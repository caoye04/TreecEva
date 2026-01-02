import math

# Irrelevant helper function (decoy)
def dummy_transform(x):
    return (x ** 2 + 3 * x + 1) % 100

# Unused transformation chain
def legacy_filter(values):
    return [v for v in values if v % 7 != 0]

# Distractor: complex-looking but unused computation
def spectral_score(seq):
    score = 0
    for i, val in enumerate(seq):
        score += val * math.sin(i * math.pi / 4)
    return round(score, 3)

# Real processing components
def validate_chunk(chunk):
    return sum(chunk) > 50 and len(chunk) <= 7

def normalize(val):
    return val / 10.0 if val > 0 else 0.1

# Core logic disguised among red herrings
transform_step = lambda x: x * 2 + 1

# Simulate sensor data with noise masking
raw_readings = [12, 8, 15, 23, 4, 18, 9, 27]
noise_pattern = [(-1)**i * (i % 3) for i in range(len(raw_readings))]
adjusted_readings = [r + n for r, n in zip(raw_readings, noise_pattern)]

# Dead code path - looks important but unused
data_matrix = [[x + i for x in adjusted_readings] for i in range(3)]
redundant_aggregate = sum(sum(row) for row in data_matrix)

# Actual signal extraction
signal_peaks = [x for x in adjusted_readings if x > 15]

# Misleading intermediate
fake_trend = list(map(lambda x: x ** 0.5, signal_peaks))

# Real pipeline begins here
data_stream = [8, 6, 14, 22, 3, 17, 8, 26]

# Corrupted copy (distractor)
corrupted_copy = data_stream.copy()
for i in range(len(corrupted_copy)):
    if i % 3 == 0:
        corrupted_copy[i] = -999

# Conditional processing with early returns
def analyze_segment(segment):
    if not segment:
        return 0
    if len(segment) < 3:
        return -1
    if sum(segment) < 40:
        return 0
    
    # Valid path
    base = segment[0] * 2
    offset = sum(1 for s in segment if s % 2 == 0)
    return base + offset

# Complex transformation pipeline
processed_parts = []
for i in range(0, len(data_stream), 3):
    chunk = data_stream[i:i+3]
    if validate_chunk(chunk):
        processed = sum(transform_step(c) for c in chunk)
        processed_parts.append(processed)
    else:
        temp = sum(chunk) // 2
        processed_parts.append(temp)  # fallback

# Secondary adjustment layer
temp_output = 0
for val in processed_parts:
    if val > 30:
        temp_output += int(normalize(val) * 10)
    elif val == 25:
        temp_output += 5
    else:
        temp_output += 1

# Final aggregation with conditional expression
intermediate = temp_output * 3 if len(processed_parts) > 2 else temp_output * 2

# Red herring: fake checksum
checksum = 0
for i, v in enumerate(data_stream):
    checksum += v * (i + 1)
checksum = (checksum % 89) + 10  # Looks critical, unused

# Another decoy variable
theoretical_limit = math.floor(math.log(len(data_stream) * max(data_stream), 2))

# Real final step
final_output = 0
def process_pipeline(stream):
    global final_output
    segments = [stream[i:i+4] for i in range(0, len(stream), 4)]
    results = []
    
    for seg in segments:
        analysis = analyze_segment(seg)
        if analysis <= 0:
            continue
        results.append(analysis)
        
        # Early break based on condition
        if sum(results) > 50:
            break
    
    # Key calculation
    if results:
        avg_result = sum(results) / len(results)
        final_output = int(avg_result * 2.5)  # Critical assignment
    else:
        final_output = -1
        
    return final_output

# Execute main logic
final_output = process_pipeline(data_stream)

# Print result as required
print(f"Target result: {final_output}")