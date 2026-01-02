from collections import Counter

def analyze_sequence_trends(seq):
    count = Counter(seq)
    peak_frequency = 0
    current_streak_value = None
    streak_length = 0
    temp_buffer = []  # Irrelevant storage (distractor)

    for i, val in enumerate(seq):
        if i == 0:
            current_streak_value = val

        if val == current_streak_value:
            streak_length += 1
        else:
            if streak_length > peak_frequency and current_streak_value > 0:
                peak_frequency = streak_length
            current_streak_value = val
            streak_length = 1

        # Early termination condition based on pattern
        if streak_length >= 5:
            break  # Critical execution point

        temp_buffer.append(i * 2)  # Distractor operation

    return peak_frequency

sequence = [3, 3, 3, 3, 3, 2, 2, 1]
result = analyze_sequence_trends(sequence)
print(f"Result: {result}")