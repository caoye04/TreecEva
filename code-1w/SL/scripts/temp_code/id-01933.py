from collections import Counter

def analyze_sequence_trend(sequence):
    count_map = Counter(sequence)
    frequencies = sorted(count_map.values(), reverse=True)
    peak_frequency = frequencies[0] if frequencies else 0
    trend_score = 0
    
    for i in range(len(frequencies)):
        if frequencies[i] < peak_frequency * 0.5:
            break
        trend_score += frequencies[i]
    
    adjustment = len(sequence) // (peak_frequency + 1)
    result = trend_score - adjustment
    
    # Irrelevant tracking variable (minor distraction)
    update_log = []
    update_log.append(f"Final result computed: {result}")
    
    print(f"Result: {peak_frequency}")

# Input data
data_stream = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
analyze_sequence_trend(data_stream)