import math

# Simulated sensor fusion system for environmental monitoring

def collect_samples():
    raw_signals = [127, 85, 196, 43, 210, 72, 158, 103]
    noise_floor = 42
    adjusted = [s ^ 0x55 for s in raw_signals]  # Bit-flip correction
    return adjusted

# Irrelevant audio processing decoy function
def process_audio_stream(data):
    fft_bins = [abs(math.sin(d / 10.0)) for d in data]
    peak_freq = max(fft_bins)
    normalized = [f / peak_freq for f in fft_bins if f > 0.1]
    return sum(normalized)  # Dead-end computation

# Data transformation pipeline with red herrings
def transform_coordinates(x, y, z):
    lat_offset = x * 0.001
    lon_scale = y * 0.002
    alt_factor = z * 0.1
    # Complex but unused geospatial transform
    transformed = {
        'north': lat_offset + math.cos(lon_scale),
        'east': lon_scale + math.sin(lat_offset),
        'elevation': alt_factor ** 2
    }
    return transformed  # Computation has no effect on main logic

# Core data processor (used)
def filter_anomalies(readings):
    filtered = []
    for val in readings:
        if val < 20 or val > 200:
            continue
        if val % 7 == 0:  # Arbitrary exclusion rule
            continue
        filtered.append(val)
    return filtered

# Higher-order function distractor
def create_multiplier(factor):
    return lambda x: x * factor  # Never actually used

scale_func = create_multiplier(3.14159)

# Set-based mode analysis with real and fake usage
def detect_modes(data):
    unique_vals = set(data)
    duplicates = set([x for x in data if data.count(x) > 1])
    modes = unique_vals - duplicates  # Actual logic not meaningful
    sorted_modes = sorted(list(modes))
    return sorted_modes[:3]  # Returns some values but not used downstream

def compute_entropy(data):
    total = sum(data)
    probs = [ (d / total) for d in data ]
    entropy = -sum(p * math.log2(p) for p in probs if p > 0)
    return entropy  # Computed but ignored later

# Real signal path begins here
raw_data = collect_samples()

# Decoy: audio-like processing on non-audio data
audio_proxy = process_audio_stream(raw_data)

# Transform irrelevant coordinates
transform_coordinates(15, 30, 45)

# Filter to valid diagnostic range
processed_data = filter_anomalies(raw_data)

# Fake entropy calculation (misleading intermediate)
diag_entropy = compute_entropy(processed_data)

# Generate various threshold sets (only one is used)
thresh_a = {5, 15, 25, 35, 45}
thresh_b = {10, 30, 50, 70}
thresh_c = {x for x in range(5, 100, 10) if x % 15 != 0}
thresh_d = {8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96}

# Critical threshold set selected via indirection
def get_active_threshold():
    choices = [thresh_a, thresh_b, thresh_c, thresh_d]
    indices = [len(s) for s in choices]
    total_elements = sum(indices)
    selected_index = (total_elements % 4)  # Evaluates to 1 → thresh_b
    return choices[selected_index]

threshold_set = get_active_threshold()  # Actually returns thresh_b

# Primary analysis engine
def analyze_readings(readings, thresholds):
    count_above = 0
    sum_within = 0
    for r in readings:
        if r > 55:
            count_above += 1
        if r in thresholds:
            sum_within += r
    aggregate = count_above * 1000 + sum_within
    
    # Complex-looking but irrelevant secondary check
    reading_set = set(readings)
    overlap = reading_set & thresholds
    if len(overlap) > 2:
        adjustment = sum([math.sqrt(x) for x in overlap])
    else:
        adjustment = len(reading_set) // 2
    
    final_score = aggregate - adjustment  # Key result computed here
    return int(final_score)

# Dead code path: combinatorics decoy
def calculate_combinations(n, r):
    if r > n:
        return 0
    num = math.factorial(n)
    den = math.factorial(r) * math.factorial(n - r)
    return num // den

combination_check = calculate_combinations(10, 3)

# Trigger the actual target computation
final_diagnostic = analyze_readings(processed_data, threshold_set)

# Print required result
print(f"Target result: {final_diagnostic}")