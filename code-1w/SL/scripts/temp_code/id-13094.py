from itertools import combinations

def analyze_sequence(data):
    # Irrelevant analysis function (dead weight)
    count = 0
    for i, val in enumerate(data):
        if val > sum(data) / len(data):
            count += 1
    return count

def transform_entries(raw_list):
    # Transform with misleading intermediate steps
    temp_result = []
    offset = 7
    multiplier = 3
    for idx, item in enumerate(raw_list):
        transformed = (item * multiplier + offset) % 19
        temp_result.append(transformed)
    
    # Extra unused sorting
    sorted_temp = sorted(temp_result, reverse=True)
    
    # Actual useful transformation: square even-indexed elements
    for i in range(0, len(temp_result), 2):
        temp_result[i] **= 2
    
    return temp_result

def filter_and_pair(values):
    # Pair values but only keep relevant ones
    paired = list(combinations(values, 2))
    filtered_pairs = []
    for a, b in paired:
        diff = abs(a - b)
        if diff > 5:
            filtered_pairs.append((a, b))
    # Return only the second element of each pair's sum (semi-relevant)
    dummy_sum = sum([a + b for a, b in filtered_pairs])  # Distractor
    return [a + b for a, b in filtered_pairs]

def calculate_optimal_yield(inputs):
    base_yield = 0
    adjustments = []
    for val in inputs:
        if val % 4 == 0:
            base_yield += val // 4
        elif val % 3 == 0:
            adjustments.append(val % 7)
    net_adjustment = sum(adjustments) - len(adjustments)
    return base_yield + net_adjustment

# Main execution flow
raw_data = [4, 5, 6, 8, 9, 10, 12]

# Step 1: Analyze but don't use result (distractor call)
diagnostic_count = analyze_sequence(raw_data)

# Step 2: Transform entries with side effects
processed_data = transform_entries(raw_data)

# Step 3: Generate pair sums but only use part of logic
pair_sums = filter_and_pair(processed_data)

# Step 4: Key computation branch
intermediate_total = 0
for x in pair_sums:
    if x < 20:
        intermediate_total += x

# Step 5: Critical assignment point
final_yield = calculate_optimal_yield(processed_data)

# Output target result
print(f"Target result: {final_yield}")