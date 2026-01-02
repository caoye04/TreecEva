from collections import defaultdict

def find_equilibrium(sequence):
    total_sum = sum(sequence)
    left_sum = 0
    for i, value in enumerate(sequence):
        total_sum -= value
        if left_sum == total_sum:
            return i
        left_sum += value
    return -1

# Simulate sensor weight readings along a beam
class SensorArray:
    def __init__(self, readings):
        self.readings = readings

    def get_readings(self):
        return self.readings

# Irrelevant helper (minimal distraction)
def normalize(data):
    max_val = max(data)
    return [x / max_val for x in data]

# Main data: weights at positions 0 to 5
weights = [2, 3, 1, 4, 2, 4]
sensor_net = SensorArray(weights)
data = sensor_net.get_readings()

# Key computation
equilibrium_point = find_equilibrium(weights)

# Output result
print(f"Result: {equilibrium_point}")