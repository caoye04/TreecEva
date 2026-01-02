def analyze_pattern(sequence):
    if len(sequence) < 5:
        return 0
    peak_count = 0
    for i in range(1, len(sequence) - 1):
        if sequence[i-1] < sequence[i] > sequence[i+1]:
            peak_count += 1
    return peak_count


def smooth_data(data):
    # Smoothing function - not used in final result but looks relevant
    smoothed = [data[0]]
    for i in range(1, len(data)-1):
        avg_val = (data[i-1] + data[i] + data[i+1]) / 3
        smoothed.append(avg_val)
    smoothed.append(data[-1])
    return smoothed


def calculate_baseline(seq):
    # Irrelevant baseline calculation
    total = 0
    for val in seq[:len(seq)//2]:
        total += val * 0.9
    return total // len(seq) if seq else 0


def calculate_efficiency(log_data, threshold):
    # Extract active segments using slicing
    filtered_data = log_data[::2]  # Every other reading
    
    # Track state with auxiliary variables
    duration_counter = 0
    idle_periods = []
    temp_sum = 0
    spike_count = 0
    
    for idx, val in enumerate(filtered_data):
        if val > threshold * 1.5:
            spike_count += 1
        
        if val < threshold:
            duration_counter += 1
        else:
            if duration_counter > 0:
                idle_periods.append(duration_counter)
            duration_counter = 0
    
    if duration_counter > 0:
        idle_periods.append(duration_counter)
    
    # Compute secondary metrics (some irrelevant)
    avg_idle = sum(idle_periods) / len(idle_periods) if idle_periods else 0
    max_gap = max(idle_periods) if idle_periods else 0
    
    # Core logic: efficiency based on pattern analysis
    pattern_strength = analyze_pattern(filtered_data)
    
    # Misleading normalization step
    normalized_spike = spike_count / (len(filtered_data) or 1) * 100
    
    # Actual key computation
    base_efficiency = len(filtered_data) - sum(idle_periods)
    penalty = max_gap * 1.2
    efficiency_score = base_efficiency - penalty + pattern_strength
    
    # Dead code path - never executed under current logic
    if False and normalized_spike > 50:
        efficiency_score *= 0.8
    
    # Extraneous transformation
    adjusted_log = [x ** 0.5 for x in log_data if x > 0]
    ignored_total = sum(adjusted_log)
    
    return efficiency_score

# Main execution
raw_readings = [12, 45, 10, 8, 52, 15, 9, 5, 3, 70, 22, 18, 6, 4, 2, 81, 25, 11, 7, 3]
threshold = 20

baseline_ref = calculate_baseline(raw_readings)
signal_peaks = analyze_pattern(raw_readings)
smoothed_signal = smooth_data(raw_readings)  # Computed but unused

final_output = calculate_efficiency(raw_readings, threshold)

Result: {final_output}