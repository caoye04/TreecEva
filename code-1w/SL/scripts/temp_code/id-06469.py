def analyze_metrics(data_list):
    temp_sum = sum(x ** 0.5 for x in data_list if x > 10)
    weighted = [x * 1.5 for x in data_list]
    return int(temp_sum // 1.5) + len(weighted)


def validate_sequence(seq):
    seen = set()
    for item in seq:
        if item in seen:
            return False
        seen.add(item)
    return True


def transform_key(key_str):
    shifted = ''.join(chr((ord(c) - 97 + 3) % 26 + 97) for c in key_str)
    return shifted.upper()[::-1]


def compute_entropy(values):
    from math import log2
    total = sum(values)
    probs = [v / total for v in values if v > 0]
    entropy = -sum(p * log2(p) for p in probs)
    return round(entropy, 4)


def filter_candidates(records):
    qualified = []
    for r in records:
        if r['experience'] >= 5 and r['rating'] > 4.0:
            qualified.append(r['id'])
    return qualified


def process_rankings(rankings, boost):
    base_points = 0
    penalty_adjustment = 0

    # Real logic path
    ranking_list = list(rankings.values())
    sorted_ranks = sorted(ranking_list)

    for i, rank in enumerate(sorted_ranks):
        if i % 2 == 0:
            base_points += rank * boost
        else:
            base_points += rank

    # Distractor: complex string manipulation with no effect
    metadata_tag = "config_x9z"
    tag_parts = metadata_tag.split('_')
    coded = transform_key(tag_parts[1])
    entropy_val = compute_entropy([len(coded), 128, 256])

    # Distractor: unused dictionary operations
    temp_cache = {f"key_{i}": pow(i, 3) for i in range(1, 20)}
    temp_cache.update({"aux": sum(len(str(v)) for v in temp_cache.values())})

    # Distractor: irrelevant filtering
    mock_records = [
        {'id': 101, 'experience': 6, 'rating': 4.5},
        {'id': 102, 'experience': 3, 'rating': 4.2},
        {'id': 103, 'experience': 7, 'rating': 3.8}
    ]
    filtered_ids = filter_candidates(mock_records)

    # Distractor: dead computation path
    debug_snapshot = {
        'checksum': sum(ord(c) for c in coded) ^ 12345,
        'size': len(temp_cache),
        'valid': validate_sequence(filtered_ids)
    }

    # Actual adjustment (non-obvious due to noise)
    if len(sorted_ranks) > 3:
        penalty_adjustment = -(sorted_ranks[0] // 4)

    intermediate = base_points + penalty_adjustment

    # Final transformation using string and dict side results (minimal but plausible)
    modifier = len(coded) % 5
    final_score = intermediate + modifier

    # Critical output
    return final_score

# Main execution
if __name__ == "__main__":
    # Input data
    rank_map = {
        'alpha': 12,
        'beta': 8,
        'gamma': 15,
        'delta': 6,
        'epsilon': 20
    }
    bonus_multiplier = 2

    # Irrelevant preprocessing
    raw_data = [16, 25, 36, 49, 64]
    signal_strength = analyze_metrics(raw_data)

    # Key statement
    final_score = process_rankings(rank_map, bonus_multiplier)

    print(f"Result: {final_score}")