from collections import Counter

def analyze_sequence_trends(sequence):
    trend_shifts = 0
    prev_difference = sequence[1] - sequence[0]
    
    for i in range(2, len(sequence)):
        current_difference = sequence[i] - sequence[i-1]
        if (prev_difference > 0 and current_difference < 0) or (prev_difference < 0 and current_difference > 0):
            trend_shifts += 1
        prev_difference = current_difference

    frequency_counter = Counter(sequence)
    peak_frequency = max(frequency_counter.values())
    
    total_amplitude = max(sequence) - min(sequence)
    avg_value = sum(sequence) / len(sequence)
    
    return peak_frequency

sequence_data = [12, 15, 12, 18, 12, 21, 15, 15, 18, 12, 24, 21]
result = analyze_sequence_trends(sequence_data)
print(f"Result: {result}")