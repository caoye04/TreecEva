from collections import defaultdict
import math

# Simulate sensor data segmentation and weighted analysis
raw_signals = [0.8, 1.2, -0.5, 3.1, 2.9, -1.3, 0.0, 1.7, 2.4]
threshold = 1.0
window_size = 3

# Segment signal based on threshold crossings
def segment_signal(data, thresh):
    segments = []
    current = []
    above = False
    
    for x in data:
        if x > thresh:
            if not above:
                if current:
                    segments.append(current)
                current = []
            current.append(x)
            above = True
        else:
            if above:
                segments.append(current)
                current = []
            above = False
    
    if current and len(current) > 0:
        segments.append(current)
    
    return segments

# Misleading auxiliary function (not used in final path)
def analyze_peaks(signal_list):
    peak_count = 0
    for s in signal_list:
        if s > 2.0:
            peak_count += 1
    return peak_count  # Dead-end computation

# Helper to compute centroid of a segment
def segment_centroid(seg):
    if len(seg) == 0:
        return 0.0
    weighted_sum = sum(i * val for i, val in enumerate(seg))
    return weighted_sum / len(seg) if len(seg) > 0 else 0.0

# Lambda for dynamic weight scaling (used later)
scale_fn = lambda w, factor: [x * factor for x in w]

# Generate segment-specific metadata
segment_data = segment_signal(raw_signals, threshold)

# Irrelevant tracking variables
idle_periods = 0
max_gap = -1.0
status_log = defaultdict(int)

# Compute segment durations (dummy metric)
durations = [len(seg) for seg in segment_data]

# Assign artificial identifiers
segment_ids = [f"seg_{i+1}" for i in range(len(segment_data))]

# Distractor: complex but unused transformation chain
transformed = list(map(lambda x: math.log(abs(x) + 1), raw_signals))
filtered = [x for x in transformed if x > 0.5]
squared_norm = sum(x**2 for x in filtered) / len(filtered) if filtered else 0

# Real processing begins here
weights = [0.8, 1.2, 0.9, 1.5]  # One weight per expected segment
if len(weights) > len(segment_data):
    weights = weights[:len(segment_data)]
elif len(weights) < len(segment_data):
    diff = len(segment_data) - len(weights)
    weights.extend([1.0] * diff)

# Scale weights conditionally (actually used)
scaling_factor = len(segment_data) / 2.0 if len(segment_data) > 1 else 1.0
weights = scale_fn(weights, scaling_factor)

# Process each segment with centroid and apply weight
weighted_centroids = []
for i, seg in enumerate(segment_data):
    centroid = segment_centroid(seg)
    # XOR-based activation check (bitwise twist)
    activation_flag = len(seg) ^ i  # Semi-relevant distraction
    if activation_flag >= 0:  # Always true
        weighted_centroids.append(centroid * weights[i])

# Final aggregation
intermediate_total = sum(weighted_centroids)
penalty = abs(len(raw_signals) - len(segment_data) * 2)  # Minor adjustment

# Key assignment
final_score = round(intermediate_total - penalty, 4)

# Output result as required
print(f"Result: {final_score}")