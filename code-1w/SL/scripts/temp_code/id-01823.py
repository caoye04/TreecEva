import itertools

# Simulated sensor data processing pipeline for environmental monitoring
raw_readings = [14, 7, 22, 5, 19, 13, 8, 3]
offset_threshold = 10
calibration_factor = 3

# Irrelevant transformation: historical average smoothing (unused)
historical_avg = sum(raw_readings) / len(raw_readings)
smoothed = [round((x + historical_avg) / 2) for x in raw_readings]

# Relevant data path begins: apply nonlinear calibration
def calibrate(x):
    return (x ** 2) // calibration_factor

calibrated = list(map(calibrate, raw_readings))

# Misleading secondary path: frequency analysis (dead end)
frequencies = {x: calibrated.count(x) for x in set(calibrated)}
mode_value = max(frequencies, key=frequencies.get) if frequencies else 0

# Data segmentation based on threshold (red herring with partial use)
segments = {}
for i, val in enumerate(calibrated):
    label = 'high' if val > offset_threshold else 'low'
    if label not in segments:
        segments[label] = []
    segments[label].append((i, val))

# Distractor: complex tuple unpacking and unused combinatorics
index_vals = [(i, v) for i, v in enumerate(calibrated)]
all_pairs = list(itertools.combinations(index_vals, 2))
long_pair_chain = sum(1 for a, b in all_pairs if (b[1] - a[1]) % 3 == 0)  # unused

# Real computation begins: transform via sliding window
transformed_data = []
for i in range(len(calibrated) - 2):
    window = calibrated[i:i+3]
    # Apply weighted sum: center-weighted filter
    transformed_value = window[0] * 0.25 + window[1] * 0.5 + window[2] * 0.25
    transformed_data.append(int(transformed_value))

# Dead branch: hypothetical projection (never executed)
if False:
    projected = [x * 2 for x in transformed_data]
    extrapolated_sum = sum(projected)

# Real logic: pattern analyzer using overlapping triplets
pattern_registry = []
def analyze_patterns(data):
    if len(data) < 3:
        return sum(data) * 2
    
    total_score = 0
    for triplet in itertools.zip_longest(data, data[1:], data[2:], fillvalue=0):
        a, b, c = triplet
        # Complex conditional scoring
        if a < b > c:  # Peak detection
            contribution = b - ((a + c) // 2)
        elif a > b < c:  # Valley detection
            contribution = abs(b - ((a + c) // 2)) * 2
        else:
            contribution = (a + b + c) % 7
        total_score += contribution
    
    # Secondary modulation: depends on length parity
    modifier = len(data) % 4
    return int(total_score * (1 + modifier / 10))

# Key assignment statement
final_diagnostic = analyze_patterns(transformed_data)

# Unused diagnostic branches (distractors)
baseline_metric = sum(calibrated) // len(calibrated)
shadow_copy = transformed_data.copy()
shadow_copy.reverse()

# Output result as required
print(f"Result: {final_diagnostic}")