import math
from contextlib import contextmanager

def log_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper

class StateMachine:
    def __init__(self):
        self.state = 'IDLE'
    
    @log_decorator
    def process(self, input_signal):
        if self.state == 'IDLE' and input_signal > 0:
            self.state = 'ACTIVE'
            return 1
        elif self.state == 'ACTIVE':
            if input_signal == 0:
                self.state = 'LATCHED'
                return 2
            else:
                return (input_signal ** 2) % 7
        elif self.state == 'LATCHED':
            if input_signal < 0:
                self.state = 'ERROR'
                return -1
            else:
                return int(math.log(input_signal + 1)) if input_signal > 0 else 0
        else:  # ERROR state
            return 0

@contextmanager
def circuit_context():
    sm = StateMachine()
    try:
        yield sm
    finally:
        pass

signals = [3, -1, 5, 0, 2, -3]
circuit_output = 0

with circuit_context() as machine:
    for i, sig in enumerate(signals):
        intermediate = machine.process(sig)
        if i % 2 == 0:
            circuit_output = circuit_output | intermediate
        else:
            circuit_output = circuit_output & (intermediate ^ ((sig * 3) % 5))
        
        # Short-circuit evaluation check
        if circuit_output > 10 or (circuit_output < 0 and machine.state != 'ERROR'):
            circuit_output = circuit_output ^ 0xF

print(f"Result: {circuit_output}")