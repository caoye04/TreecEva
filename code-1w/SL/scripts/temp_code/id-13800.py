import math

# Simulated sensor grid data from environmental monitoring stations
def generate_sensor_readings():
    base_values = [23.4, 19.5, 27.3, 18.2, 24.1, 26.7, 20.3]
    adjustments = [0.1 * i for i in range(7)]
    readings = [base_values[i] + adjustments[i] for i in range(7)]
    return readings

# Legacy function - not used in current logic (red herring)
def compute_legacy_index(data):
    acc = 0
    for x in data:
        acc += x ** 0.5
    return acc / len(data)

# Irrelevant transformation chain (distractor)
def transform_signal(signal):
    if not signal:
        return []
    temp = [s * 1.05 for s in signal]
    temp = [t + 2.1 for t in temp]
    return [math.sin(x) for x in temp]

# Unused helper with misleading name (dead path)
def get_normalization_factor(arr):
    total = sum(arr)
    factor = total / (len(arr) + 1e-9)
    return factor if factor > 0 else 1

# Decoy data structure (irrelevant)
baseline_profiles = {
    'summer': [25.0, 28.1, 24.3, 26.7],
    'winter': [18.2, 16.5, 19.0, 17.3],
    'spring': [21.0, 20.8, 22.1, 23.0],
    'fall': [19.9, 18.7, 20.2, 19.5]
}

# Core processing functions
def extract_peaks(data, threshold=22.0):
    peaks = []
    for idx, val in enumerate(data):
        if val > threshold:
            peaks.append((idx, val))
    return peaks

def calculate_entropy(data):
    total = sum(data)
    if total == 0:
        return 0.0
    probabilities = [x / total for x in data]
    entropy = 0.0
    for p in probabilities:
        if p > 0:
            entropy -= p * math.log(p)
    return round(entropy, 6)

def apply_weight_mask(data, mask):
    return [data[i] * mask[i] for i in range(len(data))]

def aggregate_metrics(data, weights):
    # Step 1: Apply weight mask
    weighted_data = apply_weight_mask(data, weights)
    
    # Step 2: Extract significant readings above threshold
    significant = extract_peaks(weighted_data, threshold=25.0)
    
    # Step 3: Compute entropy of original data (not weighted!)
    raw_entropy = calculate_entropy(data)
    
    # Step 4: Process peak indices and values
    peak_sum = sum([val for _, val in significant])
    peak_count = len(significant)
    
    # Step 5: Combine metrics with fixed formula
    if peak_count == 0:
        composite = raw_entropy * 100
    else:
        peak_avg = peak_sum / peak_count
        composite = (peak_avg * 2.5) + (raw_entropy * 10) + (peak_count * 5)
    
    # Step 6: Apply final nonlinear transformation
    final_score = int(composite * 10) / 10.0  # Round to 1 decimal
    
    # Step 7: Additional adjustment based on bit pattern of count
    control_flag = len(data) ^ 7  # XOR operation
    if control_flag & 1:  # Check least significant bit
        final_score += 1.5
    
    # Step 8: Final clamping and scaling
    final_score = max(final_score, 10.0)
    final_score = min(final_score, 100.0)
    
    return final_score

# Main execution block
if __name__ == "__main__":
    # Generate real data
    grid_data = generate_sensor_readings()
    
    # Prepare weight configuration (simulates calibration factors)
    weights = [1.1, 0.9, 1.2, 0.8, 1.0, 1.3, 0.7]
    
    # Transform but do NOT use (distractor)
    transformed = transform_signal(grid_data)
    
    # Calculate legacy index but ignore result (red herring)
    _ = compute_legacy_index(grid_data)
    
    # Extract peaks for logging (unused)
    _ = extract_peaks(grid_data, threshold=20.0)
    
    # Create zip object for parallel iteration (meaningful use)
    indexed_weights = list(zip(range(len(weights)), weights))
    
    # Recompute weights using enumerate (actual relevant logic)
    adjusted_weights = []
    for i, w in enumerate(weights):
        if i % 2 == 0:
            adjusted_weights.append(w * 1.05)
        else:
            adjusted_weights.append(w * 0.95)
    
    # Use adjusted weights in final calculation
    final_diagnostic = aggregate_metrics(grid_data, adjusted_weights)
    
    # Print result as required
    print(f"Result: {final_diagnostic}")