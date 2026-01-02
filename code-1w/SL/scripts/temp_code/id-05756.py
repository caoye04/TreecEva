def preprocess_observations(raw):
    # Irrelevant preprocessing function (dead end)
    return [x * 0.95 for x in raw if x > 10]


def validate_entry(record):
    # Misleading validation with side effects that aren't used
    if sum(record) % 2 == 0:
        return False
    checksum = 0
    for i, val in enumerate(record):
        checksum += val * (i + 1)
    return checksum < 100


def transform_sequence(seq):
    # Distractor transformation (never called in main logic)
    shifted = [seq[i] ^ seq[(i+1)%len(seq)] for i in range(len(seq))]
    return [x for x in shifted if x & 1]


def accumulate_metrics(values, mode='fast'):
    # Red herring accumulation with unused branches
    temp_result = 0
    history = []
    for idx, v in enumerate(values):
        if mode == 'debug':
            history.append(v ** 2)
        elif mode == 'safe':
            temp_result += abs(v)
        else:
            temp_result += v * (idx + 1)  # Only this branch matters, but obfuscated
    return temp_result


def filter_anomalies(dataset):
    # Complex filtering logic that looks important but isn't used
    threshold = sum(sum(row) for row in dataset) / len(dataset)
    filtered = []
    for i, row in enumerate(dataset):
        if any(abs(x) > threshold for x in row):
            continue
        filtered.append([x for x in row if x % 2 != 0])
    return filtered


def compute_entropy(vector):
    # Unused mathematical distraction
    from math import log2
    total = sum(vector)
    if total == 0:
        return 0
    probs = [v / total for v in vector if v > 0]
    return -sum(p * log2(p) for p in probs)


def compute_final_score(data, weights):
    # Core logic buried among distractions
    base_scores = []
    for i, row in enumerate(data):
        weighted_sum = 0
        for j, val in enumerate(row):
            if j < len(weights):  # Handle mismatched lengths
                weighted_sum += val * weights[j]
        base_scores.append(weighted_sum)
    
    # Real computation path starts here
    adjusted = [x - 5 for x in base_scores]  # Normalize around baseline
    
    # Use enumerate and zip as required
    multipliers = [1, -1, 2]
    final_parts = []
    for idx, (val, mult) in enumerate(zip(adjusted, multipliers * 2)):
        if idx >= len(adjusted):
            break
        temp_val = val * mult
        if temp_val > 0:
            final_parts.append(temp_val)
        else:
            final_parts.append(temp_val * -0.5)  # Invert negative contributions partially
    
    # Critical aggregation
    aggregate = 0
    for k, part in enumerate(final_parts):
        if k % 2 == 0:
            aggregate += part
        else:
            aggregate -= part * 0.1
    
    # Final adjustment based on control flag
    control_flag = True
    offset = 0
    if control_flag:
        offset = len(data)  # Add number of rows as bonus
    
    final_score = int(aggregate + offset)  # Answer determined here
    
    # Dead code path (misleading)
    if final_score < 0:
        backup_weights = [w * 0.5 for w in weights]
        alt = compute_final_score(data, backup_weights)
        return alt + 100
    
    return final_score

# Main execution block
if __name__ == '__main__':
    # Input data (simulated sensor readings)
    raw_data = [
        [8, 12, 5],
        [6, 10, 7],
        [9, 11, 4]
    ]

    config_weights = [2, -1, 3]  # Influence per feature

    # Irrelevant intermediate steps (distractors)
    cleaned = preprocess_observations([item for row in raw_data for item in row])
    entropy_measure = compute_entropy([sum(row) for row in raw_data])
    anomalies_filtered = filter_anomalies(raw_data)

    # Key call that produces the answer
    final_score = compute_final_score(raw_data, config_weights)

    # Print result as required
    print(f"Target result: {final_score}")