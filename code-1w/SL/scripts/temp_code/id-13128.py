scores = {'alice': 85, 'bob': 92, 'carol': 78, 'david': 90}
adjustments = [1.1, 0.9, 1.0, 1.2]
ranked_names = sorted(scores, key=lambda x: scores[x], reverse=True)

top_performer = ranked_names[0]
second_performer = ranked_names[1]

# Calculate average of top two performers
avg_top_two = (scores[top_performer] + scores[second_performer]) / 2

# Apply adjustment based on position: top gets first adjustment, second gets second
if top_performer == 'bob':
    performance_multiplier = adjustments[0]
elif second_performer == 'bob':
    performance_multiplier = adjustments[1]
else:
    performance_multiplier = 1.0

# Update scores with multiplier for next round
updated_scores = {k: v * 1.05 for k, v in scores.items()}

# Special bonus for those above average
threshold = 88
bonus_eligible = [name for name, score in updated_scores.items() if score > threshold]

final_scores = {}
for name in updated_scores:
    if name in bonus_eligible:
        final_scores[name] = int(updated_scores[name] + 5)
    else:
        final_scores[name] = int(updated_scores[name])

winner = 'bob'
result = final_scores.get(winner, 0) * performance_multiplier
print(f"Target result: {result}")