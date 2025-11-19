from collections import defaultdict

class Hub:
    def __init__(self, capacity):
        self.capacity = capacity
        self.subhubs = []

def calculate_max_capacity(hub):
    if not hub.subhubs:
        return hub.capacity
    max_subcapacity = max(calculate_max_capacity(sub) for sub in hub.subhubs)
    return hub.capacity + max_subcapacity

# Construct warehouse hierarchy
hq = Hub(20)
regional_1 = Hub(15)
regional_2 = Hub(12)
local_a = Hub(8)
local_b = Hub(10)
local_c = Hub(5)
local_d = Hub(7)

hq.subhubs = [regional_1, regional_2]
regional_1.subhubs = [local_a, local_b]
regional_2.subhubs = [local_c, local_d]

# Use dynamic programming with memoization
cache = defaultdict(lambda: -1)

def dp_max_capacity(node):
    if cache[node] != -1:
        return cache[node]
    if not node.subhubs:
        cache[node] = node.capacity
        return cache[node]
    max_val = node.capacity + max(dp_max_capacity(child) for child in node.subhubs)
    cache[node] = max_val
    return max_val

max_capacity = dp_max_capacity(hq)
print(f"Result: {max_capacity}")