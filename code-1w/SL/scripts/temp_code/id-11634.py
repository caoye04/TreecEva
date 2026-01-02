from collections import Counter

def analyze_sequence_pattern(sequence):
    # Convert sequence to list of differences between consecutive elements
    diffs = [sequence[i+1] - sequence[i] for i in range(len(sequence) - 1)]
    
    # Count frequency of each difference
    frequency_counter = Counter(diffs)
    
    # Identify the most frequent difference (mode)
    peak_frequency = max(frequency_counter.values())
    
    # Irrelevant: track how many differences are positive (minor distraction)
    positive_trend_count = sum(1 for d in diffs if d > 0)
    
    return peak_frequency

# Input sequence representing time-series data points
input_sequence = [10, 15, 20, 25, 20, 15, 10, 15, 20, 25]

result = analyze_sequence_pattern(input_sequence)
print(f"Result: {result}")