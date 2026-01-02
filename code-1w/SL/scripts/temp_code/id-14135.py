from collections import defaultdict

# Simulate a sequence of events with repeated patterns
event_stream = [1, 3, 2, 1, 4, 3, 1, 2, 3, 1, 4, 4, 2]

# Count frequency of each event
def calculate_event_frequencies(stream):
    freq_map = defaultdict(int)
    for event in stream:
        freq_map[event] += 1
    return freq_map

frequency_map = calculate_event_frequencies(event_stream)

# Identify the highest occurrence count
peak_frequency = max(frequency_map.values())

# Secondary analysis: total unique events
unique_events = len(frequency_map)

# Irrelevant metric: sum of squared frequencies (distractor)
squared_total = sum(x**2 for x in frequency_map.values())

# Output target result
print(f"Result: {peak_frequency}")