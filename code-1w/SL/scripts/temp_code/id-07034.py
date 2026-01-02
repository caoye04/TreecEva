from itertools import combinations

def generate_metrics(raw_values):
    squared = [x**2 for x in raw_values if x > 0]
    filtered = [s for s in squared if s < 1000]
    return filtered

def track_state(events):
    state_log = {}
    for e in events:
        if e not in state_log:
            state_log[e] = 0
        state_log[e] += 1
    # Irrelevant tracking
    cumulative = sum(state_log.values())
    avg_per_event = cumulative / len(state_log) if state_log else 0
    return avg_per_event

def analyze_efficiency(data, limit):
    temp_results = []
    for i, val in enumerate(data):
        if i % 2 == 0:
            adjusted = val - (i * 0.1)
        else:
            adjusted = val + (i * 0.05)
        temp_results.append(adjusted)
    
    # Real computation path
    base_total = sum(temp_results)
    penalty = 0
    for pair in combinations(temp_results, 2):
        if abs(pair[0] - pair[1]) > limit:
            penalty += 0.5
    
    # Dead code - misleading calculation
    peak_moment = max(temp_results) if temp_results else 0
    decay_factor = peak_moment * 0.01  # Not used later
    
    final_score = base_total - penalty
    return int(final_score)

# Main execution
raw_input = [3, 7, -2, 8, 4, 0, 6]
processed = generate_metrics(raw_input)
events = ['start', 'run', 'pause', 'run', 'end']

auxiliary_score = track_state(events)

threshold = 3.5
performance_data = [x + 1 for x in processed if x != 25]  # Filter out phantom value

# Key intervention point
efficiency_score = analyze_efficiency(performance_data, threshold)

# Print result as required
print(f"Target result: {efficiency_score}")