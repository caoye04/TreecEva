from collections import defaultdict

# Simulate sensor data processing with noise filtering and threshold analysis
def preprocess_data(raw_values):
    filtered = []
    noise_floor = 0.5
    for val in raw_values:
        if abs(val) > noise_floor:
            filtered.append(abs(val))
    return sorted(filtered, reverse=True)

# Detect significant peaks above dynamic threshold
def detect_peaks(values, base_threshold):
    peaks = []
    dyn_threshold = base_threshold
    for i, v in enumerate(values):
        if v > dyn_threshold:
            peaks.append((i, v))
            dyn_threshold *= 1.1  # Raise threshold after each detection
    return peaks

# Calculate composite score based on peak distribution and decay factors
def calculate_final_score(data, thresholds):
    # Irrelevant intermediate calculation (distractor)
    temp_buffer = [x * 0.95 for x in data if x % 2 == 1]
    temp_sum = sum(temp_buffer) / (len(temp_buffer) + 1)
    
    # Relevant preprocessing
    processed = preprocess_data(data)
    primary_peaks = detect_peaks(processed, thresholds[0])
    secondary_peaks = detect_peaks(processed, thresholds[1])
    
    # State tracking with defaultdict (python idiom)
    peak_stats = defaultdict(int)
    for idx, val in primary_peaks:
        peak_stats['count'] += 1
        peak_stats['total'] += val

    # Secondary logic with slicing and bitwise check (mixed paradigms)
    recent_primary = primary_peaks[:3]  # Top 3 only
    bonus = 0
    if len(recent_primary) >= 2:
        # XOR-based consistency check on indices
        index_pattern = recent_primary[0][0] ^ recent_primary[1][0]
        if index_pattern & 1:  # Odd pattern gets bonus
            bonus = 7

    # Composite scoring with weighted contributions
    main_score = 0
    if peak_stats['count'] > 0:
        main_score = peak_stats['total'] / peak_stats['count']
        
    # Use of slicing to derive correction factor
    correction = 1.0
    if len(processed) > 4:
        tail_values = processed[-4:]
        correction = (sum(tail_values) / len(tail_values)) * 0.1

    # Final computation chain
    stability_factor = len(primary_peaks) - len(secondary_peaks)
    raw_final = main_score * 10 + bonus + (stability_factor * 3)
    final_score = int(raw_final - (raw_final * correction))  # Apply dampening
    
    # Dead code path (distractor)
    if temp_sum < 0:
        final_score *= 2  # Never reached
        
    return final_score

# Input data and configuration
data = [0.3, -1.2, 2.5, 4.8, -3.1, 1.7, 5.9, -0.4, 6.2, 3.3, 2.9]
thresholds = [3.0, 4.5]

# Execution point of interest
final_score = calculate_final_score(data, thresholds)
print(f"Result: {final_score}")