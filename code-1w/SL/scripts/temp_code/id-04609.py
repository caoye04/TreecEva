import math

# Simulated sensor data processing with diagnostic analysis
def collect_samples(base, count):
    return [base * (i + 1) ** 1.5 for i in range(count)]

def filter_outliers(data, limit):
    return [x for x in data if x <= limit]

def apply_calibration(signal):
    calibrated = []
    for x in signal:
        if x < 10:
            calibrated.append(x * 1.2)
        elif x < 25:
            calibrated.append(x * 1.1)
        else:
            calibrated.append(x * 0.95)
    return calibrated

def generate_sequence(n):
    # Irrelevant Fibonacci-like sequence generator (distractor)
    seq = [1, 1]
    for i in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq

def compute_entropy(data):
    # Irrelevant entropy calculation (dead path)
    total = sum(data)
    probs = [x / total for x in data]
    return -sum(p * math.log2(p) for p in probs if p > 0)

def rolling_window(data, size=3):
    # Creates overlapping sublists (used in transformation)
    return [data[i:i+size] for i in range(len(data) - size + 1)]

def transform_window(win):
    # Transform each window into a scalar using mixed operations
    a, b, c = win
    return abs(a - b) ** 1.1 + (c * 0.5) - (a * b * 0.01)

def analyze_pattern(dataset, cutoff):
    # Core logic: count how many transformed values exceed threshold
    count = 0
    for val in dataset:
        if val > cutoff:
            count += 1
    return count * 17  # Final scaling factor

# Begin main execution
raw_readings = collect_samples(base=2.5, count=12)
denoised_signal = filter_outliers(raw_readings, limit=40.0)
calibrated_data = apply_calibration(denoised_signal)

# Dead branch: unused recursive function (red herring)
def recursive_sum(n):
    return n + recursive_sum(n - 1) if n > 0 else 0

unused_entropy = compute_entropy(calibrated_data)  # Computed but not used

# Generate irrelevant sequence
fib_approx = generate_sequence(len(calibrated_data))

# Key transformation path
windowed_data = rolling_window(calibrated_data, size=3)
transformed_data = [transform_window(window) for window in windowed_data]

# Phantom variable with misleading name
aggregated_metric = sum(transformed_data) / len(transformed_data)

threshold = 7.3

# This is the critical statement
final_diagnostic = analyze_pattern(transformed_data, threshold)

# Distractor: complex-looking but unused bitwise computation
obfuscated_flag = (len(transformed_data) << 3) ^ 0xFF & int(aggregated_metric)

# Print result as required
print(f"Result: {final_diagnostic}")