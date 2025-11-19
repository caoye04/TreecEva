from collections import defaultdict

def call_counter(func):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper

class SensorNetwork:
    def __init__(self):
        self.signal_cache = {}
    
    @call_counter
    def propagate_signal(self, node_id, depth):
        if (node_id, depth) in self.signal_cache:
            return self.signal_cache[(node_id, depth)]
        
        # Base cases
        if depth == 0:
            return 100
        if node_id <= 0:
            return 0
            
        # Switch-like behavior for sensor types
        sensor_type = node_id % 4
        if sensor_type == 0:  # Omnidirectional
            result = self.propagate_signal(node_id-1, depth-1) * 0.8
        elif sensor_type == 1:  # Directional
            result = self.propagate_signal(node_id-2, depth-1) + self.propagate_signal(node_id-1, depth-1)
        elif sensor_type == 2:  # Phased array
            result = max(self.propagate_signal(node_id-1, depth-1), self.propagate_signal(node_id-3, depth-1)) * 0.9
        else:  # Adaptive
            result = (self.propagate_signal(node_id-1, depth-1) + self.propagate_signal(node_id-2, depth-1)) / 2
            
        self.signal_cache[(node_id, depth)] = result
        return result

# Initialize network
network = SensorNetwork()
fibonacci_sequence = [1, 1]
for i in range(2, 10):
    fibonacci_sequence.append(fibonacci_sequence[i-1] + fibonacci_sequence[i-2])

# Calculate signal pattern
signal_pattern = 0
active_sensors = {2, 3, 5, 8, 13}
for idx, fib_num in enumerate(fibonacci_sequence[:6]):
    if fib_num in active_sensors:
        signal_contribution = network.propagate_signal(fib_num, idx)
        signal_pattern += signal_contribution
    else:
        signal_pattern -= fib_num * 2

# Apply final transformation
transform_func = lambda x: x * 1.5 if x > 50 else x + 25
final_signal_strength = int(transform_func(signal_pattern))

print(f"Result: {final_signal_strength}")