from collections import defaultdict
import math

# Simulate sensor signal processing with noise filtering and flow computation

def preprocess_signal(raw_data, noise_floor):
    cleaned = []
    for val in raw_data:
        if abs(val) > noise_floor:
            cleaned.append(abs(val))
    return sorted(cleaned, reverse=True)


def generate_threshold_map(keys, base):
    # Irrelevant helper that creates distracting data
    return {k: base * (i + 1) for i, k in enumerate(keys)}


def calculate_amplitude_score(seq):
    # Distractor function - not used in final result
    if not seq:
        return 0.0
    return sum(math.sqrt(x) for x in seq if x % 2 == 1)


def calculate_net_flow(signals, thresholds):
    flow = 0
    category_count = defaultdict(int)
    
    for key in signals:
        category_count[key[0]] += 1
    
    # Real logic starts here
    for label, vals in signals.items():
        capped_vals = [min(v, thresholds.get(label, 50)) for v in vals]
        adjusted_sum = sum(v - 10 for v in capped_vals if v > 15)
        flow += adjusted_sum
    
    # Dead code branch - misleading control flow
    if len(category_count) > 10:
        flow -= 100  # Never reached
    
    return flow

# Main execution
raw_input_data = {
    'A': [-5, 23, -18, 45, 12],
    'B': [31, -44, 19, 27],
    'C': [15, -22, 33, 38],
    'D': [29, -30, 41]
}

# Preprocessing phase
processed_signals = {}
for tag, readings in raw_input_data.items():
    filtered = preprocess_signal(readings, noise_floor=10)
    processed_signals[tag] = [x - 5 for x in filtered if x > 12]  # Further refine

# Generate maps (one useful, one irrelevant)
threshold_map = generate_threshold_map(processed_signals.keys(), base=25)
amplitude_weights = {k: len(v) * 1.5 for k, v in processed_signals.items()}  # Unused

# Secondary distractor variables
normalization_factor = sum(len(v) for v in raw_input_data.values()) or 1
scaling_curve = list(map(lambda x: round(x**0.5, 2), range(1, 6)))  # Not used

# Key computation
net_flow = calculate_net_flow(processed_signals, threshold_map)

# Additional red herring computations
entropy_score = sum(math.log(v) if v > 0 else 0 for v in threshold_map.values())
peak_magnitude = max(max(v) for v in processed_signals.values()) if any(processed_signals.values()) else 0

# Final output
Result: {net_flow}