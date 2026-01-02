from itertools import combinations

def analyze_patterns(sequence):
    count = 0
    total_pairs = 0
    temp_result = []
    
    # Irrelevant pattern tracking (distractor)
    for i in range(len(sequence)):
        for j in range(i + 1, len(sequence)):
            if sequence[i] + sequence[j] == 10:
                count += 1
            total_pairs += 1

    # Real logic begins: find triplets where sum is divisible by 3
    valid_triplets = []
    for triplet in combinations(sequence, 3):
        if sum(triplet) % 3 == 0:
            valid_triplets.append(triplet)
    
    # Misleading intermediate (not used later)
    avg_length = total_pairs / (len(sequence) + 1e-5)
    
    return valid_triplets

def process_metrics(raw_data):
    # Unrelated normalization (distractor)
    normalized = [x * 0.95 for x in raw_data]
    offset_values = [x - 1 for x in normalized]
    
    # Key transformation
    filtered = [x for x in raw_data if x > 5]
    
    # Extra loop with no impact
    cumulative = 0
    for val in offset_values:
        cumulative += val ** 2
    
    return filtered

def calculate_final_score(data_list):
    base_sum = sum(data_list)
    penalty = 0
    
    # State tracking with partial relevance
    state_log = {}
    for idx, val in enumerate(data_list):
        if val % 2 == 0:
            penalty += 1
        state_log[idx] = val * 2  # logged but not used
    
    # Red herring computation
    squared_total = sum([x**2 for x in data_list])
    
    # Core scoring logic
    multiplier = 3 if len(data_list) > 4 else 2
    bonus = len(data_list) * 2
    
    return base_sum * multiplier + bonus - penalty

# Main execution flow
raw_input = [3, 6, 7, 8, 9, 10]

# Step 1: Process metrics (filters to [6,7,8,9,10])
intermediate_data = process_metrics(raw_input)

# Step 2: Analyze patterns (returns valid triplets, not directly used)
detected = analyze_patterns(intermediate_data)

# Step 3: Extract key values for scoring
processed_data = []
for num in intermediate_data:
    if num in {7, 8, 9}:  # selective inclusion
        processed_data.append(num)
    else:
        processed_data.append(num // 2)

# Step 4: Final score calculation
temp_cache = {x: x*3 for x in processed_data}  # dead storage
final_score = calculate_final_score(processed_data)

print(f"Result: {final_score}")