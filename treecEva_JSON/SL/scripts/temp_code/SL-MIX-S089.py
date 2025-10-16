import math
from collections import defaultdict

def calculate_angle_adjustment(sensor_readings):
    base_log = math.log(sum(sensor_readings) + 1)
    return round(base_log * 15.0)

def update_state(current_state, adjustment):
    state_transitions = {
        'NORTH': lambda adj: 'EAST' if adj > 0 else 'WEST',
        'EAST': lambda adj: 'SOUTH' if adj > 0 else 'NORTH',
        'SOUTH': lambda adj: 'WEST' if adj > 0 else 'EAST',
        'WEST': lambda adj: 'NORTH' if adj > 0 else 'SOUTH'
    }
    return state_transitions.get(current_state, lambda _: current_state)(adjustment)

sensor_data = [2, 4, 1, 3]
heading_states = defaultdict(int)
current_direction = 'NORTH'
final_heading_adjustment = 0

for i in range(len(sensor_data)):
    adjustment = calculate_angle_adjustment(sensor_data[:i+1])
    current_direction = update_state(current_direction, adjustment)
    heading_states[current_direction] += adjustment
    if i == len(sensor_data) - 1:
        final_heading_adjustment = heading_states[current_direction] + int(math.exp(adjustment % 3))

print(f"Result: {final_heading_adjustment}")