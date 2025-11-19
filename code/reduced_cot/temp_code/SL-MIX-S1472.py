import itertools
from functools import reduce

def calculate_priority_modifier(weights):
    if not weights:
        return 0
    positive_weights = [w for w in weights if w > 0]
    negative_weights = [abs(w) for w in weights if w < 0]
    pos_product = reduce(lambda x, y: x * y, positive_weights, 1)
    neg_sum = sum(negative_weights)
    return pos_product - neg_sum if pos_product > neg_sum else neg_sum - pos_product

def get_route_efficiency(traffic_conditions, weather_factor):
    efficiency_base = 0
    if traffic_conditions == 'heavy':
        efficiency_base = 10
    elif traffic_conditions == 'moderate':
        efficiency_base = 25
    elif traffic_conditions == 'light':
        efficiency_base = 40
    else:
        efficiency_base = 5
    
    if weather_factor == 'storm':
        efficiency_base -= 15
    elif weather_factor == 'rain':
        efficiency_base -= 5
    elif weather_factor == 'clear':
        efficiency_base += 10
    
    return max(0, efficiency_base)

# Main execution
packages = [
    {'weight': 5, 'fragile': True, 'express': False},
    {'weight': -3, 'fragile': False, 'express': True},
    {'weight': 2, 'fragile': True, 'express': True},
    {'weight': -1, 'fragile': False, 'express': False}
]

fragile_count = sum(1 for p in packages if p['fragile'])
express_count = sum(1 for p in packages if p['express'])
weight_values = [p['weight'] for p in packages]

modifier = calculate_priority_modifier(weight_values)
traffic_status = 'moderate'
weather = 'rain'
efficiency = get_route_efficiency(traffic_status, weather)

# Execution point Y
final_adjustment = 0
if fragile_count > 1 and express_count >= 1:
    final_adjustment = modifier + efficiency
elif fragile_count == 1 or not express_count:
    final_adjustment = modifier - efficiency
else:
    final_adjustment = modifier * efficiency

# Short-circuit evaluation with logical operations
if fragile_count and (express_count or efficiency > 20):
    final_adjustment += 5

print(f"Result: {final_adjustment}")