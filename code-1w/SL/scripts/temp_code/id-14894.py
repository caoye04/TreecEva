import math

# Simulated sensor data processing with diagnostic pipeline
def collect_sensor_data():
    raw_readings = [0.78, 0.65, 0.91, 0.44, 0.58]
    timestamps = [1623456780, 1623456781, 1623456782, 1623456783, 1623456784]
    metadata = {'sensor_id': 'SNSR-7X', 'calibration': 1.02, 'version': '2.1'}
    return list(zip(timestamps, raw_readings))


def filter_noise(data, threshold=0.5):
    filtered = []
    noise_log = []  # distractor: unused later
    for ts, val in data:
        if val >= threshold:
            filtered.append((ts, val * 1.05))
        else:
            noise_log.append(ts)  # logged but not used
    return filtered


def extract_peaks(signal_list):
    peaks = []
    for i, (t, v) in enumerate(signal_list):
        prev_val = signal_list[i-1][1] if i > 0 else -1
        next_val = signal_list[i+1][1] if i < len(signal_list)-1 else -1
        if v > prev_val and v > next_val:
            peaks.append((t, round(v, 2)))
    return peaks


def generate_checksum(items):
    # irrelevant utility function (distractor)
    chk = 0
    for item in items:
        chk ^= hash(str(item))
    return chk % 1000


def compute_entropy(values):
    # misleading advanced computation (dead end)
    total = sum(values)
    probs = [v / total for v in values]
    return -sum(p * math.log2(p) for p in probs)


def frame_window(peaks, window_size=2):
    frames = []    
    for i in range(0, len(peaks), window_size):
        frame = tuple(peaks[i:i+window_size])
        frames.append(frame)
    padding = tuple()  # red herring
    if len(peaks) % window_size != 0:
        padding = ((-1, -1),)  # never actually appended
    return frames


def transform_coordinates(frames):
    # complex-looking transformation with partial relevance
    transformed = []
    temp_store = []  # distractor list
    for idx, frame in enumerate(frames):
        x_comp = sum(t for t, v in frame)
        y_comp = sum(v**2 for t, v in frame)
        transformed.append((x_comp, round(math.sqrt(y_comp), 3)))
        temp_store.append({'index': idx, 'raw': frame})  # stored but unused
    return transformed


def detect_anomalies(grid_points):
    anomalies = set()
    for i, (x, y) in enumerate(grid_points):
        if x % 100 == 0 or y > 100:  # unlikely conditions
            anomalies.add(i)
    return anomalies  # returned but ignored later


def calculate_baseline(measurements):
    # decoy function with plausible name
    sorted_vals = sorted([v for _, v in measurements])
    mid = len(sorted_vals) // 2
    return (sorted_vals[mid] + sorted_vals[~mid]) / 2


def analyze_signal(thermal_map):
    base_metric = 0
    for x, y in thermal_map:
        contribution = (x // 100) * (y * 10)
        base_metric += contribution
    
    # Final diagnostic uses set operations (required feature)
    critical_set = {int(x) for x, _ in thermal_map if x > 1623456000}
    reference_set = {1623456782, 1623456783, 1623456784, 1623456785}
    overlap = critical_set & reference_set
    adjustment = len(overlap) * 17
    
    # Secondary factor using enumerate and zip (required features)
    indices = [i for i, _ in enumerate(thermal_map)]
    pairs = list(zip(indices, [x for x, _ in thermal_map]))
    bonus = sum(i for i, x in pairs if x > 1623456782)
    
    final_diagnostic = base_metric + adjustment + bonus
    return final_diagnostic

# Main execution flow
if __name__ == '__main__':
    # Step 1: Collect raw data
    readings = collect_sensor_data()
    
    # Step 2: Filter low-amplitude noise
    cleaned = filter_noise(readings)
    
    # Step 3: Identify signal peaks
    peak_values = extract_peaks(cleaned)
    
    # Step 4: Irrelevant entropy calculation (distraction)
    entropy = compute_entropy([v for _, v in peak_values])
    
    # Step 5: Window into processable frames
    processed_frames = frame_window(peak_values)
    
    # Step 6: Transform to coordinate space
    mapped_grids = transform_coordinates(processed_frames)
    
    # Step 7: Spurious anomaly check (no effect on output)
    fault_indices = detect_anomalies(mapped_grids)
    
    # Step 8: Decoy baseline (unused)
    baseline = calculate_baseline(readings)
    
    # Step 9: Core analysis (answer point)
    final_diagnostic = analyze_signal(mapped_grids)
    
    # Output target result
    print(f"Result: {final_diagnostic}")