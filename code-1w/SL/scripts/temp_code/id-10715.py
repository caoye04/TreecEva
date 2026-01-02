import math

# Simulated sensor frame data (irrelevant in part)
sensor_logs = [
    [1.2, 0.8, 3.4, 2.1],
    [0.9, 1.1, 2.8, 5.6],
    [2.3, 1.7, 0.6, 4.4],
    [1.1, 0.9, 1.3, 1.5]
]

# Irrelevant calibration constants
calibration_factor = 0.987
offset_table = {i: math.sin(i * 0.1) for i in range(10)}
dummy_counter = 0

# Signal processing parameters (some are red herrings)
noise_threshold = 1.5
smoothing_window = 3
sample_rate = 100  # unused

# Decoy function - looks important but never called
def deprecated_filter(data):
    return [x for x in data if x > 0.5]

# Auxiliary transformation - actually used indirectly
def normalize_frame(frame):
    global dummy_counter
    norm = sum(x**2 for x in frame) ** 0.5
    return [round(x / norm, 6) for x in frame]

# Misleading intermediate computation (dead end)
baseline_energy = 0
for frame in sensor_logs:
    energy = sum(abs(x) for x in frame)
    if energy > noise_threshold:
        baseline_energy += energy * 0.1  # distractor accumulation

# Real processing begins: extract frames above threshold
significant_frames = []
for i, frame in enumerate(sensor_logs):
    magnitude = sum(abs(x) for x in frame)
    if magnitude > noise_threshold:
        significant_frames.append((i, magnitude))

# Processed frames: store normalized vectors with index
processed_frames = []
for idx, mag in significant_frames:
    raw = sensor_logs[idx]
    normalized = normalize_frame(raw)
    processed_frames.append(normalized)

# Another decoy: complex-looking but unused structure
feature_map = {
    'peaks': [],
    'entropy': {},
    'spectral': lambda x: sum(math.cos(val) for val in x)
}

# Key transformation using list comprehension and zip
aligned = [
    [vec[i] for vec in processed_frames]
    for i in range(len(processed_frames[0]))
]

# Apply window smoothing via list comprehension (partially irrelevant)
smoothed_signal = [
    sum(window) / len(window)
    for window in aligned
    if len(window) >= smoothing_window // 2
]

# Critical function: analyzes phase coherence across dimensions
def compute_coherence(frames):
    if not frames:
        return 0.0
    
    # Use enumerate and zip idiomatically
    transposed = list(zip(*frames))
    coherence_score = 0.0
    for dim_idx, channel in enumerate(transposed):
        variation = max(channel) - min(channel)
        avg = sum(channel) / len(channel)
        # Introduce lambda for dynamic weighting
        weight_func = lambda x: math.exp(-abs(x - avg))
        weights = [weight_func(val) for val in channel]
        coherence_score += variation * (sum(weights) / len(weights))
    return round(coherence_score, 6)

# Secondary analysis: temporal stability (distractor metric)
stability_log = []
for frame in processed_frames:
    diff_vector = [
        abs(frame[i] - frame[i-1])
        for i in range(1, len(frame))
    ]
    if diff_vector:
        stability_log.append(sum(diff_vector) / len(diff_vector))

# Unused recursive red herring
def trace_path(matrix, row=0, col=0, path=[]):
    if row == len(matrix) - 1 and col == len(matrix[0]) - 1:
        return path + [matrix[row][col]]
    if row >= len(matrix) or col >= len(matrix[0]):
        return []
    return trace_path(matrix, row+1, col, path + [matrix[row][col]]) or \
           trace_path(matrix, row, col+1, path + [matrix[row][col]])

# Real diagnostic logic
coherence = compute_coherence(processed_frames)

# Destructuring assignment - relevant
primary, secondary = processed_frames[0][0], processed_frames[0][1]

# Bit manipulation decoy (no effect on result)
flag_register = 0b1010
flag_register ^= 0b1111
flag_register |= 0b0101
parity_check = bin(flag_register).count('1') % 2

# Final analysis function
def analyze_signal(frames):
    # Complex conditional branch with early returns
    if len(frames) < 2:
        return -1
    
    total_amplitude = 0.0
    for frame in frames:
        amp = 0.0
        for val in frame:
            amp += abs(val)
        total_amplitude += amp
    
    # Use of enumerate in meaningful way
    adjustment = 0.0
    for i, frame in enumerate(frames):
        if i % 2 == 0:
            adjustment += math.log(1 + sum(frame))
    
    # Final formula combining multiple factors
    n_frames = len(frames)
    n_dims = len(frames[0])
    base_score = total_amplitude * (adjustment + 1)
    penalty = (n_frames * 0.1) ** (n_dims * 0.25)
    
    # The actual answer emerges here
    return int(round(base_score / penalty))

# Execution point of interest
final_diagnostic = analyze_signal(processed_frames)

# Print required output
print(f"Result: {final_diagnostic}")