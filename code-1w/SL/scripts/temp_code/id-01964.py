def analyze_pattern(data, limit):
    # Precompute transformations with some irrelevant ones
    squared_values = [x**2 for x in data]
    filtered_data = [x for x in data if x > 0]
    reversed_slice = data[::-1][:len(data)//2]  # slicing operation - relevant later
    
    # Irrelevant statistical distractions
    mean_value = sum(data) / len(data) if data else 0
    variance_proxy = sum([abs(x - mean_value) for x in data])  # not used in final logic
    peak_magnitude = max(data, default=0)
    
    # State tracking with conditional logic
    trend_streak = 0
    balance_point = 0
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            trend_streak += 1
        elif data[i] < data[i-1]:
            trend_streak -= 1
        
        # Conditional expression used to update balance
        balance_point += 1 if abs(trend_streak) >= limit else -1
    
    # Secondary analysis on reversed slice (uses slicing)
    adjusted_sum = sum(reversed_slice[::2])  # every other element from reversed first half
    
    # Simulate recursive depth filtering (simple recursion)
    def dampen_value(n, depth=2):
        if depth == 0 or n < 2:
            return n
        return dampen_value(n // 2, depth - 1)

    processed_adjustment = dampen_value(adjusted_sum)

    # Final computation combines multiple concepts
    raw_score = balance_point + processed_adjustment
    normalization_factor = len(filtered_data) - len(squared_values) + peak_magnitude  # includes red herring
    
    # Key result derived from mixed signals
    equilibrium_score = raw_score * (1 if normalization_factor != 0 else 1)
    
    # Dead code path - misleading
    if mean_value < 0:
        equilibrium_score *= -1
    
    return equilibrium_score

# Main execution
sequence = [3, -2, 5, 1, 4, 6, -1]
threshold = 2
equilibrium_score = 0  # initialization

# Intermediate irrelevant calculations
offset_correction = sum(x for x in sequence if x % 2 == 0)
scale_factor = max(sequence) - min(sequence)

# Critical statement
equilibrium_score = analyze_pattern(sequence, threshold)

print(f"Target result: {equilibrium_score}")