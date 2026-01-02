from collections import defaultdict


def analyze_transmission(signal_str, threshold=3):
    # Count frequency of each character (signal segment)
    freq_map = defaultdict(int)
    for ch in signal_str:
        freq_map[ch] += 1

    # Extract segments that meet or exceed threshold
    valid_segments = [ch for ch, count in freq_map.items() if count >= threshold]
    return valid_segments


def calculate_entropy(items):
    # Dummy entropy-like calculation (not actually used in final logic)
    total = len(items)
    if total == 0:
        return 0.0
    entropy = 0.0
    for item in set(items):
        p = items.count(item) / total
        if p > 0:
            entropy -= p * (p ** 0.5)  # Not real entropy, just distraction
    return round(entropy, 4)


def process_segments(segs, weight_map):
    base_values = {}
    temp_result = []
    
    # Assign numeric values based on ASCII offset (relevant)
    for i, seg in enumerate(segs):
        base_values[seg] = ord(seg) - ord('a')
        temp_result.append(base_values[seg] * (i + 1))

    # Misleading transformation with zip and enumerate (semi-relevant)
    weighted_parts = []
    for idx, (seg, val) in enumerate(zip(segs, temp_result)):
        adjustment = weight_map.get(seg, 1)
        weighted_parts.append(val * adjustment + idx)

    # Final aggregation
    cumulative = 0
    for part in weighted_parts:
        if part % 2 == 0:
            cumulative += part // 2
        else:
            cumulative += part

    return cumulative


# Main execution block
if __name__ == "__main__":
    raw_signal = "abccdaacbbd"
    
    # Step 1: Analyze signal for frequent segments
    segments = analyze_transmission(raw_signal, threshold=3)
    
    # Step 2: Calculate useless entropy metric (distractor)
    _ = calculate_entropy(raw_signal)
    
    # Step 3: Prepare weights with some irrelevant keys
    influence_weights = {'a': 2, 'b': 1, 'x': 3, 'z': 5}  # 'x' and 'z' not in segments
    
    # Step 4: Process the valid segments into a score
    final_score = process_segments(segments, influence_weights)
    
    # Output result
    print(f"Result: {final_score}")