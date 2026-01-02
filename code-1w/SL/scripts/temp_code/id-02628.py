import math

# Simulated sensor data processing with diagnostic analysis
def collect_samples(base_signal, noise_level, duration):
    samples = []
    for t in range(duration * 10):
        noise = (t % 7) * noise_level / 10
        signal = base_signal * math.sin(t / 5.0) + noise
        samples.append(round(signal, 2))
    return samples

def filter_outliers(data, limit):
    cleaned = []
    for x in data:
        if -limit <= x <= limit:
            cleaned.append(x)
    return cleaned

def rolling_average(values, window_size):
    averages = []
    for i in range(len(values) - window_size + 1):
        window = values[i:i + window_size]
        avg = sum(window) / len(window)
        averages.append(round(avg, 2))
    return averages

def shift_phase(sequence, offset):
    return sequence[offset:] + sequence[:offset]

def compute_entropy(values):
    # Dummy entropy-like computation for distraction
    total = sum(abs(v) for v in values)
    norm = [abs(v) / total for v in values if v != 0]
    entropy = -sum(p * math.log(p) for p in norm)
    return round(entropy, 4)

def detect_cycles(seq):
    # Irrelevant cycle detection (unused in final logic)
    cycles = 0
    for i in range(1, len(seq)):
        if seq[i] == seq[i-1]:
            cycles += 1
    return cycles

def compress_data(arr):
    # Unused compression function (dead code path)
    compressed = []
    count = 1
    for i in range(1, len(arr)):
        if arr[i] == arr[i-1]:
            count += 1
        else:
            compressed.append((arr[i-1], count))
            count = 1
    if arr:
        compressed.append((arr[-1], count))
    return compressed

def extract_features(dataset):
    # Extracts statistical features — some used, others not
    size = len(dataset)
    midpoint = size // 2
    left_half = dataset[:midpoint]
    right_half = dataset[midpoint:]
    
    mean_left = sum(left_half) / len(left_half) if left_half else 0
    mean_right = sum(right_half) / len(right_half) if right_half else 0
    trend = round(mean_right - mean_left, 2)
    
    peak = max(dataset)
    valley = min(dataset)
    spread = round(peak - valley, 2)
    
    # Distractor: unused advanced metrics
    squared_sum = sum(x**2 for x in dataset)
    rms = math.sqrt(squared_sum / len(dataset))
    
    # Return relevant and irrelevant features
    return {
        'trend': trend,
        'spread': spread,
        'peak': peak,
        'valley': valley,
        'mean_left': round(mean_left, 2),
        'mean_right': round(mean_right, 2),
        'rms': round(rms, 3),  # distractor
        'size': size
    }

def transform_sequence(raw):
    # Apply transformations including slicing and shifting
    doubled = [x * 2 for x in raw]
    shifted = shift_phase(doubled, 3)
    halved = [x / 2 for x in shifted]
    
    # Critical slicing operation
    cropped = halved[2:-2]  # removes unstable edge readings
    
    smoothed = rolling_average(cropped, 3)
    normalized = [round(x - 0.5, 2) for x in smoothed]  # baseline correction
    
    return normalized

def analyze_pattern(processed, cutoff):
    # Core decision logic
    magnitude = sum(abs(x) for x in processed)
    length = len(processed)
    density = round(magnitude / length, 3) if length else 0
    
    # Diagnostic rules
    if density > cutoff:
        flag = 3
    elif density > cutoff * 0.7:
        flag = 2
    else:
        flag = 1
    
    # Final result derived from reasoning chain
    score = int((density * 100) + flag * 10)
    return score

# --- Main Execution ---
if __name__ == "__main__":
    # Initial parameters
    signal_strength = 4.5
    interference = 1.8
    time_window = 12
    
    # Step 1: Collect raw sensor data
    raw_readings = collect_samples(signal_strength, interference, time_window)
    
    # Step 2: Filter extreme outliers
    filtered_readings = filter_outliers(raw_readings, 5.0)
    
    # Step 3: Extract preliminary statistics (some unused)
    stats = extract_features(filtered_readings)
    
    # Distractor variables
    entropy_measure = compute_entropy(filtered_readings)
    cycle_count = detect_cycles(filtered_readings)
    compressed_form = compress_data(filtered_readings)
    
    # Step 4: Transform the sequence into analyzable format
    transformed_data = transform_sequence(filtered_readings)
    
    # Step 5: Set dynamic threshold based on feature (only some matter)
    base_threshold = 0.8
    adjustment = 0.1 if stats['trend'] > 0 else 0
    threshold = base_threshold + adjustment
    
    # Step 6: Run final diagnostic analysis
    final_diagnostic = analyze_pattern(transformed_data, threshold)
    
    # Output target result
    print(f"Result: {final_diagnostic}")