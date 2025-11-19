from dataclasses import dataclass
from typing import NamedTuple
import math

class FibonacciProcessorState(NamedTuple):
    current_state: str
    fib_index: int
    last_prime_fib_pos: int
    prime_gap_count: int
    max_prime_gap: int

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Initialize state machine
state = FibonacciProcessorState(
    current_state="SEARCHING",
    fib_index=2,
    last_prime_fib_pos=0,
    prime_gap_count=0,
    max_prime_gap=0
)

fib_count = 0

while fib_count < 20:
    current_fib = fibonacci(state.fib_index)
    
    if state.current_state == "SEARCHING":
        if is_prime(current_fib):
            # Found a prime, transition to COUNTING
            state = FibonacciProcessorState(
                current_state="COUNTING",
                fib_index=state.fib_index + 1,
                last_prime_fib_pos=state.fib_index,
                prime_gap_count=0,
                max_prime_gap=state.max_prime_gap
            )
        else:
            # Still searching, continue
            state = FibonacciProcessorState(
                current_state="SEARCHING",
                fib_index=state.fib_index + 1,
                last_prime_fib_pos=state.last_prime_fib_pos,
                prime_gap_count=state.prime_gap_count,
                max_prime_gap=state.max_prime_gap
            )
    elif state.current_state == "COUNTING":
        if is_prime(current_fib):
            # Found another prime, calculate gap
            gap = state.fib_index - state.last_prime_fib_pos
            new_max = max(state.max_prime_gap, gap)
            # Reset counting with new prime position
            state = FibonacciProcessorState(
                current_state="COUNTING",
                fib_index=state.fib_index + 1,
                last_prime_fib_pos=state.fib_index,
                prime_gap_count=0,
                max_prime_gap=new_max
            )
        else:
            # Continue counting gap
            state = FibonacciProcessorState(
                current_state="COUNTING",
                fib_index=state.fib_index + 1,
                last_prime_fib_pos=state.last_prime_fib_pos,
                prime_gap_count=state.prime_gap_count + 1,
                max_prime_gap=state.max_prime_gap
            )
    
    fib_count += 1

print(f"Result: {state.max_prime_gap}")