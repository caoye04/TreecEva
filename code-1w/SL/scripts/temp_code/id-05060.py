from itertools import combinations

def analyze_segments(data, limit):
    segments = []
    temp_sum = 0
    segment_count = 0
    
    for val in data:
        temp_sum += val
        if temp_sum >= limit:
            segments.append(temp_sum)
            temp_sum = 0
            segment_count += 1
    
    # Irrelevant tracking (distractor)
    excess_contributions = [x for x in data if x > limit // 4]
    average_excess = sum(excess_contributions) / len(excess_contributions) if excess_contributions else 0
    
    return segments

def compute_pairwise_gaps(values):
    if len(values) < 2:
        return [0]
    gaps = []
    for i in range(1, len(values)):
        gap = abs(values[i] - values[i-1])
        gaps.append(gap)
    return gaps

def process_distribution(inputs, cutoff):
    # Step 1: Segment input based on threshold
    grouped = analyze_segments(inputs, cutoff)
    
    # Step 2: Compute derived stats (some irrelevant)
    squared_totals = [x**2 for x in grouped]
    total_energy = sum(grouped)
    
    # Step 3: Generate combinatorial pairs (distractor computation)
    combo_power = 0
    if len(grouped) >= 2:
        for pair in combinations(grouped, 2):
            combo_power += pair[0] * pair[1]
    
    # Step 4: Filter significant segments
    strong_segments = [x for x in grouped if x > cutoff * 1.5]
    
    # Step 5: Accumulate final tally based on logic chain
    accumulator = 0
    for s in strong_segments:
        if s % 2 == 0:
            accumulator += s // 2
        else:
            accumulator += s * 2
    
    # Step 6: Add unrelated offset (but defined, not random)
    debug_offset = len(squared_totals) - len(strong_segments)
    final_value = accumulator + debug_offset
    
    return final_value

# Main execution
flow_data = [12, 7, 9, 14, 6, 18, 3, 11, 8]
threshold = 20
baseline_check = {x for x in flow_data if x > 10}
count_high_flow = len(baseline_check)

# Secondary distractor: unused grouping
pair_gaps = compute_pairwise_gaps(flow_data)
reference_mean = sum(flow_data) / len(flow_data)

final_tally = process_distribution(flow_data, threshold)
print(f"Target result: {final_tally}")