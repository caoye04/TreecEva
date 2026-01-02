from itertools import combinations

def analyze_transmission(signal_sequence, threshold=3):
    valid_segments = []
    temp_buffer = []
    noise_count = 0
    cumulative_energy = 0

    for i, val in enumerate(signal_sequence):
        if val < 0:
            noise_count += 1
            continue
        
        temp_buffer.append(val)
        cumulative_energy += val ** 0.5

        if len(temp_buffer) >= threshold:
            segment_avg = sum(temp_buffer) / len(temp_buffer)
            if segment_avg > threshold * 1.5:
                valid_segments.append(segment_avg)
            temp_buffer = temp_buffer[1:]
    
    return valid_segments, noise_count, cumulative_energy


def extract_peaks(data_list):
    peaks = []
    for i in range(1, len(data_list) - 1):
        if data_list[i] > data_list[i-1] and data_list[i] > data_list[i+1]:
            peaks.append(data_list[i])
    return peaks if peaks else [0]


def calculate_final_score(segments):
    base_score = 0
    adjustment_factor = 0.85
    peak_contributions = 0

    for seg in segments:
        if seg > 5:
            base_score += int(seg * 2)
        else:
            base_score += int(seg)

    # Simulate additional analysis (distractor logic)
    all_pairs = list(combinations(segments, 2))
    pair_sum = 0
    for a, b in all_pairs:
        pair_sum += abs(a - b)  # Irrelevant computation
    
    # Another distractor: character counting in debug mode
    debug_tag = "ANALYSIS_COMPLETE"
    char_count = sum(1 for c in debug_tag if c == 'A')  # Unused variable

    # Real contribution starts here
    processed_segments = [s for s in segments if s > 4]
    if len(processed_segments) >= 2:
        sorted_segments = sorted(processed_segments, reverse=True)
        top_two_product = sorted_segments[0] * sorted_segments[1]
        peak_contributions = int(top_two_product * 0.1)

    final_score = base_score + peak_contributions

    # Dead code path (never executed due to fixed input)
    if False and len(segments) > 100:
        fallback = sum(segments) // len(segments)
        final_score = max(final_score, fallback)

    return final_score

# Main execution
raw_signal = [2, 7, -1, 5, 6, -2, 8, 3, 9, 1]
processed_data, _, _ = analyze_transmission(raw_signal, threshold=2)
extended_analysis = extract_peaks([int(x) for x in processed_data])
final_score = calculate_final_score(processed_data)
print(f"Result: {final_score}")