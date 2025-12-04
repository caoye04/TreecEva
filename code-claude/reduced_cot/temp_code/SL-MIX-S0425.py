import itertools

def normalize_values(data, factor=2.5):
    # Misleading normalization that's not used for final result
    return [x/factor for x in data]

def apply_filter(values, threshold=5):
    # This function is a distraction - not used for final computation
    return [v for v in values if abs(v) > threshold]

def compute_entropy(signal):
    # Another misleading function - calculates entropy but isn't used
    from math import log2
    total = sum(signal)
    return -sum((x/total) * log2(x/total) if x > 0 else 0 for x in signal)

def signal_processing(data):
    # This is the key function that determines our answer
    if len(data) == 0:
        return -1  # Dead code path - data is never empty
    
    # Misleading transformation that isn't used
    transformed = list(map(lambda x: x**2 - 3*x + 2, data))
    
    # Extract every third element - this is important
    sampled = data[::3]
    
    # Misleading calculation
    noise_factor = sum(data) / len(data) if data else 0
    
    # Create pairs with shifted version of sampled data - relevant
    pairs = list(zip(sampled, sampled[1:] + sampled[:1]))
    
    # Misleading operation with the pairs
    pair_products = [a*b for a, b in pairs]
    
    # This is the actual calculation we care about
    result = 0
    for idx, (a, b) in enumerate(pairs):
        if idx % 2 == 0:  # Only use even indices
            result += (a - b) ** 2
        else:  # This branch is a distraction
            result -= a * b * 0.01
    
    # More distraction - unused variables
    average = sum(sampled) / len(sampled)
    deviation = sum((x - average)**2 for x in sampled) / len(sampled)
    
    # Conditional expression that's important
    result = result * 2 if result > 50 else result / 2
    
    return int(result)

# Main processing starts here
raw_data = [12, 9, 15, 18, 7, 13, 16, 10, 14, 8, 11, 17]

# Distraction - create permutations we don't use
permutations = list(itertools.permutations(raw_data[:3]))

# Distraction - sorting that isn't used for final result
sorted_data = sorted(raw_data, reverse=True)

# This is used but is a distraction - we don't need normalized values
normalized = normalize_values(raw_data)

# More distraction - filtering we don't use
high_values = apply_filter(raw_data, 10)

# This is the data we actually use
filtered_data = raw_data[2:10]  # Slice the data - this matters

# Distraction - calculate statistics we don't use
mean_value = sum(filtered_data) / len(filtered_data)
median_value = sorted(filtered_data)[len(filtered_data)//2]

# More distractions - bit operations that aren't used
bit_result = 0
for val in filtered_data:
    bit_result = (bit_result << 2) | (val & 0x3)

# This is the important call that gives us our answer
target_signal = signal_processing(filtered_data)

# Final distractions
if target_signal > 100:
    target_signal = target_signal // 2  # Dead code - target_signal is not > 100
elif target_signal < 0:
    target_signal = abs(target_signal)  # Dead code - target_signal is not < 0

print(f"Result: {target_signal}")