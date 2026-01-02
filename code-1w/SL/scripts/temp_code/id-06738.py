from collections import Counter

# System load simulation across nodes
node_signals = [1, 0, 1, 1, 0, 1, 1, 1, 0, 0]
signal_count = Counter(node_signals)

dominant_signal = 1 if signal_count[1] > signal_count[0] else 0

# Calculate partial loads based on signal dominance
partial_loads = []
for i in range(len(node_signals)):
    if node_signals[i] == dominant_signal:
        partial_loads.append(i * 1.5)
    else:
        partial_loads.append(i * 0.5)

# Key statement
total_load = sum(partial_loads)

# Irrelevant auxiliary variable (minimal distraction)
avg_load = total_load / len(partial_loads) if partial_loads else 0

print(f"Result: {total_load}")