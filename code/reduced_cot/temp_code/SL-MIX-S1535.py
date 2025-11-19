from collections import deque
from contextlib import contextmanager

def transform_state(x):
    return x * 2 - 1

def adjust_state(x):
    return x + 3 if x < 10 else x - 2

class StateLogger:
    def __init__(self):
        self.log = []
    
    @contextmanager
    def log_transition(self, state):
        self.log.append(f"Entering: {state}")
        try:
            yield
        finally:
            self.log.append(f"Exiting: {state}")

states = deque([5, 8, 3, 9])
logger = StateLogger()
stack = []
intermediate_result = 0

while states:
    current = states.popleft()
    with logger.log_transition(current):
        modified = transform_state(current)
        corrected = adjust_state(modified)
        stack.append(corrected)

while stack:
    val = stack.pop()
    intermediate_result += val if val % 2 == 0 else val * 2

final_conformation_score = intermediate_result if intermediate_result > 20 else intermediate_result * 3
print(f"Result: {final_conformation_score}")