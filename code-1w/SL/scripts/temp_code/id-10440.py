import math

# Simulated sensor data processing with diagnostic analysis
def fetch_raw_readings():
    return [5, -3, 8, 0, -1, 12, 7, 2, -4, 6]

def clean_data(readings):
    # Irrelevant transformation (distractor)
    offset = sum(readings) // len(readings)
    cleaned = [x + offset for x in readings]
    normalized = [max(0, x) for x in cleaned]  # Loses negative info
    return normalized

def compute_entropy(values):
    # Dead function - not used in main logic
    total = sum(values)
    if total == 0:
        return 0.0
    entropy = 0.0
    for v in values:
        p = v / total
        if p > 0:
            entropy -= p * math.log(p)
    return round(entropy, 4)

def filter_outliers(data, limit=10):
    # Filters values above limit (mostly irrelevant here)
    return [x for x in data if x <= limit]

def shift_window(sequence, steps):
    # Circular shift (unused path)
    n = len(sequence)
    if n == 0:
        return sequence
    steps = steps % n
    return sequence[-steps:] + sequence[:-steps]

def augment_data(seq):
    # Adds derived features (distractor computation)
    squared = [x**2 for x in seq]
    smoothed = [seq[i] for i in range(len(seq)) if i % 2 == 0]
    return squared + smoothed

def preprocess(signal):
    # Main preprocessing chain
    shifted = [x + 1 for x in signal]
    rectified = [abs(x) for x in shifted]
    return [x for x in rectified if x % 2 == 1]  # Keep only odd values

def evaluate_threshold(value, mode='strict'):
    # Conditional expression used
    return value > 5 if mode == 'strict' else value >= 3

def count_peaks(series, t):
    count = 0
    for val in series:
        # Logical combination and comparison
        if evaluate_threshold(val, 'strict') and (val & 1 == 1):  # Greater than 5 AND odd
            count += 1
    return count

def generate_checksum(items):
    # Bitwise decoy operation
    checksum = 0
    for item in items:
        checksum ^= item  # XOR into checksum (unused result)
    return checksum  # Never actually used

def analyze_signal(data, thresh):
    # Core logic hidden among distractions
    base_score = sum(data)
    peak_count = count_peaks(data, thresh)
    modifier = 3 if peak_count >= 2 else -2
    # Critical calculation
    intermediate = (base_score * peak_count) + modifier
    # Additional red herring: complex unused tuple unpacking
    extra_data = [(x, x*2, x//2) for x in data if x > thresh]
    aux_total = sum([t[1] for t in extra_data]) if extra_data else 0
    dummy_flag = any((x > 100) for x in [aux_total])
    # Final result depends only on core logic
    return intermediate + (100 if dummy_flag else 0)

# --- Execution Flow ---
raw_sensor_data = fetch_raw_readings()
cleaned_readings = clean_data(raw_sensor_data)  # Distractor step
filtered_readings = filter_outliers(cleaned_readings)  # Mostly passes through
processed_data = preprocess(filtered_readings)  # Key transformation
threshold = 4

# Generate unused diagnostics (distractors)
dummy_entropy = compute_entropy(cleaned_readings)
augmented_set = augment_data(processed_data)
shifted_frame = shift_window(augmented_set, 3)
checksum_value = generate_checksum(shifted_frame)  # Computed but ignored

# Critical execution point
final_diagnostic = analyze_signal(processed_data, threshold)

print(f"Result: {final_diagnostic}")