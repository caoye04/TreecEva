from collections import Counter

# Simulate signal processing with noise filtering and pattern detection
def analyze_signal(data, limit):
    frequencies = Counter(data)
    top_values = sorted(frequencies.items(), key=lambda x: -x[1])[:limit]
    signal_peaks = [k for k, v in top_values if k % 3 == 1]
    
    # Irrelevant computation: analyzing even/odd distribution (not used later)
    even_count = sum(1 for x in data if x % 2 == 0)
    odd_count = len(data) - even_count
    balance_ratio = even_count / odd_count if odd_count != 0 else float('inf')

    segments = []
    for i in range(0, len(data), 5):
        chunk = data[i:i+5]
        if len(chunk) == 5:
            avg = sum(chunk) / len(chunk)
            segments.append(avg)
    
    # Misleading transformation
    transformed = [x * 1.5 for x in segments if x > 20]
    dropoff = len(segments) - len(transformed)  # Unused metric

    return segments

# Signal post-processing with conditional aggregation
def evaluate_coherence(chunks):
    coherence_map = {}
    total_power = 0
    
    for idx, val in enumerate(chunks):
        if val > 15:
            adjusted = val * (idx + 1) ** 0.5
            coherence_map[idx] = round(adjusted, 3)
            total_power += adjusted

    # Dummy tracking of index flow
    index_trace = [k for k in coherence_map.keys() if k % 2 == 0]
    trace_sum = sum(index_trace)  # Not used

    return total_power

# Main pipeline: segment processing with threshold logic
def process_segments(chunks, thresh):
    filtered = [c for c in chunks if c > thresh]
    boosted = list(map(lambda x: x * 1.2, filtered))
    
    # Red herring calculation
    baseline_avg = sum(chunks) / len(chunks) if chunks else 0
    deviation_sq = sum((x - baseline_avg) ** 2 for x in chunks)
    stability_score = deviation_sq / len(chunks)  # Computed but unused

    aggregate = sum(boosted) - len(boosted) * 0.1
    return int(aggregate)

# Simulated sensor input
raw_data = [22, 18, 23, 19, 24, 21, 17, 25, 20, 22, 23, 19, 24, 18, 21, 20, 22, 19, 23, 25]

# Extract overlapping windows (slicing with step)
data_slices = [raw_data[i:i+6] for i in range(0, len(raw_data)-5, 3)]
flattened_view = [item for sublist in data_slices for item in sublist]

# Apply primary analysis
signal_chunks = analyze_signal(flattened_view, limit=8)
coherence_energy = evaluate_coherence(signal_chunks)

threshold = 19.5
final_score = process_segments(signal_chunks, threshold)

print(f"Result: {final_score}")