from collections import defaultdict
import math

# Simulate sensor data with some noise
data = [4.5, 3.2, 7.8, 2.1, 9.0, 5.5]
weights = [0.1, 0.3, 0.15, 0.05, 0.2, 0.2]

# Irrelevant backup data (distractor)
backup_data = [x * 1.05 for x in data if x > 4]

# Misleading transformation using lambda (not used later)
transformed = list(map(lambda x: math.sqrt(x) if x > 5 else x / 2, data))

# Track frequency of rounded values (semi-relevant but not critical)
freq_tracker = defaultdict(int)
for val in data:
    freq_tracker[round(val)] += 1

# Weighted sum calculation
weighted_sum = sum(d * w for d, w in zip(data, weights))

# Apply non-linear boost if average exceeds threshold
avg = sum(data) / len(data)
boost_factor = 1.2 if avg > 5.0 else 1.0
adjusted_sum = weighted_sum * boost_factor

# Secondary adjustment based on max value
max_val = max(data)
penalty = 0.5 if max_val >= 9.0 else 0

# Final score computation
final_score = adjusted_sum - penalty

# Dead code path (never executed, red herring)
if False:
    final_score *= 1.1
    temp = [x ** 2 for x in weights]

# Print result
print(f"Result: {final_score}")