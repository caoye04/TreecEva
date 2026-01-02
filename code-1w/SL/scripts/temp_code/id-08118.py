from collections import defaultdict
import itertools

# Simulate sensor array phase readings and frequency weighting for interference analysis
def analyze_sensor_interference():
    base_frequencies = [50, 60, 100, 120, 400]
    phase_offsets = [0.1, -0.2, 0.15, -0.05, 0.3]
    signal_strengths = [85, 92, 78, 88, 95]

    # Irrelevant transformation: normalize strengths (not used in final calculation)
    normalized_strengths = [s / max(signal_strengths) for s in signal_strengths]
    avg_strength = sum(normalized_strengths) / len(normalized_strengths)

    # Generate all pairwise combinations for cross-interference consideration
    combo_pairs = list(itertools.combinations(base_frequencies, 2))
    frequency_ratios = defaultdict(float)

    for a, b in combo_pairs:
        frequency_ratios[(a, b)] = round(a / b, 3) if b != 0 else 0

    # Weighted contribution based on harmonic proximity to 60Hz
    reference_freq = 60
    proximity_weights = {}
    for freq in base_frequencies:
        detune = abs(freq - reference_freq)
        weight = 1 / (1 + detune / 10)
        proximity_weights[freq] = round(weight, 3)

    # Simulate phase state transitions under load
    phase_states = []
    for i, offset in enumerate(phase_offsets):
        state_vector = [
            offset * 2 if i % 2 == 0 else offset * 1.5,
            offset * -1,
            abs(offset) * 0.5
        ]
        # Add dummy operation: simulate noise filtering
        filtered = [x for x in state_vector if abs(x) > 0.05]  # Not actually used
        phase_states.append(state_vector)

    frequency_weights = [proximity_weights[f] for f in base_frequencies]

    # Dead code: simulation of thermal drift (never called)
    def simulate_thermal_drift(temp):
        return temp * 0.02 if temp > 30 else 0

    # Core interference calculation
    def calculate_interference(phases, weights):
        total_shift = 0.0
        for i, (phase_row, w) in enumerate(zip(phases, weights)):
            row_effect = 0
            for j, p in enumerate(phase_row):
                if j % 2 == 0:
                    row_effect += p * w
                else:
                    row_effect -= p * w
            total_shift += abs(row_effect)
        return round(total_shift, 4)

    net_phase_shift = calculate_interference(phase_states, frequency_weights)
    
    # Additional irrelevant computation: simulate data logging overhead
    log_entries = []
    for freq in base_frequencies:
        log_entries.append(f"Sensor_{freq}: Active")
    entry_count = len(log_entries)

    return net_phase_shift

result = analyze_sensor_interference()
print(f"Result: {result}")