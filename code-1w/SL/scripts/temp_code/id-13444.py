import math

# Irrelevant constants (distractors)
MAX_BUFFER_SIZE = 1024
DEFAULT_TIMEOUT = 30
DEBUG_MODE = False
DUMMY_FACTOR = 0.987

# Misleading intermediate variables
auxiliary_data = [i * 0.5 for i in range(10)]
temp_offset = sum(auxiliary_data) / len(auxiliary_data)

# Unused function (dead code path)
def legacy_conversion(x):
    return x * 0.76 + 12  # Never called

# Simulated sensor readings (some relevant, some not)
sensor_readings = [127, 130, 118, 142, 135, 120, 110]
calibration_factor = 1.05
adjusted_readings = list(map(lambda x: (x * calibration_factor) + 3, sensor_readings))

# Data transformation chain with distractors
baseline_shift = 15
fused_metrics = []
for val in adjusted_readings:
    if val > 130:
        fused_metrics.append(val * 1.1)
    elif val < 120:
        fused_metrics.append(val * 0.9)
    else:
        fused_metrics.append(val)

# Secondary irrelevant processing
outlier_suppression = [x for x in fused_metrics if 110 <= x <= 150]
suppressed_avg = sum(outlier_suppression) / len(outlier_suppression)

# Core calculation inputs
process_sequence = [(2, 4), (3, 3), (5, 2)]  # exponent pairs

# Decoy accumulator (looks important but unused)
total_cumulative_score = 0
for a, b in process_sequence:
    total_cumulative_score += a ** b

# Real computation buried among noise
def calculate_entropy(arr):
    entropy = 0.0
    total = sum(arr)
    for x in arr:
        if x > 0:
            prob = x / total
            entropy -= prob * math.log(prob)
    return entropy

# Another decoy function
def compute_aggregate(data):
    return sum([d**2 for d in data]) * 0.1

# Main logic hidden in abstraction
def calculate_thermal_output(seq):
    base = 0
    multiplier = 1
    for a, b in seq:
        base += a ** b  # 2^4 + 3^3 + 5^2 = 16 + 27 + 25 = 68
    
    # Additional transformations
    intermediate = base * 2.5
    
    # Red herring: complex-looking but unused expression
    derived_constant = math.sqrt(sum([x*x for x in sensor_readings])) / 100
    
    # Actual final step
    result = int(intermediate) + len(process_sequence)  # 68*2.5 = 170 → int(170)=170 → 170+3=173
    
    # More dead computations
    buffer = []
    for i in range(5):
        buffer.append((result * i) % 17)
    
    return result

# Key execution point
thermal_capacity = calculate_thermal_output(process_sequence)

# Final output
print(f"Result: {thermal_capacity}")