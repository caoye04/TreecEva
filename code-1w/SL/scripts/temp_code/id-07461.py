from collections import defaultdict
import math

# Simulate system performance metrics over time
metrics = [85, 90, 78, 92, 88]
weights = [0.2, 0.3, 0.15, 0.25, 0.1]

# Irrelevant backup data (distractor)
backup_metrics = [x * 1.05 for x in metrics]
adjusted_backup = list(map(lambda x: max(0, min(100, x)), backup_metrics))

# Helper function to normalize values (partially relevant)
def normalize(data):
    total = sum(data)
    return [round(x / total, 4) for x in data]

# Weight analysis (semi-relevant but not used directly)
normalized_weights = normalize(weights)

# Bitwise diagnostic check (distractor - simulates hardware check)
diagnostic_flag = 0
for val in metrics:
    diagnostic_flag ^= (val & 7)  # XOR with lower 3 bits

diagnostic_log = []
for i, val in enumerate(metrics):
    if (val >> 2) % 3 == 0:  # Right shift and modulo check
        diagnostic_log.append(i)

# Real computation begins here
weighted_sum = 0.0
for i in range(len(metrics)):
    weighted_sum += metrics[i] * weights[i]

# Additional adjustment based on consistency (relevant)
consistency_bonus = 0
if all(abs(metrics[i] - metrics[i+1]) < 10 for i in range(len(metrics)-1)):
    consistency_bonus = 5

# Secondary scoring via tuple unpacking and enumeration (relevant)
score_components = defaultdict(float)
for idx, (m, w) in enumerate(zip(metrics, weights)):
    score_components[f'segment_{idx}'] = m * w * 10  # Scale up contribution

# Dummy accumulation (distractor)
temp_accumulator = 0
for k, v in score_components.items():
    temp_accumulator += v * 0.01  # Minor side-effect calc

# Final evaluation logic
base_performance = sum(score_components.values()) / 10  # Reverse scaling
final_score = base_performance + consistency_bonus

# Misleading final adjustment (not applied, distractor)
theoretical_max = sum(w * 100 for w in weights)
if final_score > theoretical_max:
    final_score = theoretical_max

print(f"Result: {final_score}")