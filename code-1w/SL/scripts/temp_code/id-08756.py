import itertools

# Simulated sensor array diagnostics with signal processing
sensor_ids = [101, 102, 103, 104]
base_frequencies = [440, 880, 220, 660]
calibration_offsets = [0.12, -0.08, 0.34, -0.21]

# Irrelevant auxiliary data (distractor)
diagnostic_log = {}
for sid in sensor_ids:
    diagnostic_log[f'sensor_{sid}'] = {'status': 'OK', 'retries': 0}

# Signal pattern generator with complex mapping (core logic begins)
def generate_pattern(frequency, phase_shift, duration=10):
    pattern = []
    for t in range(duration):
        val = int(frequency * (t + phase_shift)) % 127
        if val < 0:
            val += 127
        pattern.append(val)
    return pattern[:10]

# Misleading signal analysis (dead path)
def legacy_evaluate(signal):
    magnitude = sum([x ** 2 for x in signal]) ** 0.5
    normalized = [x / (magnitude + 1e-9) for x in signal]
    return sum(normalized[::2]) - sum(normalized[1::2])

# Real-time filter simulation (distractor)
current_filters = {k: {'active': True, 'gain': 1.0} for k in ['low', 'mid', 'high']}
for band in current_filters:
    current_filters[band]['cutoff'] = 1000 if band == 'high' else 500 if band == 'mid' else 100

# Threshold map generation with modular arithmetic and shifts (relevant)
def build_threshold_map(base_freqs, offsets):
    thresholds = {}
    for i, freq in enumerate(base_freqs):
        # Complex transformation chain
        scaled = (freq * 1.5) // 10
        adjusted = int(scaled + offsets[i] * 100)
        level = (adjusted ^ i) & 127  # Bitwise mix
        thresholds[f'sensor_{sensor_ids[i]}'] = level
    return thresholds

# Pattern buffer construction using itertools (required feature)
def construct_buffer(frequencies, phases):
    all_patterns = []
    phase_cycle = itertools.cycle(phases)
    for freq in frequencies:
        phase = next(phase_cycle)
        raw_pattern = generate_pattern(freq, phase)
        # Apply dummy smoothing (irrelevant modification)
        smoothed = [raw_pattern[0]]
        for j in range(1, len(raw_pattern)):
            smoothed.append(int((smoothed[-1] + raw_pattern[j]) / 2))
        all_patterns.append(smoothed)
    
    # Interleave patterns using itertools (core)
    interleaved = list(itertools.chain.from_iterable(
        zip(*all_patterns)
    ))
    return interleaved

# Main analyzer (critical function)
def analyze_signal(buffer, thresholds):
    # Compute rolling checksum
    checksum = 0
    for i, val in enumerate(buffer):
        if i % 3 == 0:
            checksum += val * (i // 3 + 1)
        elif i % 7 == 0:
            checksum -= val
    
    # Determine activation count above thresholds (complex logic)
    sensor_101_thresh = thresholds['sensor_101']
    sensor_102_thresh = thresholds['sensor_102']
    sensor_103_thresh = thresholds['sensor_103']
    sensor_104_thresh = thresholds['sensor_104']
    
    counts = {
        'over_101': 0,
        'over_102': 0,
        'over_103': 0,
        'over_104': 0
    }
    
    # Assign sub-patterns (uses slicing logic)
    chunk_size = len(buffer) // 4
    chunks = [
        buffer[0:chunk_size],
        buffer[chunk_size:2*chunk_size],
        buffer[2*chunk_size:3*chunk_size],
        buffer[3*chunk_size:4*chunk_size]
    ]
    
    for val in chunks[0]:
        if val > sensor_101_thresh:
            counts['over_101'] += 1
    for val in chunks[1]:
        if val > sensor_102_thresh:
            counts['over_102'] += 1
    for val in chunks[2]:
        if val > sensor_103_thresh:
            counts['over_103'] += 1
    for val in chunks[3]:
        if val > sensor_104_thresh:
            counts['over_104'] += 1
    
    # Composite diagnostic score
    weighted_sum = (
        counts['over_101'] * 1.1 +
        counts['over_102'] * 0.9 +
        counts['over_103'] * 1.3 +
        counts['over_104'] * 0.7
    )
    
    # Final nonlinear transformation
    if weighted_sum > 20:
        diagnostic_score = int(weighted_sum * 1.25)
    elif weighted_sum > 10:
        diagnostic_score = int(weighted_sum * 1.1)
    else:
        diagnostic_score = int(weighted_sum * 0.9)
    
    # Secondary adjustment based on checksum parity
    if checksum % 2 == 0:
        final_adjustment = diagnostic_score + (checksum % 17)
    else:
        final_adjustment = diagnostic_score - (checksum % 13)
    
    return final_adjustment

# Unused diagnostic routine (red herring)
def comprehensive_scan(data):
    entropy = 0.0
    freq_dist = {}
    for x in data:
        freq_dist[x] = freq_dist.get(x, 0) + 1
    total = len(data)
    for count in freq_dist.values():
        p = count / total
        entropy -= p * (p).log() if p > 0 else 0
    return entropy

# Setup execution context
phase_sequence = [0.5, 1.5, 2.5, 3.5]
threshold_map = build_threshold_map(base_frequencies, calibration_offsets)
pattern_buffer = construct_buffer(base_frequencies, phase_sequence)

# Execute main analysis
final_diagnostic = analyze_signal(pattern_buffer, threshold_map)

# Print result as required
print(f"Target result: {final_diagnostic}")