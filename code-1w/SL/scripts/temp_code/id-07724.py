def analyze_pattern(sequence):
    count = 0
    for i in range(1, len(sequence)):
        if sequence[i] > sequence[i-1]:
            count += 1
    return count

# Simulated sensor data stream
data_stream = [3, 7, 2, 8, 5, 9, 1, 6, 4, 10]

# Irrelevant transformation (distractor)
transformed = [x * 2 + 1 for x in data_stream if x % 2 == 0]

# Extract meaningful segment using slicing
data_slice = data_stream[2:8]  # Focus on window [2,8,5,9,1,6]

# Threshold logic with set operations
deviations = {x for x in data_slice if x > 5}
thresh_limit = 7
threshold_set = deviations.intersection({x for x in data_slice if x >= thresh_limit})

# Secondary analysis (semi-relevant)
peak_count = sum(1 for x in data_slice if x == max(data_slice))
baseline_offset = sum(data_slice) / len(data_slice)

# Dummy state tracking (dead code path)
counters = {}
for item in data_slice:
    if item not in counters:
        counters[item] = 0
    counters[item] += 1

# Misleading accumulation
phantom_total = 0
for val in transformed:
    phantom_total += val * 0.5

# Core calculation function
def calculate_final_score(segment, thresholds):
    raw_sum = sum(segment)
    penalty = 0
    
    # Nested conditional logic with interdependent steps
    for val in segment:
        if val in thresholds:
            if val % 2 == 1:  # odd high values
                penalty += 3
            else:
                penalty += 1
    
    # Additional adjustment based on pattern trend
    trend_upward = analyze_pattern(list(thresholds))
    adjustment = len(thresholds) - penalty if trend_upward > 0 else -penalty
    
    intermediate = raw_sum + adjustment
    
    # Final nonlinear scaling (key step)
    final = abs(intermediate) // (len(thresholds) or 1)
    
    return final

# Execute main computation
temp_var = [x for x in data_slice if x in threshold_set]
final_score = calculate_final_score(data_slice, threshold_set)
print(f"Result: {final_score}")