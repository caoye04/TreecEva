import itertools

# Simulated sensor data processing with red herrings and distractions
def preprocess(stream):
    filtered = [x for x in stream if x > 30]
    adjusted = [x * 1.05 for x in filtered]
    return adjusted

# Irrelevant transformation - dead end
def transform_noise(data):
    return [d ** 0.5 for d in data if d % 2 == 0]

# Unused recursive function - distraction
def recursive_sum(arr, n):
    if n <= 0:
        return 0
    return arr[n-1] + recursive_sum(arr, n-1)

# Decoy checksum that looks important but isn't used
def bad_checksum(seq):
    acc = 0
    for i, val in enumerate(seq):
        acc += val * (i + 1)
    return acc % 97

# Real processing functions
def segment(signal):
    chunks = []
    for i in range(0, len(signal), 4):
        chunk = signal[i:i+4]
        if len(chunk) == 4:
            chunks.append(chunk)
    return chunks

def analyze_chunk(chunk):
    base = sum(chunk) / len(chunk)
    deviation = sum(abs(x - base) for x in chunk)
    return base, deviation

def finalize(data_segments):
    values = []
    for seg in data_segments:
        mean_val, dev = analyze_chunk(seg)
        if dev < 15:
            values.append(int(mean_val))
    # Key computation happens here
    result = 0
    for i, v in enumerate(values):
        result ^= (v + i) * 11
    return result

# Simulated raw input - appears noisy and complex
raw_input = [25, 32, 38, 45, 29, 33, 36, 41, 50, 28, 30, 34, 37, 44, 55, 60, 27, 31, 35, 39]

# Multiple processing paths - only one leads to answer
processed_signal = preprocess(raw_input)
decoy_output = transform_noise(processed_signal)

# Real path begins here
segments = segment(processed_signal)

# Red herring: unused analysis
for s in segments:
    _ = analyze_chunk(s)  # intermediate result ignored

# Critical execution point
checksum = finalize(segments)

# Print final target result
print(f"Target result: {checksum}")