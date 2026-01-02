def analyze_performance(records):
    base_multiplier = 1.5
    adjustment_factor = 0.9
    temp_results = []
    cumulative_shift = 0

    for i, (success, failure) in enumerate(records):
        if i % 2 == 0:
            adjusted_success = success * base_multiplier + 2
        else:
            adjusted_success = success * adjustment_factor

        noise_offset = (i ** 2) % 3  # Irrelevant computation
        filtered_failures = [f for f in [failure] if f > 0]  # Redundant filtering

        net_yield = adjusted_success - failure
        temp_results.append(net_yield)

        # Dead code path - never used later
        if len(temp_results) > 5:
            cumulative_shift += sum(temp_results[:2])

    return temp_results


def compute_baseline(n):
    # Distractor function: not directly contributing to final result
    seq = [1, 1]
    for i in range(2, n + 1):
        seq.append(seq[-1] + seq[-2])
    return seq[n]


def calculate_ranking(points_list, deductions):
    ranking = 0
    offset_tracker = {}

    for idx, (point, penalty) in enumerate(zip(points_list, deductions)):
        if point <= 0:
            continue

        scale = 2 if idx % 3 == 0 else 1.5
        normalized = (point * scale) - (penalty * 1.2)

        bonus = 5 if normalized > 10 else 0  # Conditional bonus
        contribution = normalized + bonus

        offset_tracker[idx] = contribution % 7  # Semi-relevant tracking

        ranking += int(contribution)

        # Extra logic that affects nothing
        shadow_buffer = [ranking // (i+1) for i in range(1, 4) if ranking > 20]

    return ranking

# Main execution
raw_data = [(8, 2), (12, 4), (5, 1), (15, 6), (7, 3)]
points = [x[0] for x in raw_data]
deductions = [x[1] for x in raw_data]

interim_values = analyze_performance(raw_data)
baseline_ref = compute_baseline(6)  # Computed but unused in final score

scaling_hint = sum([i for i in range(len(interim_values)) if interim_values[i] > 6])

# Key statement
final_score = calculate_ranking(points, deductions)

print(f"Result: {final_score}")