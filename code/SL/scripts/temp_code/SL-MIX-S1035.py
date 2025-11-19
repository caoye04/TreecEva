from functools import reduce
from math import gcd

class NetworkNode:
    def __init__(self, operation, value):
        self.operation = operation
        self.value = value
    
    def process(self, ttl):
        if self.operation == 'add':
            return ttl + self.value
        elif self.operation == 'subtract':
            return ttl - self.value
        elif self.operation == 'multiply':
            return ttl * self.value
        elif self.operation == 'divide':
            return ttl // self.value if self.value != 0 else ttl
        elif self.operation == 'mod':
            return ttl % self.value if self.value != 0 else ttl
        elif self.operation == 'gcd':
            return gcd(ttl, self.value)
        else:
            return ttl

# Create network nodes with different operations
network_topology = [
    NetworkNode('add', 15),
    NetworkNode('multiply', 2),
    NetworkNode('subtract', 10),
    NetworkNode('mod', 7),
    NetworkNode('gcd', 12)
]

# Initial packet TTL
initial_ttl = 24

# Process packet through network using functional approach
final_ttl = reduce(lambda ttl, node: node.process(ttl), network_topology, initial_ttl)

# Calculate statistics about the network operations
operation_values = [node.value for node in network_topology]
prime_operation_values = [x for x in operation_values if all(x % i != 0 for i in range(2, int(x**0.5)+1)) and x > 1]
composite_count = len(operation_values) - len(prime_operation_values) - operation_values.count(1)

# Adjust final TTL based on network statistics
if composite_count > 2:
    final_ttl += sum(prime_operation_values)
else:
    final_ttl -= len(network_topology)

print(f'Result: {final_ttl}')