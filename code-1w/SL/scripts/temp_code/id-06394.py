def analyze_trends(data):
    trend_scores = []
    for i, val in enumerate(data):
        if i == 0:
            trend_scores.append(0)
        else:
            diff = val - data[i-1]
            trend_scores.append(1 if diff > 0 else (-1 if diff < 0 else 0))
    return trend_scores

# Irrelevant helper function (dead code path)
def unused_helper(x):
    return sum([i**2 for i in range(x)]) // 2 + 17

# Misleading precomputation
offset = 3
scaling_factor = 1.5
noise_correction = [i * 0.1 for i in range(10)]
useless_sum = sum(noise_correction)

benchmark_data = [12, 15, 14, 18, 22, 20, 25]

# Distractor: secondary processing with no impact
trend_analysis = analyze_trends(benchmark_data)
smoothed_data = [x * scaling_factor for x in benchmark_data]

# Real logic starts here
length = len(benchmark_data)
mod_values = [val % (i+2) for i, val in enumerate(benchmark_data)]
mod_total = sum(mod_values)

averages = []
for i in range(1, len(benchmark_data)+1):
    averages.append(sum(benchmark_data[:i]) / i)

# Key intermediate step
adjusted_avg = sum(averages) / len(averages) + offset

# Use of zip and enumerate together (required python feature)
pairwise_shift = 0
for i, (avg, raw) in enumerate(zip(averages, benchmark_data)):
    if i % 2 == 0 and avg > 15:
        pairwise_shift += raw // (i+1)

# Composite score calculation
base_score = 0
for i, val in enumerate(benchmark_data):
    base_score += val * (i % 4 + 1)

# Final performance metric depends only on mod_total, base_score, and pairwise_shift
final_score = (mod_total + base_score // 10) - pairwise_shift

# Print result as required
print(f"Result: {final_score}")