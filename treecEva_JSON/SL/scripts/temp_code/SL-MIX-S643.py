from math import log2
from collections import namedtuple

def modular_power(base, exp, mod):
    return pow(base, exp, mod)

def fibonacci_delay(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, (a + b) % 97
    return b

def calculate_cumulative_delay(sensor_positions, depth=0):
    if not sensor_positions or depth > 3:
        return 0
    
    total = 0
    for pos in sensor_positions:
        x, y = pos
        distance_squared = x**2 + y**2
        log_component = int(log2(distance_squared + 1))
        fib_adjustment = fibonacci_delay(log_component)
        mod_exp_result = modular_power(log_component, 3, 17)
        total += (mod_exp_result * fib_adjustment) % 13
    
    # Recursive call with modified positions
    next_positions = [(x//2, y//2) for x, y in sensor_positions if x > 0 and y > 0]
    return (total + calculate_cumulative_delay(next_positions, depth + 1)) % 97

SensorCoord = namedtuple('SensorCoord', ['x', 'y'])
sensor_network = {SensorCoord(8, 6), SensorCoord(5, 12), SensorCoord(15, 8)}

# Convert to list of tuples for processing
positions_list = [(coord.x, coord.y) for coord in sensor_network]
final_delay = calculate_cumulative_delay(positions_list)
print(f'Result: {final_delay}')