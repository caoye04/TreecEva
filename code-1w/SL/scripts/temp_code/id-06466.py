from itertools import compress

# Water filter efficiency testing data
filter_runtimes = [15, 27, 12, 38, 21, 9]
efficiency_flags = [runtime > 10 for runtime in filter_runtimes]

# Simulate weight of contaminants removed (proportional to runtime)
base_weights = [runtime * 0.7 for runtime in filter_runtimes]

# Apply conditional filtering: only consider filters that ran longer than 10 mins
purified_weights = list(compress(base_weights, efficiency_flags))

# Secondary adjustment: reduce by 5% due to measurement drift
adjusted_weights = [w * 0.95 for w in purified_weights]

# Final score based on best performance
filtration_score = max(purified_weights) if purified_weights else 0

# Irrelevant auxiliary variable (minor distraction)
avg_runtime = sum(filter_runtimes) / len(filter_runtimes)

print(f"Result: {filtration_score}")