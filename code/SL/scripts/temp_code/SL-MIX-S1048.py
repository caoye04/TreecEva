from collections import defaultdict
from functools import reduce
import math

def calculate_route_score(on_time_pct, fuel_avg, satisfaction):
    efficiency = (on_time_pct / 100) * 0.5 + (1 - min(fuel_avg / 50, 1)) * 0.3 + (satisfaction / 10) * 0.2
    return round(efficiency * 1000)

routes_data = [
    {'id': 'R001', 'on_time': 85, 'fuel': 42.3, 'satisfaction': 8.7},
    {'id': 'R002', 'on_time': 92, 'fuel': 38.1, 'satisfaction': 9.2},
    {'id': 'R003', 'on_time': 78, 'fuel': 45.6, 'satisfaction': 7.9},
    {'id': 'R004', 'on_time': 95, 'fuel': 35.8, 'satisfaction': 9.5},
    {'id': 'R005', 'on_time': 88, 'fuel': 40.2, 'satisfaction': 8.3}
]

route_scores = defaultdict(int)
for route in routes_data:
    score = calculate_route_score(route['on_time'], route['fuel'], route['satisfaction'])
    route_scores[route['id']] = score

sorted_routes = sorted(route_scores.items(), key=lambda x: x[1], reverse=True)
top_route_score = sorted_routes[0][1] if sorted_routes else 0

# Apply a bonus factor using ternary operator and bit manipulation
bonus_factor = 1.1 if top_route_score > 800 else 1.05
adjusted_score = int(top_route_score * bonus_factor)
top_route_score = adjusted_score ^ (adjusted_score >> 3) if adjusted_score > 850 else adjusted_score

print(f"Result: {top_route_score}")