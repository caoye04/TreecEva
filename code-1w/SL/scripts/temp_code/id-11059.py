from collections import defaultdict

# Simulate user feedback counts by category
categories = ['usability', 'performance', 'design', 'security', 'documentation']
raw_feedback = [
    'usability', 'performance', 'usability', 'design', 
    'security', 'usability', 'performance', 'usability'
]

# Count feedback using defaultdict
feedback_count = defaultdict(int)
for item in raw_feedback:
    feedback_count[item] += 1

# Add zero entries for categories with no feedback
for cat in categories:
    if cat not in feedback_count:
        feedback_count[cat] = 0

# Define dynamic threshold based on average feedback
average_count = sum(feedback_count.values()) / len(feedback_count)
threshold_func = lambda x: x >= average_count

# Determine performance score based on threshold crossing
def evaluate_performance(feed_dict, threshold):
    above_threshold = 0
    for key in categories:
        if threshold(feed_dict[key]):
            above_threshold += 1
    return above_threshold * 2  # Each qualifying category contributes 2 points

# Compute final score
final_score = evaluate_performance(feedback_count, threshold_func)
print(f"Result: {final_score}")