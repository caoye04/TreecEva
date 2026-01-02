from collections import Counter

def analyze_sequence_trends(sequence):
    count_map = Counter(sequence)
    peak_frequency = 0
    current_trend = 0
    temp_offset = 0  # irrelevant distractor variable

    for val in sequence:
        if val > 0:
            current_trend += 1
        else:
            current_trend -= 1

        freq = count_map[val]
        if freq > peak_frequency:
            peak_frequency = freq
            if peak_frequency >= 4:
                break  # critical execution point

    return peak_frequency

# Input data with clear frequency distribution
input_sequence = [3, -1, 2, 2, 3, 3, 3, -1, 2, 2, 2, 3]
result = analyze_sequence_trends(input_sequence)
print(f"Target result: {result}")