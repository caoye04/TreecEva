from collections import defaultdict, Counter

# Simulate network traffic load over time with noise injection
def generate_noisy_load(baseline, hour):
    noise = (hour * 17) % 13
    return baseline + noise if hour % 4 != 0 else baseline - 5

def analyze_fragmentation(data_stream):
    # Irrelevant analysis function – decoy
    frag_score = 0
    for i in range(len(data_stream)):
        if data_stream[i] > 100:
            frag_score += 1
    return frag_score

def normalize_values(values):
    # Unused normalization path – dead code
    total = sum(values)
    return [v / total for v in values] if total > 0 else values

def simulate_buffer_overflow(load_profile):
    # Misleading intermediate calculation – distractor
    threshold = 85
    overflow_events = 0
    for load in load_profile:
        if load > threshold:
            overflow_events += 1
    return overflow_events * 2  # Not used in final result

def evaluate_redundancy(nodes):
    # Decoy function with complex logic but no impact
    redundancy_map = defaultdict(int)
    for node in nodes:
        redundancy_map[node % 7] += 1
    counter = Counter(redundancy_map)
    return sum(counter.values()) % 19

def calculate_peak(loads, factor):
    # Core logic: find max after applying efficiency scaling
    adjusted = [load * factor for load in loads]
    filtered = adjusted[::2]  # Slice every other element – relevant
    temp_result = sum(filtered) / len(filtered)
    
    # Additional distraction inside core function
    outlier_check = [x for x in adjusted if x > 120]
    adjustment = len(outlier_check) * 0.5 if len(outlier_check) > 3 else 0
    
    # Final peak depends on conditional expression and slicing
    peak = max(adjusted) + adjustment if len(outlier_check) else max(adjusted) - 10
    return int(peak)

# Main simulation setup
baseline_load = 60
hours = list(range(24))
network_loads = [generate_noisy_load(baseline_load, h) for h in hours]

# Inject irrelevant data structures
traffic_matrix = [[0]*5 for _ in range(5)]
node_registry = {f'node_{i}': i*3 + 2 for i in range(15)}

# Unused intermediate transformations
fragmentation_index = analyze_fragmentation(network_loads)
overflow_count = simulate_buffer_overflow(network_loads)
redundancy_score = evaluate_redundancy(list(node_registry.values()))

# Efficiency model with conditional expression
base_efficiency = 1.15
age_factor = 8
condition_factor = 0.9 if age_factor > 5 else 1.0

# Critical assignment
efficiency_factor = base_efficiency * condition_factor

# Key statement
peak_capacity = calculate_peak(network_loads, efficiency_factor)

# Print result as required
print(f"Target result: {peak_capacity}")