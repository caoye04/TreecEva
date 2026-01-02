from collections import defaultdict

# Simulate student quiz scores across multiple topics
topic_scores = [85, 90, 78, 92, 88]
participation_flags = [True, False, True, True, False]
bonus_awarded = [1.0, 0.5, 1.0, 1.2, 0.0]

score_map = defaultdict(int)
for i, score in enumerate(topic_scores):
    score_map[f'student_{i}'] = score

weighted_total = 0.0
count = 0
for i, (score, flag) in enumerate(zip(topic_scores, participation_flags)):
    if flag:
        weighted_total += score * 1.1
    else:
        weighted_total += score
    count += 1

average_performance = weighted_total / count

# Apply bonus only to students with participation
adjusted_scores = [
    (topic_scores[i] * 1.1 + bonus_awarded[i]) if participation_flags[i] 
    else topic_scores[i] for i in range(len(topic_scores))
]

total_score = int(sum(adjusted_scores))
final_adjustment = total_score * 0.95  # Final scaling

print(f"Result: {total_score}")