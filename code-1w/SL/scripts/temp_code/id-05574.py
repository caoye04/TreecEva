from collections import Counter, defaultdict
import math

def analyze_trends(data):
    trends = []
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            trends.append('up')
        elif data[i] < data[i-1]:
            trends.append('down')
        else:
            trends.append('same')
    return trends

def compute_variance(values):
    mean = sum(values) / len(values)
    squared_diffs = [(x - mean) ** 2 for x in values]
    variance = sum(squared_diffs) / len(squared_diffs)
    return variance

def filter_outliers(nums, threshold=1.5):
    q1 = sorted(nums)[len(nums)//4]
    q3 = sorted(nums)[3*len(nums)//4]
    iqr = q3 - q1
    lower, upper = q1 - threshold * iqr, q3 + threshold * iqr
    return [n for n in nums if lower <= n <= upper]

def evaluate_performance(ratings):
    raw_total = sum(ratings)
    rating_counts = Counter(ratings)
    mode = max(rating_counts, key=rating_counts.get)
    
    # Irrelevant aggregation
    category_map = defaultdict(list)
    for r in ratings:
        if r < 3:
            category_map['low'].append(r)
        elif r < 4:
            category_map['medium'].append(r)
        else:
            category_map['high'].append(r)
    
    adjustment_factor = 1.0
    if len(category_map['high']) > len(category_map['low']):
        adjustment_factor *= 1.1
    
    # Distractor: complex but unused calculation
    entropy = 0.0
    total = sum(rating_counts.values())
    for count in rating_counts.values():
        p = count / total
        entropy -= p * math.log(p)
    
    # Unused smoothing
    smoothed = [ratings[0]]
    for i in range(1, len(ratings)-1):
        smoothed.append(sum(ratings[i-1:i+2]) / 3)
    smoothed.append(ratings[-1])
    
    # Actual logic path
    filtered_ratings = filter_outliers(ratings)
    base_score = sum(filtered_ratings) / len(filtered_ratings)
    variance_penalty = compute_variance(filtered_ratings) * 0.5
    trend_sequence = analyze_trends(ratings)
    upward_pressure = trend_sequence.count('up') - trend_sequence.count('down')
    
    final_score = base_score - variance_penalty + (upward_pressure * 0.1)
    return int(round(final_score))

# Simulation data
initial_metrics = [2, 3, 4, 5, 4, 3, 2, 4, 5, 5, 4, 3, 3, 4, 5]
efficiency_ratings = [x * 1.1 for x in initial_metrics]
efficiency_ratings = [int(x * 10) / 10 for x in efficiency_ratings]  # Round to 1 decimal

# Key computation step
final_score = evaluate_performance(efficiency_ratings)
print(f"Result: {final_score}")