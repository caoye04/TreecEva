import itertools

# Sensor simulation and diagnostic system
base_signals = [0.3, 0.7, 1.2, 0.4, 1.9, 2.1, 0.8, 1.1]
decoy_offsets = [0.05, -0.03, 0.07, 0.02, -0.08]

# Irrelevant transformation - red herring
transformed_offsets = [abs(x) ** 2 for x in decoy_offsets if x > -0.05]

# Simulate environmental noise injection (distractor)
noise_matrix = [[(i + j) * 0.01 for j in range(4)] for i in range(len(base_signals))]

# Apply meaningless perturbation to confuse data flow
perturbed_signals = [
    sig + sum(row[:2]) - 0.01 * idx
    for idx, (sig, row) in enumerate(zip(base_signals, noise_matrix))
]

# Real processing begins here
raw_readings = [x * 100 for x in perturbed_signals]  # Scale to integer-like precision

# Misleading filter - looks important but unused later
outlier_mask = [abs(x - sum(raw_readings)/len(raw_readings)) > 50 for x in raw_readings]

# Actual relevant filtering
valid_range = (65, 180)
filtered_data = [x for x in raw_readings if valid_range[0] <= x <= valid_range[1]]

# Decoy statistical analysis (dead code path)
class NoiseModel:
    def __init__(self, data):
        self.data = data
        self.mean = sum(data) / len(data)
    
    def get_variance(self):
        m = self.mean
        return sum((x - m) ** 2 for x in self.data) / len(self.data)

# Unused instance - misleading object usage
decoy_model = NoiseModel(noise_matrix[0])

# Threshold logic with bit manipulation twist
threshold = 100
activation_flag = 0b1010

# Conditional branching with red herring computation
if len(filtered_data) > 5:
    # Looks significant but only modifies unused variable
    temp_weights = list(itertools.accumulate([2] * len(filtered_data), lambda a, b: a * b % 17))
    
    # Real logic embedded within
    clipped = [min(x, 150) for x in filtered_data]
    adjusted_values = [x - 65 for x in clipped]  # Normalize to base
    
    # Key transformation using XOR masking (actual signal extraction)
    masked_values = [x ^ (activation_flag & 0b1111) for x in adjusted_values]
    
    # Final aggregation
    aggregate_score = sum(masked_values) + (len(masked_values) << 2)
else:
    aggregate_score = sum(filtered_data) // 10

# Secondary decoy: complex string-based encoding of data (unused)
symbol_map = {i: chr(97 + (i % 26)) for i in range(50)}
encoded_sequence = ''.join(symbol_map.get(int(x) % 50, '?') for x in raw_readings)

# Core diagnostic processor function
def process_readings(data, limit):
    if not data:
        return -1
    
    # Real computation chain
    base_sum = sum(data)
    count_factor = len(data) * 3
    
    # Multiple layers of adjustment
    intermediate = base_sum - count_factor
    
    # Conditional amplification
    if intermediate > limit:
        intermediate *= 2
    else:
        intermediate += 50
    
    # Bitwise fine-tuning
    tuned = intermediate ^ 0b1101
    
    # Final scaling down via float conversion (answer becomes decimal)
    result = tuned / 7.0
    
    # Dead code - misleading early return check
    if result < 0:
        return 0.0
        extra_calc = [x for x in data if x % 2 == 0]  # unreachable
    
    return result

# Critical execution point
final_diagnostic = process_readings(filtered_data, threshold)

# Output target result
print(f"Target result: {final_diagnostic}")