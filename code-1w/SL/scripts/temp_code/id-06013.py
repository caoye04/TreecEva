import itertools

def analyze_pattern(sequence):
    even_count = 0
    odd_count = 0
    temp_sum = 0
    for i, val in enumerate(sequence):
        if i % 2 == 0:
            even_count += 1
            temp_sum += val * 2
        else:
            odd_count += 1
            temp_sum -= val
    return even_count, odd_count

def filter_noisy_data(data, limit):
    filtered = [x for x in data if x > limit // 2]
    noise_floor = sum(filtered) / len(filtered) if filtered else 0
    cleaned = [x for x in filtered if x <= noise_floor * 1.5]
    return cleaned

def compute_weighted_score(items):
    score = 0
    for a, b in zip(items[:-1], items[1:]):
        score += (a + b) * 0.5
    return int(score)

def process_segments(segments, thresh):
    valid_segments = []
    debug_logs = []
    total_energy = 0
    peak_magnitude = 0
    
    for idx, seg in enumerate(segments):
        segment_sum = sum(seg)
        segment_len = len(seg)
        normalized = segment_sum / segment_len if segment_len else 0
        
        # Irrelevant tracking (distractor)
        if segment_sum > 50:
            debug_logs.append(f"High energy in segment {idx}")
        
        total_energy += segment_sum
        if segment_sum > peak_magnitude:
            peak_magnitude = segment_sum
        
        if normalized >= thresh:
            valid_segments.append(seg)
    
    # Distractor computation: unused entropy-like measure
    if total_energy > 0:
        entropy_proxy = 0
        for s in segments:
            p = sum(s) / total_energy if total_energy else 0
            if p > 0:
                entropy_proxy -= p * __import__('math').log(p)
    
    # Real logic continues
    candidate_pool = list(itertools.chain.from_iterable(valid_segments))
    
    # More distraction: sorting with no impact
    sorted_pool = sorted(candidate_pool, reverse=True)
    trimmed = sorted_pool[1:-1]  # Remove extremes (semi-relevant but not critical)
    
    base_score = compute_weighted_score(trimmed)
    
    # Final decision logic
    adjustment = 1
    if len(valid_segments) > 2 and peak_magnitude < 80:
        adjustment = 2
    
    final_value = base_score * adjustment
    
    # Critical assignment point
    final_output = final_value
    
    # Additional red herring
    if final_output % 2 == 0:
        dummy_flag = True
        shadow_copy = [x * 0.9 for x in trimmed]

    return final_output

# Main execution
if __name__ == "__main__":
    raw_input = [3, 8, 5, 12, 7, 4, 9, 6]
    
    # Generate segment data (real signal)
    grouped = list(itertools.zip_longest(*[iter(raw_input)] * 2, fillvalue=0))
    segment_data = [list(filter(lambda x: x != 0, group)) for group in grouped]
    
    # Noise injection (distraction)
    fake_peaks = [max(group) * 1.1 for group in grouped if sum(group) > 10]
    auxiliary_metric = sum(fake_peaks) / len(fake_peaks) if fake_peaks else 0
    
    threshold = 5.0
    
    # Key statement
    final_output = process_segments(segment_data, threshold)
    
    print(f"Result: {final_output}")