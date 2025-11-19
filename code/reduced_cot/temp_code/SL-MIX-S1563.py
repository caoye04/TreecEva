import re
import statistics

def calculate_session_diversity(session_activities):
    unique_activities = frozenset(session_activities)
    return len(unique_activities) * 10

def normalize_score(score, mean_val, std_val):
    if std_val == 0:
        return 0
    return (score - mean_val) / std_val

# Session log data
session_logs = [
    "view_product|add_to_cart|checkout|purchase",
    "view_product|view_product|view_product",
    "search|view_product|add_to_wishlist|share|checkout|abandon",
    "login|view_dashboard|logout",
    "view_product|compare|view_product|compare|search"
]

# Process sessions
activity_sets = []
for log in session_logs:
    activities = re.split(r'\|', log)
    activity_sets.append(frozenset(activities))

# Calculate diversity scores
raw_scores = [calculate_session_diversity(list(s)) for s in activity_sets]

# Apply statistical normalization
mean_score = statistics.mean(raw_scores)
std_score = statistics.pstdev(raw_scores) if len(raw_scores) > 1 else 0
normalized_scores = [normalize_score(score, mean_score, std_score) for score in raw_scores]

# Filter high-diversity sessions using set operations
high_diversity_threshold = 0.0
high_diversity_sessions = {i for i, score in enumerate(normalized_scores) 
                         if score > high_diversity_threshold}

# Calculate final weighted score
weights = [1.5, 1.0, 2.0, 0.5, 1.2]
weighted_sum = sum((i+1) * weights[i] for i in high_diversity_sessions)
total_weight = sum(weights[i] for i in high_diversity_sessions)

final_score = 0
if total_weight > 0:
    final_score = round(weighted_sum / total_weight * 100)

print(f"Result: {final_score}")