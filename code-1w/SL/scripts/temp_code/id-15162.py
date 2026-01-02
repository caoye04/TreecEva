import itertools

# Simulated sensor data processing with red herrings and distractions
def analyze_signal_strength(raw_samples):
    adjusted = [x * 1.05 for x in raw_samples]
    offset = sum(adjusted) / len(adjusted)
    centered = [x - offset for x in adjusted]
    return [abs(x) for x in centered]

# Irrelevant function - decoy for signal analysis (dead code path)
def deprecated_analysis(data):
    return [d ** 0.5 for d in data if d > 0]

# Critical data transformation chain
def filter_anomalies(seq, limit):
    window_size = 3
    smoothed = []
    for i in range(len(seq)):
        start = max(0, i - window_size // 2)
        end = min(len(seq), i + window_size // 2 + 1)
        avg = sum(seq[start:end]) / (end - start)
        if abs(seq[i] - avg) < limit:
            smoothed.append(seq[i])
        else:
            smoothed.append(avg)  # Replace outliers
    return smoothed

# Core logic with distractors
raw_input = [12, -8, 15, 23, -18, 42, 16, -9, 11]
scaling_factor = 2.5

# Distractor: unused scaled version
scaled_data = [z * scaling_factor for z in raw_input]

# Step 1: Analyze signal (relevant)
processed_signal = analyze_signal_strength(raw_input)

# Distractor: fake normalization
fake_norm = [val / max(processed_signal) for val in processed_signal]
useless_ratio = sum(fake_norm) / len(fake_norm)

# Step 2: Apply filtering to remove noise
noise_threshold = 5.0
filtered_data = filter_anomalies(processed_signal, noise_threshold)

# Distractor: spurious statistical calculation
median_guess = sorted(filtered_data)[len(filtered_data)//2]
mode_approx = max(set([round(x) for x in filtered_data]), key=filtered_data.count)

# Conditional expression (required Python feature): adjust threshold based on data spread
dynamic_adjust = True if max(filtered_data) - min(filtered_data) > 10 else False
threshold = noise_threshold * 0.8 if dynamic_adjust else noise_threshold * 1.2

# Step 3: Process signals using iteration patterns (itertools used here)
def process_signals(data, t):
    grouped = [list(group) for k, group in itertools.groupby(data, key=lambda x: x >= t)]
    result_chain = []
    for segment in grouped:
        if len(segment) >= 2:
            # Complex transformation: cumulative effect
            accum = 0
            for val in segment:
                accum = accum * 0.9 + val
            result_chain.append(round(accum, 3))
        else:
            result_chain.append(segment[0] * 0.5)
    return sum(result_chain) - len(result_chain)

# Misleading recursive function (never called)
def recursive_denoise(arr, depth=0):
    if depth > 2 or len(arr) < 2:
        return arr
    mid = len(arr) // 2
    left = recursive_denoise(arr[:mid], depth+1)
    right = recursive_denoise(arr[mid:], depth+1)
    return left + [sum(left+right)/len(left+right)] + right

# Final computation
final_output = process_signals(filtered_data, threshold)

# Print required output
print(f"Result: {final_output}")