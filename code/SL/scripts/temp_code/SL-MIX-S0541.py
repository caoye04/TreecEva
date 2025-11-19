from collections import defaultdict
import math

def calculate_polygon_area(vertices):
    n = len(vertices)
    area = 0
    for i in range(n):
        j = (i + 1) % n
        area += vertices[i][0] * vertices[j][1]
        area -= vertices[j][0] * vertices[i][1]
    return abs(area) / 2

def get_resource_priority(district_id):
    match district_id:
        case 1: return 0.8
        case 2: return 1.2
        case 3: return 0.9
        case 4: return 1.1
        case _: return 1.0

districts = [
    {'id': 1, 'vertices': [(0, 0), (4, 0), (4, 3), (0, 3)]},
    {'id': 2, 'vertices': [(1, 1), (5, 1), (5, 4), (1, 4)]},
    {'id': 3, 'vertices': [(2, 2), (6, 2), (6, 5), (2, 5)]},
    {'id': 4, 'vertices': [(3, 3), (7, 3), (7, 6), (3, 6)]}
]

area_scores = defaultdict(float)
for district in districts:
    area = calculate_polygon_area(district['vertices'])
    priority = get_resource_priority(district['id'])
    area_scores[district['id']] = area * priority

available_resources = 100
allocation = {}
remaining_resources = available_resources

sorted_districts = sorted(area_scores.items(), key=lambda x: x[1], reverse=True)
for district_id, score in sorted_districts:
    if remaining_resources <= 0:
        allocation[district_id] = 0
        continue
    
    allocated = min(math.floor(score), remaining_resources)
    allocation[district_id] = allocated
    remaining_resources -= allocated

optimal_allocation = sum(allocation[district_id] * get_resource_priority(district_id) for district_id in allocation)
print(f"Result: {int(optimal_allocation)}")