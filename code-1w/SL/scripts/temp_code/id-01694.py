from collections import defaultdict, Counter
import math

# Simulated sensor data processing with red herrings
def preprocess_sensor_readings(raw):    processed = []    noise_floor = 0.87    scaling_factor = 2.1    for val in raw:        if val < 0:            val = abs(val)        normalized = (val * scaling_factor) / (noise_floor + 1e-5)        processed.append(round(normalized, 3))    return processed

def compute_entropy(values):    """Misleading function - not actually used in final computation"""    counts = Counter(values)    total = len(values)    entropy = 0    for count in counts.values():        p = count / total        entropy -= p * math.log2(p)    return round(entropy, 4)

def shift_window(sequence, window_size=3):    """Another decoy transformation"""    shifted = []    for i in range(len(sequence)):        window = sequence[max(0, i - window_size + 1):i + 1]        avg = sum(window) / len(window)        shifted.append(round(avg, 3))    return shifted

def generate_fibonacci(n):    """Unused but plausible helper - distractor"""    a, b = 0, 1    fib = []    for _ in range(n):        fib.append(a)        a, b = b, a + b    return fib

def filter_outliers(data, threshold=1.5):    """Looks important but only used on irrelevant path"""    median = sorted(data)[len(data)//2]    filtered = [x for x in data if abs(x - median) / (median + 1e-5) < threshold]    return filtered or [median]

def transform_signal(pattern):    # Core relevant transformation    phase_shift = 0.5    transformed = []    for i, x in enumerate(pattern):        if i % 2 == 0:            transformed.append(x * math.cos(phase_shift))        else:            transformed.append(x * math.sin(phase_shift))    return [round(t, 3) for t in transformed]

def recursive_sum(arr, idx=0):    # Actually used in critical path    if idx >= len(arr):        return 0    return arr[idx] + recursive_sum(arr, idx + 1)

def analyze_pattern(data, limit):    # Key function that determines answer    stats = defaultdict(float)    for i, val in enumerate(data):        if i % 3 == 0 and val > limit:            stats['trigger'] += 1        elif i % 4 == 2:            stats['modulator'] *= 1.1        else:            stats['baseline'] += val    # Only 'trigger' matters    return int(stats['trigger'] * 1000)

# Main execution flow
if __name__ == '__main__':
    # Real input data
    raw_input = [0.12, -0.34, 0.56, 0.78, -0.91, 1.23, 0.45, 0.67]
    
    # Step 1: Preprocess (relevant)
    calibrated = preprocess_sensor_readings(raw_input)
    
    # Step 2: Transform signal (relevant)
    transformed_data = transform_signal(calibrated)
    
    # Distractor 1: Compute entropy (not used)
    entropy_metric = compute_entropy(calibrated)
    
    # Distractor 2: Shift window averaging (computed but unused)
    smoothed = shift_window(calibrated)
    
    # Distractor 3: Generate Fibonacci sequence (red herring)
    fib_sequence = generate_fibonacci(len(calibrated))
    
    # Distractor 4: Filter outliers on wrong data
    cleaned = filter_outliers(smoothed, threshold=1.2)
    
    # Critical parameter
    base_threshold = 0.4
    
    # Distractor 5: Recursive sum on unrelated data
    dummy_sum = recursive_sum(fib_sequence)
    
    # Key operation: analysis based on transformed data and threshold
    final_diagnostic = analyze_pattern(transformed_data, base_threshold)
    
    # Print result as required
    print(f"Result: {final_diagnostic}")