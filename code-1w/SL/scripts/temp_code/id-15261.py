def process_strings(input_list):
    # Irrelevant string processing (distractor)
    processed = [s.upper().strip() for s in input_list if len(s) > 2]
    filtered = [s for s in processed if s.startswith('A')]
    return [s[::-1] for s in filtered]

# Seemingly important data (red herring)
raw_strings = ['apple', 'Art', 'Alice', 'Bob', 'Autumn', 'aardvark']
string_result = process_strings(raw_strings)

# Decoy statistical function (dead code path)
def compute_stats(values):
    mean = sum(values) / len(values)
    variance = sum((x - mean) ** 2 for x in values) / len(values)
    return {'mean': mean, 'variance': variance}

# Real logic begins: sensor data calibration with noise filtering
data = [3, 7, 2, 8, 5, 9, 1, 6, 4]

def filter_outliers(series, threshold=2):
    avg = sum(series) / len(series)
    return [x for x in series if abs(x - avg) <= threshold]

# Bit manipulation for checksum (relevant but obfuscated)
calculate_checksum = lambda seq: int(sum(x << 1 & 255 for x in seq)) % 100

# Recursive peak detection (key concept)
def count_peaks(arr, idx=1, count=0):
    if idx >= len(arr) - 1:
        return count
    if arr[idx] > arr[idx-1] and arr[idx] > arr[idx+1]:
        return count_peaks(arr, idx + 1, count + 1)
    return count_peaks(arr, idx + 1, count)

# Multi-step transformation pipeline
smoothed_data = filter_outliers(data, threshold=3)
decimated = smoothed_data[::2]  # Every other element
checksum = calculate_checksum(decimated)
peak_count = count_peaks(smoothed_data)

# Set operations to identify range coverage (distractor with partial relevance)
full_range = set(range(1, 10))
observed = set(smoothed_data)
coverage_gap = full_range - observed
missing_count = len(coverage_gap)

# Mock ML model confidence (irrelevant)
confidence_scores = [0.85, 0.92, 0.78]
avg_confidence = sum(confidence_scores) / len(confidence_scores)

# Core scoring logic buried among distractions
def calculate_final_score(sensor_data):
    base = sum(x * x for x in sensor_data)  # Sum of squares
    adjustment = peak_count * 10
    penalty = missing_count * 3
    score = base + adjustment - penalty
    # Final nonlinear transform
    return int((score + checksum) ** 0.5 * 17) % 100000

# Critical execution point
final_score = calculate_final_score(data)
print(f"Target result: {final_score}")