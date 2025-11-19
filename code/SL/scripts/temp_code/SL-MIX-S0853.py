def encode_priority(weight, distance, urgency):
    return (weight << 4) ^ (distance << 2) ^ urgency

def decode_priority(encoded):
    urgency = encoded & 0b11
    distance = (encoded >> 2) & 0b1111
    weight = (encoded >> 6) & 0b111111
    return weight, distance, urgency

packages = [
    (15, 8, 3),   # (weight, distance, urgency)
    (22, 5, 1),
    (10, 12, 2),
    (30, 3, 3),
    (18, 7, 2),
    (25, 4, 1),
    (12, 10, 3),
    (20, 6, 2),
    (16, 9, 1),
    (28, 2, 3)
]

# Encode priorities using lambda
priority_encoder = lambda p: encode_priority(p[0], p[1], p[2])
encoded_packages = [(priority_encoder(pkg), pkg[0]) for pkg in packages]  # (priority, weight)

# Sort by priority (descending)
encoded_packages.sort(key=lambda x: x[0], reverse=True)

# Greedy loading with context manager for tracking
class Truck:
    def __init__(self, capacity):
        self.capacity = capacity
        self.load = 0
        self.priority_sum = 0
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
    
    def load_package(self, priority, weight):
        if self.load + weight <= self.capacity:
            self.load += weight
            self.priority_sum += priority
            return True
        return False

with Truck(100) as truck:
    for priority, weight in encoded_packages:
        truck.load_package(priority, weight)
    
    target_result = truck.priority_sum

print(f"Target result: {target_result}")