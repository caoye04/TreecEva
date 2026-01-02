import math

# Irrelevant helper function (dead code path)
def unused_helper(x):
    return (x ** 2 + 3 * x + 1) % 7

# Distractor transformation chain
decoy_sequence = [i ^ 5 for i in range(10)]
temporary_buffer = {k: v for k, v in enumerate([x | 2 for x in range(8)])}

# Real data processing components
data_stream = [12, 45, 7, 23, 56, 14]

# Misleading intermediate computations
shadow_accumulator = 0
for val in data_stream:
    shadow_accumulator += (val & (val + 1)) ^ 3

# Decoy filter using lambda (not used in final result)
false_filter = lambda arr: [x for x in arr if x > 30 and (x % 4 == 0)]
filtered_decoy = false_filter(data_stream)

# Actual signal mask based on bit parity
signal_mask = list(map(lambda x: bin(x).count('1') % 2, data_stream))

# Conditional transformer with nested logic
transformed_signal = []
for i, val in enumerate(data_stream):
    if signal_mask[i]:
        if val < 20:
            transformed_signal.append(int(math.sqrt(val)) * 3)
        else:
            transformed_signal.append(val // 4)
    else:
        temp_val = val
        for _ in range(2):
            temp_val = (temp_val ^ 7) & 15
        transformed_signal.append(temp_val)

# Secondary processing: frequency analysis (some values are red herrings)
frequency_map = {}
for num in transformed_signal:
    frequency_map[num] = frequency_map.get(num, 0) + 1

# Unused high-complexity structure
dynamic_weight_matrix = [
    [(i + j) ** 2 % 9 for j in range(3)] 
    for i in range(len(transformed_signal))
]

# Real aggregation logic
aggregation_key = 0
for idx, num in enumerate(transformed_signal):
    if idx % 2 == 0:
        aggregation_key += num * (idx + 1)
    else:
        aggregation_key -= num

# Final pipeline processor
def process_pipeline(input_data):
    # Shadow copy for distraction
    shadow_data = input_data[::-1]
    dummy_result = sum([x << 1 for x in shadow_data]) % 100
    
    # Core logic hidden among distractions
    main_signal = []
    for val in input_data:
        bits = bin(val)[2:]
        ones = bits.count('1')
        if ones > 3:
            main_signal.append(val & 0xF)
        elif ones == 3:
            main_signal.append(val ^ 5)
        else:
            main_signal.append(val | 3)
    
    # Reduction step with conditional weighting
    total = 0
    weights = [2 if x % 2 else 0.5 for x in main_signal]
    for w, v in zip(weights, main_signal):
        if w == 2:
            total += v * w
        else:
            total += int(v * w)
    
    # Final adjustment using arithmetic and bit mix
    return (total + 5) ^ 10

# Execution point of interest
final_output = process_pipeline(data_stream)

# Output the target result
print(f"Target result: {final_output}")