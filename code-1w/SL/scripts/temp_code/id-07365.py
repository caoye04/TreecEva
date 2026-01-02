from itertools import combinations

def analyze_pattern(sequence):
    count = 0
    trend = []
    temp_sum = 0  # distractor: used in intermediate calc but not final

    for i, val in enumerate(sequence):
        if i > 0 and sequence[i] > sequence[i-1]:
            trend.append(1)
        elif i > 0 and sequence[i] < sequence[i-1]:
            trend.append(-1)
        else:
            trend.append(0)

    # Irrelevant pattern tracking (distractor)
    flat_streaks = 0
    for t in trend:
        if t == 0:
            flat_streaks += 1

    # Real logic: count ascending pairs
    asc_pairs = 0
    for i in range(len(trend)):
        if trend[i] == 1:
            asc_pairs += 1

    # Dummy transformation
    dummy_weight = len([x for x in sequence if x % 2 == 0])  # counts evens, unused later

    return asc_pairs

def compute_aggregate(data_stream):
    base_metric = 0
    offset = 0
    snapshot = []

    for chunk in data_stream:
        if len(chunk) < 3:
            continue
        
        # Process meaningful segment
        processed = [x * 2 + 1 for x in chunk]  # transformation
        filtered = [x for x in processed if x > 10]
        
        # Distractor: collect stats not used
        avg_temp = sum(processed) / len(processed) if processed else 0
        peak = max(filtered) if filtered else 0
        
        # Real contribution
        direction_key = analyze_pattern(chunk)
        base_metric += direction_key * 3

        # Dead code path (only triggers on impossible condition)
        if len(chunk) > 100:
            offset -= 999  # never reached

        snapshot.extend(filtered)

    # Secondary analysis with distractor variables
    total_snapshot = sum(snapshot)
    length_penalty = len(snapshot) if total_snapshot < 50 else 0  # rarely active

    # Final computation
    final_score = base_metric + (total_snapshot // 10) - length_penalty
    return final_score

# Main execution
stream_input = [
    [4, 5, 6],
    [2, 1, 3, 7],
    [8, 8, 8],
    [1, 4]
]

result_value = compute_aggregate(stream_input)
final_score = result_value
print(f"Target result: {final_score}")