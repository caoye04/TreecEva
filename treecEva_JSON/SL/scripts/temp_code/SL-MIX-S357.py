import heapq
from collections import defaultdict

# Package weights in kilograms
package_weights = [12.5, 8.3, 15.7, 6.2, 22.1, 9.8, 18.4, 5.1, 14.6, 11.9]

# Initialize data structures
weight_categories = defaultdict(list)
priority_heap = []

# Categorize packages by weight ranges
for weight in package_weights:
    if weight >= 15.0:
        weight_categories['heavy'].append(weight)
    elif weight >= 10.0 and weight < 15.0:
        weight_categories['medium'].append(weight)
    else:
        weight_categories['light'].append(weight)

# Process heavy packages with priority calculation
for weight in weight_categories['heavy']:
    priority = int(weight * 2.5)
    heapq.heappush(priority_heap, -priority)  # Max heap using negative values

# Process medium packages with priority calculation
for weight in weight_categories['medium']:
    if weight >= 12.0:  # Short-circuit evaluation
        priority = int(weight * 1.8)
        heapq.heappush(priority_heap, -priority)

# Calculate final priority score
final_priority_score = 0
while priority_heap:
    priority = -heapq.heappop(priority_heap)  # Convert back to positive
    final_priority_score += priority
    
# Apply final transformation
final_priority_score = sum(map(lambda x: x // 2, [final_priority_score]))

print(f"Result: {final_priority_score}")