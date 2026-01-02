import math

# Irrelevant helper function (dead code path)
def unused_signal_filter(x):
    return [val for val in x if val % 3 == 0]

# Distractor: complex-looking but unused transformation
class DataObfuscator:
    def __init__(self, key):
        self.key = key

    def scramble(self, data):
        return [d ^ self.key for d in data]

# Real logic begins here

# Sensor data simulation (meaningful input)
sensor_readings = [12, 15, 22, 27, 30, 36, 40, 45, 50, 60]

# Step 1: Filter valid readings above threshold (real use)
valid_readings = list(filter(lambda x: x > 25, sensor_readings))

# Step 2: Apply logarithmic scaling to compress dynamic range
scaled_readings = [round(math.log(r), 3) for r in valid_readings]

# Step 3: Misleading intermediate - looks important but unused later
aggregate_stats = {
    'sum': sum(valid_readings),
    'max': max(valid_readings),
    'count': len(valid_readings),
    'dummy_checksum': sum(r * r for r in valid_readings) // 100
}

# Step 4: Transform via conditional expression and slicing
# Extract middle portion and adjust based on parity
middle_segment = scaled_readings[1:-1]  # Slicing out first and last
adjusted_values = [
    val + 0.1 if i % 2 == 0 else val - 0.05
    for i, val in enumerate(middle_segment)
]

# Step 5: Simulate noise injection (irrelevant)
noise_profile = [math.sin(i * 0.5) * 0.01 for i in range(len(adjusted_values))]
noisy_data = [a + n for a, n in zip(adjusted_values, noise_profile)]  # Never used

# Step 6: Revert to clean data for actual processing
cleaned_data = adjusted_values  # Key transition

# Step 7: Bit manipulation red herring
bit_encoded = [int((val * 100) & 0xFF) for val in cleaned_data]  # Looks critical

# Step 8: Actual relevant transformation - character counting in scientific notation
sci_notations = [f'{val:.2e}' for val in cleaned_data]
char_count_map = {s: len(s.replace('.', '').replace('e', '')) for s in sci_notations}

total_chars = sum(char_count_map.values())

# Step 9: Conditional expression to derive transformed_data
transformed_data = [
    round(float(s)) if '5' in s else round(float(s) * 1.1)
    for s in sci_notations
]

# Step 10: Real analysis function (uses lambda and recursion indirectly)
def analyze_pattern(data):
    # Recursive sum with base case distraction
    def recursive_sum(arr, acc=0):
        if not arr:
            return acc + len(arr)  # len(arr) is always 0 here
        return recursive_sum(arr[1:], acc + arr[0])
    
    # Conditional expression determines mode
    mode = 'high' if sum(data) > 50 else 'low'
    
    # Only this line matters for final result
    raw_total = recursive_sum(data)
    
    # Multiple distractor calculations
    _ = [x ** 2 for x in data if x < 3]  # Unused list comprehension
    _temp_checksum = sum(d * (i+1) for i, d in enumerate(data))  # Unused
    
    # Final computation
    adjustment_factor = 0.9 if mode == 'high' else 1.1
    return int(raw_total * adjustment_factor)

# Step 11: Critical execution point
final_diagnostic = analyze_pattern(transformed_data)

# Output required format
print(f"Result: {final_diagnostic}")