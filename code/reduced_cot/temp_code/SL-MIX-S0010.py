import heapq

# Define bird point mapping
bird_points = {'common': 1, 'rare': 3, 'endangered': 5}

# Observation batch
observations = ['common', 'rare', 'common', 'endangered', 'rare']

# Calculate base score
base_score = sum(bird_points[bird] for bird in observations)

# Determine weight using ternary operator
weight = 2 if len(observations) > 5 else 1

# Calculate weighted score
weighted_score = base_score * weight

# Heap to track minimum score
score_heap = []
heapq.heappush(score_heap, weighted_score)

# For demonstration, let's add another dummy batch score
heapq.heappush(score_heap, 20)

# Final score is the minimum from heap
final_score = heapq.heappop(score_heap)

print(f"Result: {final_score}")