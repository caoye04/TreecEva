from collections import Counter
def analyze_neural_activity(readings):
    spike_counts = Counter()
    for region, signals in readings.items():
        spike_counts[region] = sum(1 for s in signals if s > 0.7)
    
    activation_map = {}
    for region, count in spike_counts.items():
        activation_map[region] = 'high' if count >= 3 else 'low'
    
    def calculate_threshold(counts, activations):
        total_active = sum(1 for v in activations.values() if v == 'high')
        avg_spikes = sum(counts.values()) / len(counts)
        scaling_factor = 1.5 if total_active > 1 else 1.0
        return int(avg_spikes * scaling_factor)
    
    # Irrelevant baseline metric (minor distraction)
    baseline_noise = sum(len(signals) for signals in readings.values()) * 0.05
    
    active_threshold = calculate_threshold(spike_counts, activation_map)
    return active_threshold

# Input data
eeg_data = {
    'prefrontal': [0.8, 0.6, 0.9, 0.75],
    'hippocampus': [0.5, 0.4, 0.8, 0.65],
    'amygdala': [0.9, 0.85, 0.78, 0.92]
}

result = analyze_neural_activity(eeg_data)
print(f"Target result: {result}")