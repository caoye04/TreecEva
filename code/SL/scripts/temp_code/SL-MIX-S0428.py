from collections import deque
from functools import reduce

def compute_threat_sequence(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

packet_timestamps = [3, 5, 7, 11, 13]
threat_scores = []
window_size = 3

for i in range(len(packet_timestamps)):
    score = compute_threat_sequence(packet_timestamps[i] % 10)
    threat_scores.append(score)

sliding_window = deque(maxlen=window_size)
window_scores = []

for score in threat_scores:
    sliding_window.append(score)
    if len(sliding_window) == window_size:
        window_sum = sum(sliding_window)
        window_scores.append(window_sum)

stack = []
for score in window_scores:
    if score > 10:
        stack.append(score)

final_threat_score = reduce(lambda x, y: x + y, stack, 0)
print(f"Result: {final_threat_score}")