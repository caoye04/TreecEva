def analyze_pattern(sequence):
    if not sequence:
        return 0
    transformed = [x ^ 3 for x in sequence if x % 2 == 1]
    return sum(transformed) * len(sequence)

# Irrelevant helper function (decoy)
def validate_checksum(data):
    return sum(data) % 7 == 0

# Unused complex transformation (dead code path)
def encrypt_sequence(seq, key=5):
    return [(x + key) * 2 for x in seq]

# Distractor: complicated but unused data structure
class PerformanceNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def update(self, delta):
        self.value += delta % 3

# Real logic begins here
def compute_weighted_average(values, weights):
    total = 0.0
    weight_sum = 0.0
    for i in range(len(values)):
        if weights[i] > 0:
            total += values[i] * weights[i]
            weight_sum += weights[i]
    return total / weight_sum if weight_sum != 0 else 0

# Misleading intermediate calculation with plausible naming
def calculate_robustness_index(data):
    peak = max(data) if data else 0
    avg = sum(data) / len(data) if data else 0
    variance = sum((x - avg) ** 2 for x in data) / len(data) if data else 0
    return (peak - avg) / (variance + 1) * 100 if variance > 5 else 50

# Core processing function used later
def extract_features(raw_data):
    filtered = [x for x in raw_data if x > 0]
    normalized = [x / 100.0 for x in filtered]
    scaled = [int(x * 10) for x in normalized]
    return scaled

# Another red herring — looks important but unused
def generate_synthetic_metrics(count):
    result = []
    for i in range(count):
        val = (i * 73 + 19) % 101
        result.append(val)
    return result

# Actual main logic
baseline = [85, 90, 78, 92, 88]
metrics = [88, 91, 80, 94, 87]

# Complex conditional expression combining arithmetic and comparisons
adjustment_factor = 1.05 if sum(m > b for m, b in zip(metrics, baseline)) >= 3 else 0.95

# Bitwise manipulation as part of distractor chain
flag = 0b1010
flag ^= 0b1100
flag |= len(metrics)  # now flag = 15

# Unused list comprehension that appears relevant
relevance_mask = [1 if m >= b else 0 for m, b in zip(metrics, baseline)]

# Linear search disguised as validation
for i in range(len(metrics)):
    if metrics[i] < 75:
        adjustment_factor *= 0.9  # doesn't trigger

# Key computation hidden among noise
feature_vector = extract_features([500, 600, 700, 800])  # [5, 6, 7, 8]
offset = analyze_pattern(feature_vector)  # Only odd numbers: 5,7 → [5^3=6, 7^3=4] → sum=10, *4(seq len)=40

# More misdirection
checksum_data = [1, 2, 3]
valid = validate_checksum(checksum_data)  # True, but unused

# Primary evaluation logic
weight_map = [adjustment_factor] * len(metrics)
score_component = compute_weighted_average(metrics, weight_map)
robustness = calculate_robustness_index(metrics)  # Computed but only partially influences final result

# Conditional expression combining multiple concepts
temp_bias = 5 if offset > 30 else -5

# Final integration point
final_score = score_component + temp_bias + (robustness // 10)

# Print required output
Result: {final_score}