from collections import Counter

def find_mode_value(data):
    freq = Counter(data)
    return max(freq, key=freq.get)

def find_median_score(scores):
    sorted_scores = sorted(scores)
    n = len(sorted_scores)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_scores[mid - 1] + sorted_scores[mid]) / 2
    else:
        return sorted_scores[mid]

# Irrelevant data (minor distraction)
data_logs = [101, 102, 101, 103, 102, 102]
mode_val = find_mode_value(data_logs)  # Not used in main computation

# Main dataset for problem
scores = [85, 92, 78, 96, 88, 91, 87]
result = find_median_score(scores)
print(f"Result: {result}")