def process_leaderboard(entries):
    # Normalize usernames and extract scores
    normalized_entries = []
    temp_scores = []
    for entry in entries:
        name, score = entry.split(':')
        clean_name = name.strip().lower().replace('_', '').title()
        parsed_score = int(score.strip())
        normalized_entries.append((clean_name, parsed_score))
        temp_scores.append(parsed_score)

    # Sort by score descending, then by name ascending
    sorted_entries = sorted(normalized_entries, key=lambda x: (-x[1], x[0]))

    # Assign raw ranks (with ties receiving same rank, next rank skips accordingly)
    current_rank = 1
    rank_dict = {}
    prev_score = None
    rank_list = []
    
    for i, (name, score) in enumerate(sorted_entries):
        if score != prev_score:
            current_rank = i + 1
        rank_dict[name] = current_rank
        rank_list.append(current_rank)
        prev_score = score

    # Compute statistical measures (distractor computations)
    avg_score = sum(temp_scores) / len(temp_scores)
    variance = sum((s - avg_score) ** 2 for s in temp_scores) / len(temp_scores)
    std_dev = variance ** 0.5
    adjusted_avg = round(avg_score + std_dev, 2)

    # Simulate bonus eligibility based on name length (semi-relevant)
    bonus_eligibility = [len(name) % 2 == 0 for name, _ in sorted_entries]
    bonus_factor = sum(bonus_eligibility) * 0.1

    # Final scoring adjustment function
    def calculate_adjusted_rank(ranks, bonus):
        base_penalty = sum(ranks) * 0.05
        # Apply non-linear transformation to dampen high ranks
        transformed = [max(1, r ** 0.8 - bonus) for r in ranks]
        penalty_offset = base_penalty * bonus if bonus > 0.5 else 0
        return int(sum(transformed) - penalty_offset + 0.5)  # Round to nearest int

    final_score = calculate_adjusted_rank(rank_list, bonus_factor)
    
    # Dead code path - never executed
    if False:
        debug_info = {"ranks": rank_list, "bonus": bonus_factor}
        log_entry = f"Debug: {debug_info}".upper()

    # Irrelevant string aggregation
    all_names = ''.join([name for name, _ in sorted_entries])
    char_frequency = {c: all_names.count(c) for c in set(all_names)}
    rare_chars = [c for c, cnt in char_frequency.items() if cnt == 1]

    # Output the target result
    print(f"Result: {final_score}")

# Input data
leaderboard_data = [
    "alice_123:85", "bob_55:92", "charlie_:78", "diana__7:92",
    "eve_00:76", "frank_2:85", "grace_8:92", "henry_:78"
]

process_leaderboard(leaderboard_data)