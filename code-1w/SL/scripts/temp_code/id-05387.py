def evaluate_performance(ranks, log):
    base_score = 0
    bonus_multiplier = 1.0
    penalty_count = 0

    # Irrelevant logging setup (distractor)
    debug_mode = False
    log_entries = len(log)
    temp_trace = [x % 7 for x in log if x > 0]  # Unused computation

    # Actual scoring logic
    unique_ranks = set(ranks)  # Set operation: get distinct ranks
    sorted_ranks = sorted(unique_ranks, reverse=True)

    for i, rank in enumerate(sorted_ranks):
        if rank <= 0:
            continue
        base_score += rank * (i + 1)

        # Bonus condition
        if rank > 5 and i % 2 == 0:
            bonus_multiplier *= 1.25

        # Fake branch with dead code
        if debug_mode:
            print(f'Debug: Processing rank {rank}')  # Never executed

    # Simulate performance decay over time (modular arithmetic)
    decay_factor = (sum(log) % 9) + 1
    adjusted_score = base_score / decay_factor

    # Additional irrelevant sequence analysis (distractor)
    pattern_window = log[::2]  # Slicing: every other element
    spike_count = 0
    for j in range(1, len(pattern_window)):
        if pattern_window[j] > 2 * pattern_window[j - 1]:
            spike_count += 1  # Not used in final result

    # Final score with bonus
    final_score = int(adjusted_score * bonus_multiplier)

    return final_score


# Input data
rank_list = [3, 7, 7, 2, 9, -1, 4]
access_log = [8, 12, 3, 9, 6, 15, 1]

# Execution point of interest
final_score = evaluate_performance(rank_list, access_log)

print(f"Result: {final_score}")