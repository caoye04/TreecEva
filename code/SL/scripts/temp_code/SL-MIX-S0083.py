import math
from collections import defaultdict

def calculate_priority(base_val, position):
    match position % 4:
        case 0:
            return base_val << 2
        case 1:
            return base_val >> 1
        case 2:
            return base_val ^ 0xF
        case 3:
            return ~base_val & 0xFF

def adjust_with_trig(score, index):
    return int(score * math.sin(index) + math.cos(index * 2))

packages = [12, 25, 8, 33, 19, 42, 7]
processed_scores = []
score_map = defaultdict(int)

for i, pkg in enumerate(packages):
    priority = calculate_priority(pkg, i)
    adjusted = adjust_with_trig(priority, i)
    processed_scores.append(adjusted)
    score_map[i] = adjusted

# Dynamic programming to find optimal loading sequence
n = len(processed_scores)
dp = [0] * (n + 1)
for i in range(1, n + 1):
    dp[i] = max(dp[i-1], dp[i-2] + processed_scores[i-1]) if i > 1 else processed_scores[i-1]

final_loading_score = dp[n] + (sum(packages) & 0x7)
print(f"Result: {final_loading_score}")