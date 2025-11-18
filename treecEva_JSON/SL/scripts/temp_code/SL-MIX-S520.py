import heapq
from collections import deque

def calculate_priority(distance, weight, deadline):
    return (distance * 0.3) + (weight * 0.5) + (deadline * 0.2)

def process_deliveries_divide_conquer(delivery_queue):
    if len(delivery_queue) <= 1:
        return delivery_queue
    mid = len(delivery_queue) // 2
    left = process_deliveries_divide_conquer(delivery_queue[:mid])
    right = process_deliveries_divide_conquer(delivery_queue[mid:])
    return merge_deliveries(left, right)

def merge_deliveries(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i][0] >= right[j][0]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

delivery_data = [
    (12.5, 4.2, 3),
    (8.7, 6.1, 2),
    (15.3, 3.8, 4),
    (6.9, 7.5, 1),
    (11.2, 5.3, 3)
]

priority_heap = []
for idx, (dist, wt, dl) in enumerate(delivery_data):
    priority = calculate_priority(dist, wt, dl)
    heapq.heappush(priority_heap, (-priority, idx, dist, wt, dl))

sorted_deliveries = []
while priority_heap:
    _, idx, d, w, dl = heapq.heappop(priority_heap)
    sorted_deliveries.append((d, w, dl))

processed_deliveries = process_deliveries_divide_conquer(sorted_deliveries)

completion_times = []
accumulated_time = 0.0
for distance, weight, _ in processed_deliveries:
    time_factor = distance * 0.8 + weight * 0.2
    accumulated_time += time_factor
    completion_times.append(accumulated_time)

fleet_efficiency_score = 0.0
for i in range(len(completion_times)):
    fleet_efficiency_score += completion_times[i] * (i + 1)

fleet_efficiency_score = round(fleet_efficiency_score, 2)
print(f"Result: {fleet_efficiency_score}")