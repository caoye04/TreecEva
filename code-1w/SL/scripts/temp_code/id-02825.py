from collections import defaultdict, Counter
import math

# Simulated sensor data aggregation with noise and metadata
raw_readings = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
timestamps = [100, 105, 110, 115, 120, 125, 130, 135, 140, 145]

# Irrelevant auxiliary data (distractor)
system_logs = ['OK', 'WARN', 'OK', 'ERR', 'OK', 'OK', 'WARN', 'OK', 'OK', 'OK']
user_sessions = [(101, 'A'), (102, 'B'), (103, 'C')]

# Noise injection simulation (partially relevant but misleading)
noise_profile = [math.sin(i / 3) for i in range(10)]
distorted_readings = [r + noise for r, noise in zip(raw_readings, noise_profile)]

# Data alignment (red herring - not used later)
aligned_data = list(zip(timestamps, raw_readings, system_logs))

def preprocess(data_seq):
    # Apply smoothing filter (distractor function)
    smoothed = [(data_seq[i-1] + data_seq[i] + data_seq[i+1]) / 3 
                for i in range(1, len(data_seq)-1)]
    smoothed.insert(0, data_seq[0])
    smoothed.append(data_seq[-1])
    return smoothed

# Preprocessing call (but result not used directly)
filtered_readings = preprocess(raw_readings)

# Core transformation: prime gap analysis (relevant path)
prime_gaps = [raw_readings[i] - raw_readings[i-1] for i in range(1, len(raw_readings))]
gap_counts = Counter(prime_gaps)

def transform_sequence(seq):
    # Map each gap to its frequency, then apply logarithmic weighting
    freq_map = defaultdict(float)
    counts = Counter(seq)
    for val in seq:
        freq_map[val] = math.log(counts[val] + 1)
    return [freq_map[gap] for gap in seq]

def generate_signature(gaps):
    # Create a numerical signature using cumulative product and trigonometric mix
    sig = 1.0
    for i, g in enumerate(gaps):
        sig *= (g + 1) * math.cos(i * math.pi / 4 + g)
        if abs(sig) < 1e-6:  # reset near-zero
            sig = 0.1
    return round(sig, 6)

def validate_integrity(data):
    # Fake validation (dead code path)
    total = sum(data)
    return total % 7 == 0

# Real processing begins here
transformed_gaps = transform_sequence(prime_gaps)

# Misleading conditional block (never executed)
if len(raw_readings) > 20:
    transformed_gaps = [x * 2 for x in transformed_gaps]
elif sum(prime_gaps) < 50:
    transformed_gaps = [x + 1 for x in transformed_gaps]

# Actual key transformation
transformed_data = [round(x ** 2, 4) for x in transformed_gaps]

# Configuration object with decoy fields
config = {
    'threshold': 0.5,
    'mode': 'diagnostic',
    'debug': True,
    'cache_size': 1024,
    'algorithm': 'spectral-v2'
}

# Decoy function that looks important but isn't called
def deprecated_analysis(data, mode='legacy'):
    acc = 0
    for d in data:
        acc += d * (d - 1) if d > 1 else 0
    return acc // 7

# Another red herring: recursive checksum (unused)
def calc_recursive_checksum(arr, depth=0):
    if depth >= 3 or len(arr) == 0:
        return 0
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    return (sum(arr) + calc_recursive_checksum(left, depth+1) + 
            calc_recursive_checksum(right, depth+1)) % 97

# Core analysis function (only this matters)
def analyze_pattern(data_list, cfg):
    base = 0
    multiplier = 1
    for i, val in enumerate(data_list):
        if i % 2 == 0:
            base += val * (i + 1)
        else:
            multiplier *= (val % 3 + 1)
    # Final computation
    result = int((base * multiplier) % 100000)
    
    # Inject irrelevant side calculation
    temp_hist = defaultdict(int)
    for d in data_list:
        temp_hist[round(d, 2)] += 1
    
    # Unused slicing distraction
    slice_peak = data_list[1:][::-1][::2]
    
    return result

# Critical execution point
final_diagnostic = analyze_pattern(transformed_data, config)
print(f"Target result: {final_diagnostic}")