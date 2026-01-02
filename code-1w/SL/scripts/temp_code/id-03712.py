import math

# Simulated sensor readings with noise
data_stream = [14, -5, 8, 0, 22, -11, 7, 3, 19, -6]

# Irrelevant transformation: frequency weights (not used in final path)
frequency_weights = [math.sin(i * 0.5) for i in range(len(data_stream))]
weighted_sum = sum(abs(data_stream[i] * frequency_weights[i]) for i in range(len(data_stream)))

# Noise threshold based on statistical dispersion
std_dev = (sum((x - sum(data_stream)/len(data_stream))**2 for x in data_stream) / len(data_stream)) ** 0.5
dynamic_threshold = std_dev * 1.5

# Filtering significant signals above dynamic threshold
filtered_data = [x for x in data_stream if abs(x) > dynamic_threshold]

# Secondary filter: only odd-indexed elements from original stream (distractor list)
spurious_filtered = [data_stream[i] for i in range(1, len(data_stream), 2)]
spurious_sum = sum(spurious_filtered)

# Core signal processing function
def process_signals(signals):
    if not signals:
        return 0
    
    # Bitwise stabilization mask (irrelevant to outcome but adds complexity)
    mask = 0b101010
    masked_values = [s ^ mask & 0xF for s in signals]
    
    # Conditional amplification based on parity chain
    amplified = []
    for val in signals:
        if val > 0 and (val & 1):  # positive and odd
            amplified.append(val * 3)
        elif val < 0:
            amplified.append(abs(val) + 2)
        else:
            amplified.append(val)
    
    # Nested logic: apply logarithmic scaling only if total power exceeds limit
    total_power = sum(x ** 2 for x in amplified)
    if total_power > 100:
        scaled = [math.log(p + 1) for p in amplified]
        decision_factor = sum(scaled) / len(scaled)
        if decision_factor > 2.0:
            final_adjustment = int(decision_factor * 2)
        else:
            final_adjustment = 5
    else:
        final_adjustment = 1
    
    # Final aggregation with offset
    base_result = sum(amplified) + final_adjustment
    return base_result

# Misleading pre-processing step (dead-end computation)
temp_analysis = [x for x in data_stream if x % 4 == 0]
shadow_metric = sum(temp_analysis) * 0.5

# Critical execution point
final_output = process_signals(filtered_data)

print(f"Result: {final_output}")