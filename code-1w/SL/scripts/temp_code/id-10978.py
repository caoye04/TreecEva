def analyze_pattern(sequence):
    """Irrelevant helper that analyzes repeating patterns (dead end)."""
    count = 0
    for i in range(len(sequence) - 1):
        if sequence[i] == sequence[i+1]:
            count += 1
    return count

# Distractor: Unused complex transformation
def transform_signal(signal):
    return [x ^ 255 for x in signal if x % 2 == 0]

# Decoy data structures
temp_log = [18, 24, 22, 19, 25, 23, 20]
dummy_mask = [1, 0, 1, 1, 0, 1, 0]

# Real input data (simulated sensor readings)
data = [45, 67, 32, 89, 54, 76, 23]

# Misleading weight set 1 (not used)
alt_weights = [0.1, 0.3, 0.2, 0.1, 0.3]

# Actual weights for computation
weights = [0.2, 0.1, 0.3, 0.05, 0.05, 0.2, 0.1]

# Irrelevant normalization function
def normalize(arr):
    m = max(arr)
    return [x / m for x in arr]

# Function that looks important but is never called
def validate_integrity(seq):
    checksum = 0
    for idx, val in enumerate(seq):
        checksum ^= (val + idx) * 3
    return checksum % 100 == 0

# Core processing function with key logic
def process_metrics(values, coeffs):
    accumulator = 0.0
    
    # Apply weights with index tracking
    for index, (val, weight) in enumerate(zip(values, coeffs)):
        if index % 2 == 0:
            # Even indices get squared if above threshold
            if val > 40:
                val = val ** 0.5  # Reverse logic: actually take root
        else:
            # Odd indices are bit-shifted
            val = val >> 1
        accumulator += val * weight
    
    # Secondary adjustment based on sum
    base_sum = sum(v for v in values if v < 70)
    adjustment_factor = (base_sum // 10) * 0.01
    
    # Tertiary filter using set operations (some distraction)
    unique_values = set(values)
    common_with_ref = unique_values & {32, 45, 54, 60, 76}
    bonus = len(common_with_ref) * 0.05
    
    final = accumulator + adjustment_factor + bonus
    
    # Dead code branch - never executed due to logic
    if False and len(values) > 10:
        final *= 1.1
        
    return round(final, 6)

# Execution begins
status_flags = [True, False, True]

# Simulated preprocessing (distractor)
filtered_data = []
for item in data:
    if item >= 30:
        filtered_data.append(item)

# More red herring variables
aggregated = 0
for d in temp_log:
    aggregated += d * 0.5

# Key execution point
final_score = process_metrics(data, weights)

# Output result as required
print(f"Result: {final_score}")