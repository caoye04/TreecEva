import math

# Simulated sensor data processing with diagnostic analysis
def collect_telemetry():
    raw_readings = [i * 0.7 + (i % 3) for i in range(15)]
    timestamps = list(range(1000, 1150, 10))
    return list(zip(timestamps, raw_readings))

# Irrelevant helper: formats timestamp (not used in final result)
def format_time(t):
    hours = t // 3600
    mins = (t % 3600) // 60
    secs = t % 60
    return f'{hours:02}:{mins:02}:{secs:02}'

# Distraction function: processes unrelated metadata
def extract_metadata():
    meta = {'version': '2.1', 'node_id': 8872, 'mode': 'diagnostic'}
    normalized_id = (meta['node_id'] * 17) % 999  # dead end
    return {k: v for k, v in meta.items() if k != 'mode'}

# Signal conditioning with red herrings
def preprocess_signal(data):
    filtered = []
    noise_floor = 0.3
    amplification = 2.5
    
    for t, val in data:
        adjusted = abs(val) * amplification
        if adjusted > noise_floor:
            # Apply arbitrary phase shift (distractor)
            phase_shifted = adjusted + math.sin(t / 100.0)
            filtered.append(phase_shifted * 0.95)
    
    # Decoy transformation
    inverted = [1.0 / (x + 1e-5) for x in filtered]
    sorted_inverted = sorted(inverted, reverse=True)
    mid_point = len(sorted_inverted) // 2
    
    # This looks important but isn't used later
    decoy_aggregate = sum(sorted_inverted[:mid_point]) / (mid_point + 1)
    
    return filtered

# Frame segmentation with tuple unpacking distraction
def segment_frames(signal):
    frames = []
    size = 4
    for i in range(0, len(signal) - size + 1, 2):
        frame = signal[i:i+size]
        parity_check = sum(1 for x in frame if x % 2 > 0.5)  # misleading metric
        checksum = sum(frame) * (i + 1)  # looks useful, not used
        frames.append((frame, checksum))  # store with unused checksum
    return frames

# Core analysis logic buried in distractions
def compute_coherence(packet):
    values, _ = packet  # unpack tuple, ignore checksum
    n = len(values)
    if n == 0:
        return 0.0
    squared_sum = sum(x ** 2 for x in values)
    mean_square = squared_sum / n
    root_mean_square = math.sqrt(mean_square)
    return round(root_mean_square, 4)

# Higher-order function red herring
def make_processor(factor):
    return lambda x: x * factor  # never actually used

# Actual key processing chain
processed_data = collect_telemetry()
signal = preprocess_signal(processed_data)
packets = segment_frames(signal)

# Distractor: complex-looking but unused pipeline
processor_chain = [
    lambda x: x + 0.1,
    lambda x: max(x, 0.5),
    lambda x: x if x < 10 else x * 0.9
]

temp_results = []
for p in packets:
    val = compute_coherence(p)
    # Apply decoy transformations
    for op in processor_chain:
        val = op(val)
    temp_results.append(val)

# Real computation hidden among noise
coherence_values = [compute_coherence(p) for p in packets]
suppressed = [c for c in coherence_values if c > 1.0]  # filter relevant subset
amplified = [s * 3.7 for s in suppressed]

# Critical statement embedded in multiple layers
baseline = sum(amplified) / len(amplified) if amplified else 0
offset = math.log(len(packets) + 1, 2)
dynamic_weight = (baseline * offset) ** 1.1

# Final aggregation using enumerate and zip (required features)
indexed = list(enumerate(amplified))
shifted = [w * (i + 1) for i, w in indexed]
combined = sum(w for w in shifted)
mod_factor = len(shifted) if shifted else 1
normalized_total = combined / mod_factor

# Secondary path with dead logic
if len(amplified) > 5:
    alt_path = [a ** 0.5 for a in amplified]
    fallback = sum(alt_path) * 0.3  # never reached
else:
    fallback = None

# Key intermediate that looks like final answer but isn't
tentative_diagnostic = normalized_total * 0.86

# Another decoy: recursive sum (unused)
def recursive_sum(arr, idx=0):
    if idx >= len(arr):
        return 0
    return arr[idx] + recursive_sum(arr, idx + 1)

decoys = [recursive_sum(list(range(i, i+3))) for i in range(3)]  # irrelevant

# Final computation buried after distractions
final_diagnostic = int(round(tentative_diagnostic + dynamic_weight * 0.37, 0))

print(f"Result: {final_diagnostic}")