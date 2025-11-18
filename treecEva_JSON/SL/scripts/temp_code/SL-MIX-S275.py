from itertools import combinations
import bisect

def compute_weighted_sum(scores):
    if not scores:
        return 0
    sorted_scores = sorted(scores)
    n = len(sorted_scores)
    weights = [i + 1 for i in range(n)]
    total = sum(score * weight for score, weight in zip(sorted_scores, weights))
    return total

def process_routes(route_segments):
    valid_segments = []
    for segment in route_segments:
        if segment.efficiency > 0 and segment.duration <= 120:
            valid_segments.append(segment.efficiency)
        else:
            continue
    
    if len(valid_segments) < 3:
        return -1
    
    # Remove outliers using IQR method
    sorted_valid = sorted(valid_segments)
    n = len(sorted_valid)
    q1_index = n // 4
    q3_index = 3 * n // 4
    q1 = sorted_valid[q1_index]
    q3 = sorted_valid[q3_index]
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    
    filtered_scores = [s for s in sorted_valid if lower_bound <= s <= upper_bound]
    
    if len(filtered_scores) < 2:
        return -1
    
    # Compute weighted sum of remaining scores
    return compute_weighted_sum(filtered_scores)

from collections import namedtuple
Segment = namedtuple('Segment', ['efficiency', 'duration'])

# Route data
segments_data = [
    Segment(85, 45),
    Segment(92, 60),
    Segment(78, 90),
    Segment(95, 30),
    Segment(65, 150),  # Outlier due to duration
    Segment(88, 75),
    Segment(91, 50),
    Segment(40, 100),  # Potential outlier in efficiency
    Segment(93, 55),
    Segment(87, 65)
]

final_route_score = process_routes(segments_data)
print(f"Result: {final_route_score}")