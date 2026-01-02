def analyze_performance(records):
    # Irrelevant preprocessing: normalize names (distractor)
    normalized_names = [name.strip().title() for name in records.keys()]
    unused_stats = {name: {'count': 0, 'total': 0} for name in normalized_names}

    # Real data transformation: extract scores and timestamps
    raw_entries = []
    for key, values in records.items():
        for entry in values:
            if 'score' in entry and 'ts' in entry:
                raw_entries.append((entry['score'], entry['ts']))

    # Sort by timestamp (ascending) - relevant
    raw_entries.sort(key=lambda x: x[1])

    # Compute time-weighted score decay (relevant logic)
    current_time = 1678886400
    weighted_scores = []
    for score, ts in raw_entries:
        time_diff_hours = (current_time - ts) // 3600
        decay_factor = max(0.5, 1 - (time_diff_hours * 0.001))
        weighted_scores.append(score * decay_factor)

    # Irrelevant: frequency analysis of score digits (red herring)
    digit_frequency = {i: 0 for i in range(10)}
    for score in [int(ws) for ws in weighted_scores]:
        for digit in str(abs(score)):
            digit_frequency[int(digit)] += 1

    # Destructuring with enumerate and zip (required feature) - partially relevant
    ranked = sorted(weighted_scores, reverse=True)
    positions = list(enumerate(ranked, start=1))
    zipped_pairs = list(zip(positions, reversed(positions)))

    # Decoy function call (dead path)
    def compute_legacy_rank():
        return sum([p * v for p, v in positions]) // len(positions)

    # Real ranking adjustment using top 5 and parity check
    top_5_avg = sum(ranked[:5]) / 5 if len(ranked) >= 5 else sum(ranked) / len(ranked) if ranked else 0
    parity_offset = 0
    for i, (pos, val) in enumerate(positions):
        if pos % 2 == 0 and val > top_5_avg:
            parity_offset += 1

    # Bit manipulation layer (simple XOR for obfuscation)
    magic_seed = 0x1F
    adjusted_base = int(top_5_avg * 100)
    encoded_value = adjusted_base ^ magic_seed
    decoded_value = encoded_value ^ magic_seed  # Restore original with XOR (subtle but valid)

    # Conditional expression chain with slicing (required features)
    history_window = weighted_scores[-10:] if len(weighted_scores) > 10 else weighted_scores[:]
    volatility = sum([abs(a - b) for a, b in zip(history_window, history_window[1:])])
    stability_bonus = 10 if volatility < 50 else 5 if volatility < 100 else 0

    # Final calculation - depends on multiple prior steps
    final_score = decoded_value + stability_bonus + parity_offset

    # Print result as required
    print(f"Result: {final_score}")
    return final_score


def calculate_adjusted_rank(data):
    return analyze_performance(data)

# Input dataset (fixed seed, deterministic)
data_input = {
    "alpha_team": [
        {"score": 85, "ts": 1678872000},
        {"score": 90, "ts": 1678875600},
        {"score": 87, "ts": 1678879200}
    ],
    "beta_squad": [
        {"score": 92, "ts": 1678868400},
        {"score": 88, "ts": 1678872000},
        {"score": 95, "ts": 1678882800}
    ],
    "gamma_unit": [
        {"score": 84, "ts": 1678864800},
        {"score": 90, "ts": 1678879200},
        {"score": 91, "ts": 1678884600}
    ]
}

# Execute
final_score = calculate_adjusted_rank(data_input)