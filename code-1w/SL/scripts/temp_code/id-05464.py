def analyze_system_performance(nodes):
    # Irrelevant transformation: character frequency map (distractor)
    char_freq = {}
    for node in nodes:
        for char in node['name']:
            char_freq[char] = char_freq.get(char, 0) + 1

    # Misleading intermediate: sorted frequencies (unused later)
    sorted_chars = sorted(char_freq.items(), key=lambda x: -x[1])

    # Core data: power load sequences per node
    load_profiles = []
    for node in nodes:
        raw_loads = node['loads']
        filtered = [x for x in raw_loads if x > 0]  # remove negatives (red herring)
        normalized = [round(x * 0.95, 2) for x in filtered]  # distractor scaling
        load_profiles.append(normalized)

    # Destructuring with enumerate and zip (required Python features)
    indexed_sums = []
    for i, profile in enumerate(load_profiles):
        total = sum(profile)
        indexed_sums.append((i, total))

    # Simulate time-series alignment using zip (distractor logic)
    transposed = list(zip(*[p[:10] for p in load_profiles]))  # truncated
    time_averages = [sum(t)/len(t) for t in transposed]  # computed but unused

    # Dead code path: entropy calculation (never used)
    def calculate_entropy(values):
        from math import log
        total = sum(values)
        probs = [v/total for v in values if v > 0]
        return -sum(p * log(p) for p in probs)

    entropy_val = calculate_entropy([len(p) for p in load_profiles])

    # Actual relevant computation begins here
    base_caps = [max(p) for p in load_profiles]  # peak per node
    adjustments = []
    for i, cap in enumerate(base_caps):
        if i % 2 == 0:
            adjustments.append(cap * 1.1)
        else:
            adjustments.append(cap * 0.9)

    # Combine original and adjusted peaks
    combined_peaks = []
    for orig, adj in zip(base_caps, adjustments):
        combined_peaks.append(round((orig + adj) / 2))

    # Grouping by parity index (combinatorics distractor)
    even_group = [combined_peaks[i] for i in range(len(combined_peaks)) if i % 2 == 0]
    odd_group = [combined_peaks[i] for i in range(len(combined_peaks)) if i % 2 == 1]

    # Sorting groups (irrelevant)
    even_group.sort(reverse=True)
    odd_group.sort()

    # Real signal: aggregate loads across all profiles at each timestep
    aggregate_loads = []
    max_len = max(len(p) for p in load_profiles)
    for t in range(max_len):
        tick_sum = 0
        for profile in load_profiles:
            if t < len(profile):
                tick_sum += profile[t]
        aggregate_loads.append(tick_sum)

    # Key assignment
    peak_capacity = max(aggregate_loads)

    # Print required output
    print(f"Result: {peak_capacity}")

    # Unused cleanup function (dead code)
    def reset_state():
        nonlocal char_freq, indexed_sums, time_averages
        char_freq = {}
        indexed_sums.clear()
        time_averages = []

    return peak_capacity

# Input data
node_data = [
    {'name': 'alpha', 'loads': [100, -50, 200, 150, 300]},
    {'name': 'beta', 'loads': [200, 180, -90, 220, 240, 260]},
    {'name': 'gamma', 'loads': [120, 140, 160, -30, 180]},
    {'name': 'delta', 'loads': [300, 250, 200, 150, 100, 50, 20]}
]

# Execute
analyze_system_performance(node_data)