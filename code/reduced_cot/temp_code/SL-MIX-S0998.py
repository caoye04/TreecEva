from dataclasses import dataclass
from typing import List
from contextlib import contextmanager
import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def fibonacci_sequence(start1, start2, count):
    seq = [start1, start2]
    for _ in range(count - 2):
        seq.append(seq[-1] + seq[-2])
    return seq

def prime_factors(n):
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors

class PacketProcessor:
    def __init__(self):
        self.state = 'IDLE'
        self.scheduling_priority = 0
        
    def process_packet(self, packet_id):
        # State machine transitions
        if self.state == 'IDLE':
            if packet_id % 2 == 0:
                self.state = 'EVEN_PROCESSING'
            else:
                self.state = 'ODD_PROCESSING'
        elif self.state == 'EVEN_PROCESSING':
            if is_prime(packet_id):
                self.state = 'PRIME_HANDLING'
            else:
                self.state = 'COMPOSITE_HANDLING'
        elif self.state == 'ODD_PROCESSING':
            if len(prime_factors(packet_id)) > 2:
                self.state = 'SEMI_PRIME'
            else:
                self.state = 'HIGH_PRIORITY'
        
        # Dynamic programming calculation based on state
        factors = prime_factors(packet_id)
        unique_factors = list(set(factors))
        
        if self.state == 'PRIME_HANDLING':
            self.scheduling_priority += sum(unique_factors) * len(factors)
        elif self.state == 'COMPOSITE_HANDLING':
            product = 1
            for f in unique_factors:
                product *= f
            self.scheduling_priority += product
        elif self.state == 'SEMI_PRIME':
            self.scheduling_priority += lcm(factors[0], factors[-1]) if len(factors) > 1 else factors[0]
        elif self.state == 'HIGH_PRIORITY':
            self.scheduling_priority += max(factors) ** 2
        else:  # IDLE case
            self.scheduling_priority += packet_id

@contextmanager
def packet_processing_context():
    processor = PacketProcessor()
    try:
        yield processor
    finally:
        # Cleanup if needed
        pass

# Main execution
packet_ids = fibonacci_sequence(89, 144, 12)

with packet_processing_context() as processor:
    for pid in packet_ids:
        processor.process_packet(pid)
    
    result = processor.scheduling_priority

print(f"Result: {result}")