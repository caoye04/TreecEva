from collections import defaultdict, Counter

# Simulated sensor data processing with diagnostic analysis
def preprocess_readings(raw):
    processed = []
    for val in raw:
        if val < 0:
            val = abs(val) * 0.9
        processed.append(round(val + 0.001, 3))
    return processed

# Irrelevant transformation - decoy function
def transform_signal(x):
    return [v * 1.5 for v in x if v > 5]

# Core filtering logic (relevant)
def filter_anomalies(data, limit=100):
    return [x for x in data if 5 <= x <= limit]

# Red herring: complex but unused statistical function
def compute_entropy(arr):
    counts = Counter(arr)
    total = len(arr)
    entropy = 0
    for count in counts.values():
        p = count / total
        entropy -= p * (p ** 0.5)  # Not actual entropy, just looks plausible
    return round(entropy, 4)

# Decoy state tracker (never used in final result)
class StateMonitor:
    def __init__(self):
        self.log = []
        self.active = True

    def update(self, val):
        self.log.append(f"Update: {val}")

# Unused recursive helper - distractor
def binary_partition(n):
    if n <= 1:
        return [n]
    return binary_partition(n // 2) + [n % 2]

# Real threshold logic (used)
threshold_lambda = lambda level: (level * 1.75) if level < 80 else (level * 1.1)

# Diagnostic analyzer - uses multiple concepts
def analyze_readings(readings, threshold_fn):
    stats = defaultdict(int)
    for r in readings:
        if r > threshold_fn(50):
            stats['high'] += 1
        elif r > threshold_fn(30):
            stats['medium'] += 1
        else:
            stats['low'] += 1
    
    # Complex logic chain
    score = 0
    score += stats['high'] * 7
    score -= stats['medium'] * 2
    adjustment = (stats['low'] ** 1.5) // 1
    score += int(adjustment)
    
    # Nested conditional with bit manipulation red herring
    flag = 0b1010
    if stats['high'] > stats['medium']:
        flag ^= 0b1111
        if stats['low'] == 0:
            flag >>= 2
    score ^= flag  # Actual use of flag
    
    # String-based distractor (irrelevant to outcome)
    debug_tag = "DIAG_" + "".join([chr(97 + (score % 26))]) + "X"
    
    # Final computation - depends on prior steps
    final_value = (score * 3) + (len(readings) % 10)
    return final_value

# Primary execution flow
if __name__ == "__main__":
    # Initial dataset
    sensor_input = [12.5, -8.3, 45.0, 150.2, 67.8, 3.2, 95.1, 200.0, 77.7]
    
    # Step 1: Preprocess
    cleaned = preprocess_readings(sensor_input)
    
    # Step 2: Filter anomalies (key step)
    filtered_data = filter_anomalies(cleaned, limit=120)
    
    # Irrelevant side calculation
    peak = max(filtered_data) * 1.05 if filtered_data else 0
    baseline_avg = sum(filtered_data[:3]) / 3 if len(filtered_data) >= 3 else 0
    
    # Define threshold function (used later)
    threshold_func = lambda base: threshold_lambda(base)
    
    # Dead code path - never executed
    debug_mode = False
    if debug_mode:
        monitor = StateMonitor()
        for v in filtered_data:
            monitor.update(v)
    
    # Core analysis - produces answer
    final_diagnostic = analyze_readings(filtered_data, threshold_func)
    
    # Output result
    print(f"Result: {final_diagnostic}")