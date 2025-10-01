import math
from collections import defaultdict

def complex_function(a, b, c):
    if a > b:
        return (a ** 2) - (b * c)
    elif b > c:
        return (b ** 3) + (a / c) if c != 0 else 0
    else:
        return math.sqrt(abs(a - b)) * c

data = [
    {'x': 5, 'y': 3, 'z': 2},
    {'x': 10, 'y': 20, 'z': 5},
    {'x': -4, 'y': 7, 'z': 3}
]

transformed_data = []
for item in data:
    transformed_item = {
        'u': item['x'] * item['y'],
        'v': item['y'] + item['z'] if item['x'] > 0 else item['y'] - item['z'],
        'w': complex_function(item['x'], item['y'], item['z'])
    }
    transformed_data.append(transformed_item)

aggregated = defaultdict(list)
for item in transformed_data:
    aggregated['u_vals'].append(item['u'])
    aggregated['v_vals'].append(item['v'])
    aggregated['w_vals'].append(item['w'])

# Perform nested list comprehensions and filtering
u_filtered = [x for x in aggregated['u_vals'] if x % 2 == 0]
v_filtered = [x for x in aggregated['v_vals'] if x > 0]
w_filtered = [x for x in aggregated['w_vals'] if isinstance(x, (int, float)) and not math.isnan(x)]

# Bitwise and mathematical operations
bitwise_result = (u_filtered[0] & v_filtered[0]) | (int(w_filtered[0]) ^ u_filtered[-1])
math_result = math.log(abs(bitwise_result)) if bitwise_result != 0 else 1

# Final calculation step
result_value = int(math_result * len(u_filtered) + sum(v_filtered) - max(w_filtered))

print(f"Result: {result_value}")