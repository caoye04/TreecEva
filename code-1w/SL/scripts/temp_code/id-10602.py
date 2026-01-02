def analyze_sequence(data, threshold):
    count_valid = 0
    temp_sum = 0
    max_gap = 0
    prev = None
    
    for i, val in enumerate(data):
        if val > threshold:
            count_valid += 1
            temp_sum += val
            
            if prev is not None:
                gap = i - prev
                if gap > max_gap:
                    max_gap = gap
            prev = i
    
    average_valid = temp_sum / count_valid if count_valid > 0 else 0
    return count_valid, average_valid, max_gap


def adjust_weights(scores):
    adjusted = []
    total = sum(scores)
    for s in scores:
        weight = (s + 1) / (total + len(scores))
        adjusted.append(round(weight * 100, 2))
    # Dead code - never used
    normalization_factor = sum(adjusted) / 100.0
    return adjusted

def calculate_performance(entries, cutoff=50):
    # Irrelevant transformation
    processed_entries = [x * 1.1 for x in entries if x % 2 == 1]
    filtered = [x for x in entries if x >= cutoff]
    
    # Key analysis on filtered data
    count, avg, longest_gap = analyze_sequence(entries, cutoff)
    
    # Secondary metrics with distraction
    squared_total = sum([x**2 for x in filtered])
    penalty = 0
    for i in range(len(filtered)):
        if i > 0 and filtered[i] < filtered[i-1]:
            penalty += 1
    
    # Complex but partially irrelevant scoring
    base_score = avg * count
    adjustment = (longest_gap * 2) - penalty
    
    # Red herring: unused min/max calculations
    sorted_vals = sorted(filtered)
    mid_index = len(sorted_vals) // 2
    median_val = sorted_vals[mid_index] if sorted_vals else 0
    outlier_check = [x for x in filtered if x > 3*median_val]  # Unused
    
    # Core logic embedded within noise
    if adjustment > 0:
        final_score = base_score - adjustment
    else:
        final_score = base_score + abs(adjustment)
    
    # Additional distraction: zipping unrelated sequences
    indices = list(range(len(processed_entries)))
    zipped_data = list(zip(processed_entries, indices))
    size_zipped = len(zipped_data)
    
    # Print result as required
    print(f"Result: {final_score}")
    return final_score

# Main execution
input_data = [45, 60, 30, 70, 85, 20, 55, 90, 40, 65]
calculate_performance(input_data, cutoff=50)