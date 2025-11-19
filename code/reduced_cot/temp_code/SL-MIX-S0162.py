import heapq
from collections import defaultdict

def cipher_transform(timestamp_str):
    transformed = ''
    for char in timestamp_str:
        if char.isdigit():
            transformed += str((int(char) + 3) % 10)
        else:
            transformed += char
    return transformed

logs = [
    (5, "2023-10-01T12:34:56"),
    (2, "2023-10-01T11:22:33"),
    (8, "2023-10-01T10:10:10"),
    (1, "2023-10-01T09:08:07"),
    (7, "2023-10-01T13:14:15")
]

priority_heap = []
transformed_logs = {}

for priority, timestamp in logs:
    new_timestamp = cipher_transform(timestamp)
    transformed_logs[new_timestamp] = priority
    heapq.heappush(priority_heap, (priority, new_timestamp))

# Process the top 3 alerts
alert_scores = []
for _ in range(min(3, len(priority_heap))):
    score, _ = heapq.heappop(priority_heap)
    alert_scores.append(score)

# Calculate security index as the product of top alert scores
security_index = 1
for score in alert_scores:
    security_index *= score

print(f"Result: {security_index}")