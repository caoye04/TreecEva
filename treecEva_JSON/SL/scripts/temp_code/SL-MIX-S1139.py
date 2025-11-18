def call_counter(func):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper

def sensor_metric(strength, duration):
    return strength * duration if strength > 0 else 0

@call_counter
def preprocess_signal(raw_signal):
    # Greedy selection: keep only positive signals above threshold
    threshold = 3
    return [s for s in raw_signal if s > threshold]

signal_data = [
    [-1, 5, 2, 8, 3],
    [10, -2, 4, 1],
    [0, 6, 7, -3, 9]
]

durations = [2, 3, 1, 4, 2]
processed_signals = [preprocess_signal(signal) for signal in signal_data]
metrics = [
    sum(sensor_metric(s, durations[i]) for i, s in enumerate(signal_group))
    for signal_group in processed_signals
]

# Sorting with ternary-based custom comparator
is_ascending = True
sorted_metrics = sorted(metrics, reverse=(False if is_ascending else True))

final_metric = (
    (sorted_metrics[0] + sorted_metrics[-1]) // 2
    if len(sorted_metrics) > 1 and preprocess_signal.calls > 0
    else 0
)

print(f"Result: {final_metric}")