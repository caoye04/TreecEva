import math

class ComputationTracker:
    def __init__(self):
        self.depth = 0
    
    def __enter__(self):
        self.depth += 1
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.depth -= 1

def memoize(func):
    cache = {}
    def wrapper(n, strengths):
        if n not in cache:
            cache[n] = func(n, strengths)
        return cache[n]
    return wrapper

@memoize
def calculate_node_strength(node_id, strengths):
    if node_id <= 1:
        return 100.0
    
    with ComputationTracker() as tracker:
        if tracker.depth > 3:
            return 0.0
        
        parent1_strength = calculate_node_strength(node_id - 1, strengths)
        parent2_strength = calculate_node_strength(node_id - 2, strengths)
        
        # Exponential decay factor based on node distance
        decay_factor = math.exp(-0.1 * node_id)
        
        # Logarithmic interference from previous computations
        if parent1_strength > 0 and parent2_strength > 0:
            interference = math.log(parent1_strength + parent2_strength)
        else:
            interference = 0
        
        # Combined calculation with bitwise adjustment
        raw_strength = (parent1_strength * decay_factor) + (parent2_strength / 2.0) - interference
        adjusted_strength = int(raw_strength) & 0xFF  # Keep only lower 8 bits
        
        strengths[node_id] = adjusted_strength
        return adjusted_strength

network_strengths = {}
calculate_node_strength(10, network_strengths)
final_signal_strength = network_strengths.get(10, 0)
print(f"Result: {final_signal_strength}")