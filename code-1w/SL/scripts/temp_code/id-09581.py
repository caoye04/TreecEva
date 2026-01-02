def analyze_pattern(seq):
    """Analyzes sequence patterns with distractor computations."""
    length = len(seq)
    unused_sum = sum(x ** 2 for x in seq)  # Distractor: not used later
    temp_vals = [seq[i] + seq[-i-1] for i in range(length // 2)]
    
    # Irrelevant filtering (dead-end computation)
    filtered_outliers = [x for x in seq if x > 30]
    outlier_count = len(filtered_outliers) * 0  # Always zero, misleading

    # Core transformation
    transformed = list(map(lambda x: (x * 2) % 17, temp_vals))
    return transformed


# Simulated sensor readings (real data stream)
data_stream = [5, 12, 8, 14, 9, 11]

# Step 1: Extract mirror pairs and process
pair_sums = []
for i in range(len(data_stream) // 2):
    pair_sums.append(data_stream[i] + data_stream[-(i+1)])

# Step 2: Apply analysis with side-effect-free helper
analysis_result = analyze_pattern(data_stream)

# Step 3: Build precision chain using cumulative logic
cumulative_shift = 0
precision_chain = []
for val in analysis_result:
    adjusted = val + cumulative_shift
    cumulative_shift += (adjusted % 5)
    precision_chain.append(adjusted)

# Misleading statistical check (no impact on result)
mean_precision = sum(precision_chain) / len(precision_chain) if precision_chain else 0
std_deviation_proxy = sum((x - mean_precision) ** 2 for x in precision_chain) ** 0.5

# Step 4: Final scoring via lambda-based reducer
calculate_final = lambda chain: sum(x * (i + 1) for i, x in enumerate(chain)) // 3

final_score = calculate_final(precision_chain)

# Print result as required
print(f"Target result: {final_score}")