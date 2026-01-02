def analyze_trend(values):
    trend = 0
    for i in range(1, len(values)):
        if values[i] > values[i-1]:
            trend += 1
        elif values[i] < values[i-1]:
            trend -= 1
    return trend

# Simulate sensor data with noise filtering
data_stream = [12, 15, 14, 16, 18, 17, 20, 21, 19]
filtered_data = [x for x in data_stream if x >= 15]
baseline_shift = sum(filtered_data) // len(filtered_data)

# Misleading computation - unused in final result
redundant_sum = 0
for val in data_stream:
    redundant_sum += val * 2 - 5

# Process data segments
segment_a = filtered_data[:3]
segment_b = filtered_data[3:]

# Compute metrics with conditional logic
a_trend = analyze_trend(segment_a)
b_trend = analyze_trend(segment_b)

trend_balance = abs(a_trend - b_trend)

# Dummy string operation to add distraction
data_tag = ''.join([chr(97 + (i % 26)) for i in range(10)])
checksum = sum(ord(c) for c in data_tag if c in 'aeiou')

# Core logic with slicing and conditionals
if len(segment_b) > 2:
    midpoint = segment_b[len(segment_b)//2]
    adjusted_mid = midpoint - baseline_shift
else:
    adjusted_mid = 0

processed_data = [
    sum(segment_a),
    sum(segment_b),
    a_trend if a_trend > 0 else -a_trend,
    b_trend + adjusted_mid,
    trend_balance
]

# Aggregation function with conditional expression and slicing
def aggregate_performance(data):
    # Extra distraction variables
    temp_factor = 1.5
    debug_trace = data[::-1]  # reversed slice, not used directly
    offset = len(debug_trace) > 3 ? 2 : 1  # Python doesn't have ternary operator like this
    offset = 2  # correction: use proper syntax
    
    base = sum(data[:4])
    penalty = data[-1] * 0.5
    bonus = 10 if all(x > 0 for x in data) else 0
    
    # Unused statistical distraction
    mean_val = sum(data) / len(data)
    variance_proxy = sum((x - mean_val) ** 2 for x in data) / len(data)
    
    return int(base - penalty + bonus)

final_score = aggregate_performance(processed_data)
print(f"Result: {final_score}")