import math

def calculate_intersection_efficiency(layout_points, traffic_data):
    # Calculate area using shoelace formula
    n = len(layout_points)
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += layout_points[i][0] * layout_points[j][1]
        area -= layout_points[j][0] * layout_points[i][1]
    area = abs(area) / 2.0
    
    # Calculate traffic variance
    mean_flow = sum(traffic_data) / len(traffic_data)
    variance = sum((x - mean_flow) ** 2 for x in traffic_data) / len(traffic_data)
    
    # Efficiency formula
    return area * (100 - variance) if variance < 100 else 0

# Intersection data
intersections = [
    {'id': 'A', 'points': [(0,0), (0,10), (10,10), (10,0)], 'traffic': [50, 55, 45, 60, 50]},
    {'id': 'B', 'points': [(0,0), (0,8), (12,8), (12,0)], 'traffic': [40, 42, 38, 45, 35]},
    {'id': 'C', 'points': [(0,0), (0,6), (15,6), (15,0)], 'traffic': [30, 35, 25, 40, 30]}
]

# State machine for processing
states = ['INIT', 'PROCESS', 'EVALUATE', 'FINALIZE']
current_state = 'INIT'
scores = []

while current_state != 'FINALIZE':
    if current_state == 'INIT':
        current_state = 'PROCESS'
    elif current_state == 'PROCESS':
        for intersection in intersections:
            score = calculate_intersection_efficiency(intersection['points'], intersection['traffic'])
            scores.append(score)
        current_state = 'EVALUATE'
    elif current_state == 'EVALUATE':
        avg_score = sum(scores) / len(scores)
        weighted_scores = [s * (1.2 if s > avg_score else 0.8) for s in scores]
        final_score = sum(weighted_scores) / len(weighted_scores)
        current_state = 'FINALIZE'

print(f'Result: {int(final_score)}')