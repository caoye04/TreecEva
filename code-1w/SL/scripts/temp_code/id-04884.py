from itertools import groupby

# System signal processing simulation
def analyze_signal_patterns(signal):
    sorted_signal = sorted(signal, key=lambda x: (x[1], x[0]))
    grouped = groupby(sorted_signal, key=lambda x: x[1])
    
    total_cycles = 0
    noise_floor = 0.1  # Irrelevant parameter for baseline noise (distractor)
    sample_rate = 44100  # Unused system parameter (distractor)
    
    grouped_sequences = [(label, list(group)) for label, group in grouped]
    
    for sequence in grouped_sequences:
        label = sequence[0]
        points = sequence[1]
        count = len(points)
        if label == 'PULSE':
            total_cycles += count * 2
        elif label == 'HOLD':
            total_cycles += count

    return total_cycles

# Input signal data
input_signal = [
    (1.2, 'PULSE'),
    (0.8, 'HOLD'),
    (1.5, 'PULSE'),
    (2.1, 'PULSE'),
    (0.9, 'HOLD'),
    (1.1, 'PULSE')
]

total_cycles = analyze_signal_patterns(input_signal)
print(f"Result: {total_cycles}")