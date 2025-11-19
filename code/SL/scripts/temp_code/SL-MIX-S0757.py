from collections import deque
import functools

def timing_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        wrapper.execution_count += 1
        return result
    wrapper.execution_count = 0
    return wrapper

@timing_decorator
def process_signal(value):
    return value * 2

signal_queue = deque([3, 7, 1, 9, 4])
processing_stack = []
propagation_delay = 0

while signal_queue:
    current_signal = signal_queue.popleft()
    if current_signal > 5:
        processed = process_signal(current_signal)
        processing_stack.append(processed)
    else:
        if processing_stack:
            stacked_value = processing_stack.pop()
            if stacked_value % 3 == 0:
                propagation_delay += stacked_value // 3
            else:
                propagation_delay += stacked_value % 3
        else:
            break

if processing_stack:
    remaining = processing_stack.pop()
    propagation_delay += remaining if remaining < 10 else remaining // 2

print(f"Result: {propagation_delay}")