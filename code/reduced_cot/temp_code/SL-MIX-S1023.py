import heapq

def compute_channel_efficiency(data):
    return sum(data) // len(data)

channels_data = {
    'channel_A': [120, 130, 125],
    'channel_B': [200, 210, 190],
    'channel_C': [80, 85, 75]
}

# Compute efficiency for each channel
base_scores = {name: compute_channel_efficiency(values) for name, values in channels_data.items()}

# Apply bonus if efficiency exceeds threshold
bonus_applied = {name: score + 10 if score > 100 else score for name, score in base_scores.items()}

# Get top two scores using a min-heap
heap = []
for score in bonus_applied.values():
    if len(heap) < 2:
        heapq.heappush(heap, score)
    elif score > heap[0]:
        heapq.heapreplace(heap, score)

top_scores = sorted(heap, reverse=True)

# Short-circuit evaluation to determine final score
final_score = top_scores[0] + top_scores[1] if top_scores and len(top_scores) >= 2 and top_scores[0] > 0 and top_scores[1] > 0 else 0

print(f"Result: {final_score}")