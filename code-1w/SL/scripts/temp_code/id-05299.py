def calculate_final_score(records):
    # Irrelevant transformation
    temp_normalized = [round((x - min(records)) / (max(records) - min(records)) * 100) for x in records]
    
    # Actual computation path
    filtered = [x for x in records if x > 50]
    weighted = list(map(lambda x: x * 0.85, filtered))
    adjusted = [int(w + (i * 0.1)) for i, w in enumerate(weighted)]
    
    # Distractor: unused complex structure
    stats_summary = {
        'count': len(records),
        'peak': max(records),
        'baseline': sum(records) / len(records),
        'noise_floor': sum(1 for x in records if x < 30)
    }
    
    # Key logic with early termination condition
    running_total = 0
    for val in adjusted:
        if val > 95:
            break
        running_total += val
        if running_total > 200:
            running_total -= 50  # correction factor
    
    return int(running_total)

# Main data input
raw_data = [45, 67, 89, 92, 96, 78, 83, 71, 65, 58]

# Slice operation - relevant data extraction
data_slice = raw_data[1:8]  # Focus on middle segment

# Secondary distractor variables
shadow_copy = raw_data[::-1]
duplicate_filtered = [x for x in raw_data if x % 2 == 0]
placeholder_matrix = [[i + j for j in range(5)] for i in range(5)]

# Core assignment triggering the target evaluation
total_score = calculate_final_score(data_slice)

# Output result as required
print(f"Result: {total_score}")