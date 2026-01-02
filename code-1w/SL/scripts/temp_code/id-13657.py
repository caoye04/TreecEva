def calculate_entropy(freqs):
    from math import log2
    total = sum(freqs)
    probabilities = [f / total for f in freqs if f > 0]
    entropy = -sum(p * log2(p) for p in probabilities)
    return round(entropy, 3)

# System event frequencies over a monitoring period
event_logs = "ERROR WARN INFO ERROR DEBUG WARN ERROR INFO WARN INFO WARN ERROR"
event_counts = {}
for event in event_logs.split():
    event_counts[event] = event_counts.get(event, 0) + 1

frequency_list = list(event_counts.values())

total_entropy = calculate_entropy(frequency_list)
print(f"Result: {total_entropy}")