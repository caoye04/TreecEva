import heapq

# Initialize heap with popularity scores (lower is more popular)
pie_scores = [12, 8, 20, 7, 15]
heapq.heapify(pie_scores)

# Process sales - remove the most popular (lowest score), then add new items
removed_score = heapq.heappop(pie_scores)
heapq.heappush(pie_scores, 5)
heapq.heappush(pie_scores, 18)

# After all operations, get the top score
final_top_score = pie_scores[0]
print(f'Result: {final_top_score}')