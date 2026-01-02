from collections import defaultdict
import math

# Simulated sensor data aggregation (distractor: some values unused)
sensor_logs = [
    {'id': 'A7', 'reading': 144, 'type': 'alpha'},
    {'id': 'B3', 'reading': 256, 'type': 'beta'},
    {'id': 'A7', 'reading': 9, 'type': 'alpha'},
    {'id': 'C9', 'reading': 512, 'type': 'gamma'}
]

# Irrelevant preprocessing: frequency count by type (not used in final logic)
type_count = defaultdict(int)
for log in sensor_logs:
    type_count[log['type']] += 1

# Core system state variables (some are red herrings)
current_mode = 'diagnostic'
base_offset = 17
legacy_flag = True
device_key = 0b110101

# Real input data for processing
health_data = [12, 15, 22, 8, 45, 30]

# Threshold configuration map (critical for computation)
threshold_map = {
    'low': 10,
    'moderate': 20,
    'high': 30
}

# Decoy transformation: bit-noise generator (unused)
def generate_noise(seed):
    return (seed ^ 0b1010) & 0b1111

# Auxiliary function: computes statistical moment (misleading intermediate)
def compute_moment(data, order=2):
    mean_val = sum(data) / len(data)
    return sum((x - mean_val) ** order for x in data) / len(data)

# UNUSED recursive reducer (dead code path)
def reduce_recursive(arr):
    if len(arr) <= 1:
        return arr[0] if arr else 0
    return reduce_recursive([arr[i] + arr[i+1] for i in range(0, len(arr)-1, 2)])

# Real processing function with conditional logic and list comprehension
def process_metrics(data, thresholds):
    # Step 1: Normalize using base offset (irrelevant to outcome but looks important)
    normalized = [x + base_offset for x in data]  # [29, 32, 39, 25, 62, 47]

    # Step 2: Categorize based on thresholds using conditional expressions
    categories = [
        'low' if x <= thresholds['moderate'] else \
        'high' if x >= thresholds['high'] else 'moderate'
        for x in data
    ]
    
    # Step 3: Count category occurrences (only 'high' matters)
    cat_counts = defaultdict(int)
    for cat in categories:
        cat_counts[cat] += 1

    # Step 4: Apply bitmask derived from device_key (distraction)
    mask = device_key & 0b111  # yields 5
    masked_high = cat_counts['high'] ^ mask  # 2 ^ 5 = 7

    # Step 5: Compute entropy-like measure (decoy calculation)
    total = len(categories)
    entropy = sum([
        -(count/total) * math.log2(count/total) 
        for count in cat_counts.values() if count > 0
    ])  # ~1.459

    # Step 6: Determine adjustment factor via comparison chain
    adjustment = 0
    if cat_counts['low'] > cat_counts['moderate']:
        adjustment = 3
    elif cat_counts['moderate'] > cat_counts['high']:
        adjustment = -2
    else:
        adjustment = 4  # taken: moderate(2) == high(2), so not greater

    # Step 7: Extract relevant reading from sensor logs (red herring)
    critical_reading = None
    for log in sensor_logs:
        if log['id'] == 'B3':
            critical_reading = int(math.sqrt(log['reading']))  # 16
            break

    # Step 8: Final diagnostic computed solely from category logic
    # Only this line determines the answer
    severity_score = cat_counts['high'] * 100 + adjustment * 10
    
    # Final interference: bitwise twist that cancels out
    temp = severity_score ^ device_key
    final_adjusted = temp ^ device_key  # undo XOR: equals original

    return final_adjusted

# Execution point of interest
final_diagnostic = process_metrics(health_data, threshold_map)
print(f"Result: {final_diagnostic}")