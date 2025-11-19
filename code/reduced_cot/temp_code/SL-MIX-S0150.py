from contextlib import contextmanager
from dataclasses import dataclass
from typing import List

def fibonacci_sequence(n: int) -> List[int]:
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    seq = [0, 1]
    for i in range(2, n):
        seq.append(seq[i-1] + seq[i-2])
    return seq

@contextmanager
def crypto_context(start_value: int):
    state = {'value': start_value, 'modifications': 0}
    try:
        yield state
    finally:
        state['value'] = 0
        state['modifications'] = 0

@dataclass
class CryptoTracker:
    prices: List[int]
    index: int = 0
    
    def get_current_price(self) -> int:
        if self.index < len(self.prices):
            val = self.prices[self.index]
            self.index += 1
            return val
        return 0

# Initialize components
prices_fib = fibonacci_sequence(12)[2:]  # Skip first two elements
tracker = CryptoTracker(prices_fib)
security_checksum = 0

with crypto_context(100) as ctx:
    for i in range(5):
        price = tracker.get_current_price()
        adjusted_price = price << 1  # Bitwise left shift
        
        if i % 2 == 0:
            ctx['value'] = (ctx['value'] ^ adjusted_price) & 0xFF  # XOR and mask
        else:
            ctx['value'] = (ctx['value'] + adjusted_price) & 0xFF  # Add and mask
        
        ctx['modifications'] += 1
    
    # Final checksum computation
    security_checksum = ctx['value'] ^ (ctx['modifications'] << 2)

print(f"Result: {security_checksum}")