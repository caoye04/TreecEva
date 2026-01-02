from collections import Counter

def calculate_score(data, limits):
    above_limit = [val for val in data if val > limits[0]]
    count_map = Counter(above_limit)
    total = sum(count_map.values())
    penalty = len([x for x in data if x < 0])
    scaling_factor = 1.5
    adjusted = total * scaling_factor - penalty * 2
    return int(adjusted)

# Sensor readings in degrees Celsius
temperatures = [23, 35, 18, 40, -5, 33, 41, -2, 39]
thresholds = [30]

# Irrelevant auxiliary variable (mild distraction)
days_of_week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']

result = calculate_score(temperatures, thresholds)
print(f"Result: {result}")