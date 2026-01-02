import math

def analyze_pattern(sequence):
    """Irrelevant analysis function - distractor"""
    if len(sequence) < 3:
        return False
    trend = all(sequence[i] <= sequence[i+1] for i in range(len(sequence)-1))
    return trend

def compute_checksum(data):
    """Unused checksum logic - red herring"""
    chk = 0
    for item in data:
        chk ^= hash(str(item)) % 256
    return chk

def filter_outliers(stream, threshold=2.0):
    """Partially relevant but ultimately unused filtering"""
    mean_val = sum(stream) / len(stream)
    stdev = (sum((x - mean_val) ** 2 for x in stream) / len(stream)) ** 0.5
    return [x for x in stream if abs(x - mean_val) / stdev < threshold]

def evaluate_stability(ring_buffer):
    """Dead-end stability check with misleading intermediate"""
    diffs = [abs(ring_buffer[i+1] - ring_buffer[i]) for i in range(len(ring_buffer)-1)]
    avg_diff = sum(diffs) / len(diffs)
    return avg_diff < 0.5

def integrate_signal(signal, dt=0.01):
    """Simulates integration but used only on decoy path"""
    integral = 0.0
    for s in signal:
        integral += s * dt
    return integral

def decode_frequency(bandwidth, harmonics):
    """Misleading frequency computation - not part of main logic"""
    base_freq = 440.0
    adjusted = base_freq * (2 ** (harmonics / 12))
    return adjusted % bandwidth

def rotate_phase(components, shift):
    """Bit manipulation decoy with complex arithmetic"""
    shifted = []
    for val in components:
        bits = int(val * 1000) & 0xFFFF
        rotated = ((bits << shift) | (bits >> (16 - shift))) & 0xFFFF
        shifted.append(rotated / 1000.0)
    return shifted

def validate_sequence(pattern):
    """Unused validation routine - dead code"""
    return all(isinstance(p, int) and p >= 0 for p in pattern)

def extract_features(dataset):
    """Distractor-heavy feature extraction with multiple irrelevant outputs"""
    features = {}
    temp_series = []
    for idx, val in enumerate(dataset):
        if idx % 3 == 0:
            temp_series.append(math.log(abs(val) + 1))
        elif idx % 4 == 0:
            temp_series.append(math.sqrt(abs(val)))
    
    # Irrelevant transformations
    processed = [x ** 2 for x in temp_series if x > 0.5]
    smoothed = []
    window = 3
    for i in range(len(processed) - window + 1):
        smoothed.append(sum(processed[i:i+window]) / window)
    
    features['peak'] = max(smoothed) if smoothed else 0.0
    features['entropy'] = -sum(p * math.log(p) for p in smoothed[:5] if p > 0) if smoothed else 0.0
    
    # Real feature used downstream (hidden in noise)
    features['pivot'] = sum(1 for x in dataset if x > 50 and x % 2 == 1)
    
    return features

def process_readings(readings, calib):
    """Main function - computes final diagnostic score"""
    # Step 1: Extract key metric
    total_weight = 0
    for i, reading in enumerate(readings):
        if i % 2 == 1:  # Only odd indices contribute
            scaled = reading * calib[i % len(calib)]
            if scaled > 40:
                total_weight += int(scaled // 2)
    
    # Step 2: Apply conditional adjustment
    adjustment = 0
    for j, val in enumerate(calib):
        if val > 1.5:
            adjustment += (j + 1) * 3
        else:
            adjustment -= j

    # Step 3: Use enumerate and zip as required
    paired = []
    for idx, (r, c) in enumerate(zip(readings, calib * 2)):
        if idx >= len(readings):
            break
        transformed = (r + idx) * c
        paired.append(transformed)
    
    # Step 4: Filter based on condition
    filtered = [p for p in paired if p > 60]
    
    # Step 5: Aggregate using integer division
    aggregate = sum(filtered) // len(filtered) if filtered else 0
    
    # Step 6: Secondary contribution from adjustment
    secondary = abs(adjustment) // 2
    
    # Step 7: Combine via bit manipulation
    combined = (aggregate ^ secondary) & 0xFFFF
    
    # Step 8: Final scaling with rounding
    final_score = round(combined / 3.0, 2)
    
    # Step 9: Add pivot from feature extraction
    ext_features = extract_features(readings)
    pivot_contribution = ext_features['pivot'] * 10
    
    # Step 10: Final diagnostic calculation
    final_diagnostic = int(final_score) + pivot_contribution
    
    return final_diagnostic

# Main execution block
if __name__ == "__main__":
    # Input data
    sensor_data = [23, 67, 12, 88, 45, 73, 54, 19]
    calibration_matrix = [1.2, 2.1, 0.8, 3.3, 1.9]
    
    # Dead code paths - never called
    diagnostics_log = []
    for entry in sensor_data:
        if entry > 70:
            diagnostics_log.append(compute_checksum([entry, entry//2]))
    
    # Simulated alternate processing path
    alt_chain = [math.sin(x/10) for x in sensor_data]
    if evaluate_stability(alt_chain):
        integrated = integrate_signal(alt_chain)
    
    # Key execution point
    final_diagnostic = process_readings(sensor_data, calibration_matrix)
    
    # Output result
    print(f"Result: {final_diagnostic}")