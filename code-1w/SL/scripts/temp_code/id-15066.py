def calculate_final_score(ranks, flags):
    base_points = 0
    multiplier = 1
    penalty_adjustment = 0
    temp_sum = 0  # distractor variable
    debug_log = []  # dead code path, never used

    rank_map = {name: idx + 1 for idx, name in enumerate(ranks)}
    
    # Irrelevant computation on flag combinations
    flag_combinations = set()
    for i in range(len(flags)):
        for j in range(i + 1, len(flags)):
            flag_combinations.add(flags[i] ^ flags[j])  # bitwise XOR, not directly used
    
    unused_count = len(flag_combinations) * 2  # misleading variable

    # Actual scoring logic with conditional branches
    for idx, name in enumerate(ranks):
        position_bonus = 10 - rank_map[name]
        if position_bonus > 3:
            base_points += 5
            if idx % 2 == 0:
                multiplier += 1
        else:
            penalty_adjustment -= 2

    # Simulate conditional state tracking
    state_tracker = {}
    for i, flag in enumerate(flags):
        state_tracker[f"step_{i}"] = flag & 1  # bitwise AND, store parity
    
    fluctuation_factor = 0
    for k, v in state_tracker.items():
        fluctuation_factor += v
    
    # Distractor loop: processes zipped data but doesn't affect final score
    aux_data = [3, 1, 4, 1, 5]
    for r, a in zip(ranks, aux_data):
        temp_sum += len(r) * a  # irrelevant accumulation

    # Final score depends only on base_points, multiplier, and penalty_adjustment
    final_score = (base_points + penalty_adjustment) * multiplier
    
    return final_score

# Main execution
rank_data = ['Alice', 'Bob', 'Charlie', 'Diana']
bonus_flags = [1, 0, 1, 1, 0]

final_score = calculate_final_score(rank_data, bonus_flags)
print(f"Result: {final_score}")