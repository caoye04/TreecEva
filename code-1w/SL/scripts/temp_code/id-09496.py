def analyze_sequence(seq):
    filtered = [x for x in seq if x % 3 == 0]
    shifted = [x >> 1 for x in filtered]
    return shifted

sequence = list(range(15, 45, 2))
offsets = {i: val ** 0.5 for i, val in enumerate(sequence)}
mask_set = {i for i in range(len(sequence)) if i % 4 == 0}

# Simulate data preprocessing with irrelevant transformations
temp_stats = {
    'max_val': max(sequence),
    'min_val': min(sequence),
    'range': max(sequence) - min(sequence),
    'avg': sum(sequence) / len(sequence)
}

adjusted = [x + 1 for x in sequence if x < 35]
dropped_count = len(sequence) - len(adjusted)

processed_data = []
for index, value in enumerate(sequence):
    if index in mask_set:
        processed_data.append(value // 2)
    elif value % 5 == 0:
        processed_data.append(value * 2)
    else:
        processed_data.append(value + 3)

# Irrelevant slicing and set operations
tail_slice = processed_data[-7:]
unique_tails = set(tail_slice)
duplicate_check = len(tail_slice) - len(unique_tails)

# Red herring dictionary accumulation
count_map = {}
for item in processed_data:
    rounded = int(item / 5) * 5
    count_map[rounded] = count_map.get(rounded, 0) + 1

sorted_keys = sorted(count_map.keys())
median_key = sorted_keys[len(sorted_keys)//2] if sorted_keys else 0

# Actual computation path (short-circuited by logic)
def calculate_final_score(data):
    base = sum(data[i] for i in range(0, len(data), 3))
    penalty = len([x for x in data if x > 40]) * 2
    bonus = len(set(data)) // 4
    intermediate = base - penalty + bonus
    # Apply non-linear adjustment
    adjusted_intermediate = int(intermediate ** 0.5 * 3)
    
    # Distractor: unused branch
    if adjusted_intermediate > 100:
        scaled = adjusted_intermediate * 0.8
    else:
        scaled = adjusted_intermediate
    
    # Final transformation
    return scaled + 5

final_score = calculate_final_score(processed_data)
print(f"Result: {final_score}")