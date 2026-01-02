def sensor_calibration(raw_values):
    calibrated = []
    offset = 0.78
    scale = 1.03
    for v in raw_values:
        corrected = (v + offset) * scale
        if corrected > 100:
            corrected = 97.5  # hard cap
        calibrated.append(corrected)
    return calibrated


def filter_outliers(data, limit=2.5):
    mean_val = sum(data) / len(data)
    variance = sum((x - mean_val) ** 2 for x in data) / len(data)
    std_dev = variance ** 0.5
    filtered = [x for x in data if abs(x - mean_val) / std_dev <= limit]
    return filtered if len(filtered) > 0 else data


def rolling_average(series, window=3):
    if len(series) < window:
        return series
    avgs = []
    for i in range(len(series) - window + 1):
        avgs.append(sum(series[i:i+window]) / window)
    return avgs


def shift_cipher(text, key):
    # Irrelevant function - red herring
    result = ''
    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - base + key) % 26 + base)
        else:
            result += char
    return result


def generate_sequence(n):
    # Dead code path - never used
    seq = [1, 1]
    for i in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq[:n]

# Simulated sensor readings
raw_sensor_data = [89.4, 92.1, 94.8, 101.3, 87.6, 93.2, 96.0, 88.9, 90.5, 95.7]

# Step 1: Calibrate raw values
calibrated_readings = sensor_calibration(raw_sensor_data)

# Step 2: Apply outlier filtering
filtered_readings = filter_outliers(calibrated_readings)

# Step 3: Compute rolling average over 3-element window
smoothed_signal = rolling_average(filtered_readings)

# Step 4: Slice middle portion to simulate time window of interest
trimmed_signal = smoothed_signal[1:-1]  # slicing operation

# Step 5: Compute entropy-like metric for variation analysis
squared_diffs = [(trimmed_signal[i+1] - trimmed_signal[i])**2 for i in range(len(trimmed_signal)-1)]
mean_square_change = sum(squared_diffs) / len(squared_diffs)
fluctuation_index = mean_square_change ** 0.5

# Step 6: Determine adaptive threshold based on fluctuation
threshold = max(1.5, min(5.0, fluctuation_index * 2.1))

# Step 7: Analyze signal against threshold
def analyze_readings(signal, thresh):
    count_above = 0
    cumulative_surplus = 0
    peak_deviation = 0
    baseline = sum(signal) / len(signal)
    
    # Irrelevant nested loop - distractor
    temp_grid = [[0]*3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            temp_grid[i][j] = (i + j) * 0.1  # unused computation
    
    for val in signal:
        deviation = abs(val - baseline)
        if deviation > thresh:
            count_above += 1
            cumulative_surplus += deviation - thresh
            if deviation > peak_deviation:
                peak_deviation = deviation
    
    # Decoy logic with misleading intermediate
    dummy_score = (count_above * 17) % 100
    adjustment = (cumulative_surplus // 0.5) * 0.01
    
    # Actual diagnostic formula
    final_metric = int(baseline) + (peak_deviation * 100) // 1
    return int(final_metric)

# Critical execution point
processed_data = trimmed_signal
final_diagnostic = analyze_readings(processed_data, threshold)

# Print result for evaluation
print(f"Result: {final_diagnostic}")