import math

call_tracker = set()

def track_calls(func):
    def wrapper(*args, **kwargs):
        call_tracker.add(func.__name__)
        return func(*args, **kwargs)
    return wrapper

@track_calls
def process_signal(value):
    if value > 0 and math.log(value) > 1:
        return math.exp(math.log(value) * 0.5)
    return value

signal_pool = {4, 9, 16, 25, 36}
active_signals = frozenset({9, 16, 25})
processed_values = []

for sig in signal_pool:
    if sig in active_signals and sig % 2 != 0:
        processed_values.append(process_signal(sig))
    elif sig not in active_signals or process_signal(sig) > 10:
        processed_values.append(sig * 2)
    else:
        processed_values.append(0)

final_metric = sum(processed_values) + len(call_tracker)
print(f'Result: {final_metric}')