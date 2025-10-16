import heapq
import math

# Simulated packet sizes in kilobytes
packet_sizes = [12.5, 8.75, 16.2, 22.8, 5.4, 19.1, 7.9]

# Process packet sizes using floating point operations
processed_sizes = list(map(lambda x: math.sqrt(x) * 2.5, packet_sizes))

# Calculate checksum using modular arithmetic
checksum = 0
for size in processed_sizes:
    checksum = (checksum + int(size * 100)) % 97

# Priority values for key generation
priorities = [42, 18, 73, 29, 55]
heapq.heapify(priorities)

# Generate session key using heap operations and hash table
key_components = {}
for i in range(3):
    priority_val = heapq.heappop(priorities)
    key_components[f'comp_{i}'] = (priority_val * checksum) % 79

# Final session key calculation
session_key = sum(key_components.values()) % 1000

# Merge with additional configuration
config = {'offset': 127, 'modulus': 256}
final_config = {**key_components, **config}

# Apply final transformation
session_key = (session_key * final_config['offset']) % final_config['modulus']

print(f"Result: {session_key}")