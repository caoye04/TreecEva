def analyze_pattern(sequence):
    # Auxiliary analysis with side computations
    length = len(sequence)
    avg_val = sum(sequence) / length if length else 0
    squared_devs = [(x - avg_val) ** 2 for x in sequence]
    variance = sum(squared_devs) / length if length else 0

    # Real logic: count peaks (local maxima)
    peak_count = 0
    for i in range(1, length - 1):
        if sequence[i] > sequence[i-1] and sequence[i] > sequence[i+1]:
            peak_count += 1

    # Distractor: unused smoothing
    smoothed = [sequence[0]]
    for i in range(1, length - 1):
        smoothed.append((sequence[i-1] + sequence[i] + sequence[i+1]) / 3)
    smoothed.append(sequence[-1])

    return peak_count


def process_segments(data, limit):
    total = 0
    segment_stats = []

    # Split data into chunks using enumerate and zip
    indices = [i for i, x in enumerate(data) if x >= limit]
    splits = [0] + indices + [len(data)]

    for start, end in zip(splits, splits[1:]):
        segment = data[start:end]
        if len(segment) == 0:
            continue

        # Use lambda to compute dynamic weight
        weight_func = lambda s: 1.5 if max(s) - min(s) > 5 else 1.0
        raw_score = sum(1 for x in segment if x > limit / 2)
        weighted_score = raw_score * weight_func(segment)

        # Track stats (some not used later)
        segment_stats.append({
            'size': len(segment),
            'score': raw_score,
            'weighted': weighted_score,
            'range': max(segment) - min(segment)
        })

        total += int(weighted_score)  # only integer part contributes

    # Additional irrelevant aggregation
    if segment_stats:
        high_impact = list(filter(lambda s: s['weighted'] > 3, segment_stats))
        avg_size = sum(s['size'] for s in high_impact) / len(high_impact) if high_impact else 0
        size_variance = sum((s['size'] - avg_size) ** 2 for s in high_impact)

    return total

# Main execution
readings = [3, 7, 4, 8, 2, 9, 1, 5, 6, 7, 4, 3, 8]
threshold = 6

# Preliminary pattern analysis (not directly affecting final result)
count_peaks = analyze_pattern(readings)
baseline_shift = sum(x for x in readings if x % 2 == 0)

# Key computation
final_count = process_segments(readings, threshold)

print(f"Result: {final_count}")