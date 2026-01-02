import math

# Simulated sensor data processing with red herrings
def load_calibration_data():
    return [0.1, 0.3, 0.5, 0.7, 0.9]

def calculate_entropy(seq):
    """Irrelevant entropy calculation for distraction"""
    total = 0.0
    for x in seq:
        if x > 0:
            total -= x * math.log(x)
    return round(total, 6)

def shift_window(data, offset=1):
    """Misleading window shifting function (not used in final path)"""
    return data[offset:] + data[:offset]

def extract_peaks(signal):
    """Dead-end peak detection (unused in main logic)"""
    peaks = []
    for i in range(1, len(signal)-1):
        if signal[i-1] < signal[i] > signal[i+1]:
            peaks.append(i)
    return peaks

def filter_outliers(arr, threshold=2.0):
    """Distractor: outlier filtering not actually applied"""
    mean_val = sum(arr) / len(arr)
    std_val = (sum((x - mean_val)**2 for x in arr) / len(arr))**0.5
    return [x for x in arr if abs(x - mean_val) <= threshold * std_val]

def normalize_segment(seg):
    """Normalize segment by maximum (used in real path)"""
    max_val = max(seg)
    return [round(x / max_val, 6) for x in seg] if max_val != 0 else seg

def apply_mask(segment, mask_type='binary'):
    """Apply bitwise-inspired mask (actually just scaling)"""
    if mask_type == 'binary':
        return [int(x >= 0.5) for x in segment]
    elif mask_type == 'quadratic':
        return [x**2 for x in segment]
    return segment

def compute_harmonic_mean(vals):
    """Unused statistical function as red herring"""
    if any(v == 0 for v in vals):
        return 0
    return len(vals) / sum(1/v for v in vals)

def aggregate_transform(segments):
    """Main computation chain: combines slicing, lambdas, and set ops"""
    # Step 1: Normalize each segment
    normalized = [normalize_segment(s) for s in segments]
    
    # Step 2: Apply transformation using lambda (real usage)
    transform_fn = lambda x: round(math.sin(x * math.pi / 2), 6)
    transformed = [[transform_fn(val) for val in seg] for seg in normalized]
    
    # Step 3: Use slicing to extract mid-sections
    mid_sections = [seg[len(seg)//4 : len(seg)*3//4] for seg in transformed]
    
    # Step 4: Flatten list using list comprehension
    flat_values = [item for sublist in mid_sections for item in sublist]
    
    # Step 5: Create set to remove duplicates (set operation)
    unique_vals = list(set(flat_values))
    unique_vals.sort()
    
    # Step 6: Pairwise reduction using modular arithmetic
    reduced = 0
    for i, val in enumerate(unique_vals):
        if i % 3 == 0:  # Every third element
            reduced += int(round(val * 1000))  # Scale to integer
    
    # Step 7: Add checksum from dummy calibration (distractor with partial use)
    calib_data = load_calibration_data()
    checksum = sum(int(c * 10) for c in calib_data)  # Only uses scaled index, not values directly
    
    # Step 8: Final aggregation with irrelevant conditional
    if len(unique_vals) > 10:
        final = reduced * checksum
    else:
        # Actual path
        temp_flag = True
        mode_offset = len(calib_data) % 4  # 5 % 4 = 1
        final = reduced + mode_offset  # Adds 1
    
    return final

# Main execution block
if __name__ == "__main__":
    # Raw input data
    raw_sensor_stream = [
        [10, 20, 30, 40, 50, 40, 30, 20],
        [5, 15, 25, 35, 45, 55, 45, 35],
        [12, 24, 36, 48, 60, 48, 36, 24]
    ]
    
    # Irrelevant preprocessing steps (distractors)
    baseline_shift = 5
    adjusted_stream = [[val - baseline_shift for val in row] for row in raw_sensor_stream]
    
    # More red herring variables
    peak_indices = [extract_peaks(row) for row in adjusted_stream]
    filtered_data = [filter_outliers(row) for row in raw_sensor_stream]
    entropy_scores = [calculate_entropy([x/sum(row) for x in row]) for row in raw_sensor_stream]
    
    # Critical data transformation
    temp_segments = []
    for row in adjusted_stream:
        # Normalize then apply quadratic mask (only normalization matters later)
        norm_seg = normalize_segment(row)
        masked_seg = apply_mask(norm_seg, 'quadratic')  # Not used
        temp_segments.append(norm_seg)  # Only normalized version is appended
    
    # Key computation point
    final_flux = aggregate_transform(temp_segments)
    
    # Print result
    print(f"Result: {final_flux}")