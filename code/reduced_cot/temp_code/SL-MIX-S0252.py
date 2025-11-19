from collections import defaultdict
from functools import reduce

# Route efficiency metrics: (on_time_rate, avg_delay_minutes, customer_satisfaction)
route_metrics = [
    (0.85, 12, 4.2),
    (0.92, 5, 4.7),
    (0.78, 20, 3.9),
    (0.95, 2, 4.9),
    (0.88, 8, 4.4)
]

# Step 1: Filter routes with on_time_rate >= 0.85 AND avg_delay_minutes <= 10
filtered_routes = list(filter(lambda x: x[0] >= 0.85 and x[1] <= 10, route_metrics))

# Step 2: Compute reliability score for each filtered route: on_time_rate * customer_satisfaction
reliability_scores = list(map(lambda x: x[0] * x[2], filtered_routes))

# Step 3: Use reduce to compute weighted sum where weights are derived from index positions
# Weight formula: (index + 1) * score
weighted_sum = reduce(lambda acc, pair: acc + (pair[0] + 1) * pair[1], enumerate(reliability_scores), 0)

# Step 4: Apply bonus if all filtered routes have customer satisfaction above 4.5
bonus = 1.1 if all(route[2] > 4.5 for route in filtered_routes) else 1.0

# Step 5: Calculate final reliability score
final_reliability_score = round(weighted_sum * bonus, 2)

print(f"Result: {final_reliability_score}")