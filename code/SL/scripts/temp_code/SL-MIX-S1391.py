from functools import reduce

def compute_modular_sum(signal_block):
    return sum(signal_block) % 17

def normalize_signal(value):
    return round(value / 3.0, 2)

signal_data = [
    [23, 45, 67],
    [12, 89, 33],
    [55, 22, 78],
    [19, 42, 61]
]

processed_signals = set()
anomaly_score = 0.0

for block_idx in range(len(signal_data)):
    if block_idx > 2:
        break
    signal_block = signal_data[block_idx]
    mod_sum = compute_modular_sum(signal_block)
    if mod_sum in processed_signals:
        anomaly_score += normalize_signal(mod_sum * 2)
        continue
    processed_signals.add(mod_sum)
    for val in signal_block:
        transformed = (val * 3) % 11
        if transformed == 0:
            anomaly_score += normalize_signal(val)
            break
    
final_mod_sum = reduce(lambda x, y: x + y, map(compute_modular_sum, signal_data[:3]))
anomaly_score += normalize_signal(final_mod_sum)

print(f"Result: {anomaly_score}")