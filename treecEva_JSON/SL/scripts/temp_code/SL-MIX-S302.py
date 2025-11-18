import heapq
import math

def calculate_priority(distance, weight, urgency):
    base_score = distance * 0.5 + weight * 2.0
    adjusted_score = base_score if urgency == 'normal' else base_score * (1.5 if urgency == 'high' else 2.0)
    return int(adjusted_score)

def process_deliveries(requests_heap):
    processed_scores = []
    while requests_heap:
        priority, distance, weight, urgency = heapq.heappop(requests_heap)
        if distance > 100 and weight < 50:
            continue
        score = calculate_priority(distance, weight, urgency)
        if urgency != 'low' or score > 100:
            processed_scores.append(score)
    return processed_scores

delivery_requests = [
    (10, 120, 45, 'high'),
    (5, 80, 60, 'normal'),
    (15, 150, 30, 'low'),
    (8, 95, 55, 'high'),
    (12, 200, 25, 'normal')
]

# Create max heap using negative priorities
requests_heap = [(-priority, distance, weight, urgency) for priority, distance, weight, urgency in delivery_requests]
heapq.heapify(requests_heap)

processed_scores = process_deliveries(requests_heap)

# Calculate final priority score using complex aggregation
priority_weights = {i: math.log(i+2) for i in range(len(processed_scores))}
weighted_scores = {i: processed_scores[i] * priority_weights[i] for i in range(len(processed_scores)) if processed_scores[i] > 100}

final_priority_score = sum(weighted_scores.values()) if weighted_scores else 0
final_priority_score = int(final_priority_score) & 0xFF  # Keep only lower 8 bits

print(f"Result: {final_priority_score}")