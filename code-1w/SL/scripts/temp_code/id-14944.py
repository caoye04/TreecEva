import math

# Sensor simulation constants (distractor: not actually used in final calculation)
BASE_SENSITIVITY = 0.87
CALIBRATION_OFFSET = -0.03
MAX_BUFFER_SIZE = 256

# Irrelevant sensor metadata
device_info = {
    'model': 'XTR-9000',
    'firmware': '2.1.5',
    'location_id': 4051,
    'last_updated': '2023-11-05'
}

# Dummy historical data (red herring)
historical_max = [18.2, 19.1, 17.8, 20.3, 18.9]
historical_min = [12.4, 11.9, 13.1, 12.7, 12.0]

# Simulated raw sensor input (mixed valid and irrelevant data)
raw_readings = [
    {'val': 15.6, 'status': 'OK', 'type': 'primary'},
    {'val': 14.2, 'status': 'OK', 'type': 'primary'},
    {'val': float('nan'), 'status': 'ERROR', 'type': 'secondary'},  # invalid reading
    {'val': 16.8, 'status': 'OK', 'type': 'primary'},
    {'val': 13.4, 'status': 'OK', 'type': 'backup'},  # backup type ignored
    {'val': 17.1, 'status': 'OK', 'type': 'primary'}
]

# Preprocessing: extract only valid primary readings
valid_primary = [r['val'] for r in raw_readings if r['status'] == 'OK' and r['type'] == 'primary' and not math.isnan(r['val'])]

# Intermediate transformation with decoy operations
offset_correction = sum([0.1 * i for i in range(len(valid_primary))])  # unused distraction
scaling_factor = len(valid_primary) > 3 else 1.1  # boolean expression (used once)

# Apply conditional scaling based on count
if len(valid_primary) >= 4:
    scaled_values = [v * 1.05 for v in valid_primary]
else:
    scaled_values = [v * 0.98 for v in valid_primary]

# Compute moving average window (unused in final path)
moving_avg = []
for i in range(1, len(scaled_values)):
    window = scaled_values[max(0, i-2):i]
    moving_avg.append(sum(window) / len(window))

# Secondary processing chain with red herring functions
def compute_entropy(data):
    """Unused complex function - dead code path"""
    total = sum(data)
    probs = [x / total for x in data]
    return -sum(p * math.log2(p) for p in probs)

def generate_checksum(sequence):
    """Irrelevant utility - never called"""
    return sum(x * (i + 1) for i, x in enumerate(sequence)) % 256

# Signal normalization (has side effect of filtering)
normalized = []
threshold = 15.0
for val in scaled_values:
    if val >= threshold:
        normalized.append(val + 0.25)
    else:
        normalized.append(val - 0.15)

# Data binning logic with conditional expression
bins = [0, 0, 0]
for v in normalized:
    bin_index = 0 if v < 15.0 else (1 if v < 17.0 else 2)
    bins[bin_index] += 1

# Key derived metrics (some used, some not)
peak_value = max(normalized)
avg_normalized = sum(normalized) / len(normalized)
variance_proxy = sum((x - avg_normalized) ** 2 for x in normalized)

# Decoy combinatorics block (completely irrelevant)
def count_triplets(arr):
    """Calculate number of increasing triplets - unused"""
    count = 0
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if arr[i] < arr[j] < arr[k]:
                    count += 1
    return count

triplet_count = count_triplets(valid_primary)  # dead end

# Primary analysis pipeline
processed_data = {
    'samples': len(normalized),
    'exceeds_threshold': bins[2],
    'average': avg_normalized,
    'peak': peak_value,
    'distribution_profile': bins
}

# Final diagnostic engine
threshold_met = processed_data['exceeds_threshold'] >= 2
magnitude_significant = processed_data['peak'] > 17.0
count_trend = processed_data['samples'] > 3

# Conditional expression combining boolean logic and arithmetic
base_score = 45 if threshold_met else 20
bonus = 35 if magnitude_significant and count_trend else 10
penalty = 15 if not count_trend else (25 if variance_proxy < 2.0 else 0)

# Critical execution point
final_diagnostic = base_score + bonus - penalty

print(f"Result: {final_diagnostic}")