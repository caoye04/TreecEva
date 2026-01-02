def analyze_pattern(data):
    # Lambda for transforming frequency counts
    freq_map = {}
    for item in data:
        freq_map[item] = freq_map.get(item, 0) + 1

    # Irrelevant transformation: character counting in stringified keys
    char_count = 0
    temp_str = ''
    for k in freq_map.keys():
        temp_str += str(k)
    char_count = sum(1 for c in temp_str if c.isdigit())

    # Semi-relevant processing: filter frequent items
    threshold = len(data) // 3
    frequent_items = [k for k, v in freq_map.items() if v >= threshold]

    # Dead code path: unused helper function
    def unused_helper(x):
        return x ** 2 + 1  # never called

    # Distractor: complex-looking but unused list comprehension
    _ = [i * j for i in range(len(frequent_items)) for j in range(1, 4) if i % 2 == 0]

    # Core logic: compute weighted sum of frequent diagnostics
    weight_fn = lambda x: 2 if x > 5 else 1
    weighted_sum = 0
    for val in frequent_items:
        if val % 2 == 1:  # only odd values contribute
            weighted_sum += val * weight_fn(val)

    # Additional distraction: unused state tracking
    state_log = []
    for i in range(3):
        state_log.append(f'State {i}: passive')

    # Final computation with relevant logic
    adjustment = len(frequent_items) if weighted_sum > 0 else -1
    final_score = weighted_sum + adjustment

    # Key assignment point
    final_diagnostic = final_score * 10 // (len(data) or 1)

    return final_diagnostic

# Simulate sensor diagnostics stream
diagnostics = [3, 7, 3, 9, 7, 3, 4, 8, 7, 3, 7, 9]

# Execute critical statement
final_diagnostic = analyze_pattern(diagnostics)

print(f"Result: {final_diagnostic}")