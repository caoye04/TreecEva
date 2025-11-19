import math
from functools import wraps

def performance_monitor(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return round(math.log(abs(result) + 1), 2) if result != 0 else 0
    return wrapper

@performance_monitor
def signal_transform(data_points):
    adjusted = [x**2 - 2*x + 1 for x in data_points if x > 0]
    aggregated = sum(adjusted) / len(adjusted) if adjusted else 0
    return aggregated

class SignalProcessor:
    def __init__(self, signals):
        self.signals = signals
        self.metrics = []
    
    def process_all(self):
        for signal in self.signals:
            metric = signal_transform(signal)
            self.metrics.append(metric)
        return self.metrics

# Test data representing different signal patterns
acoustic_samples = [
    [1, -2, 3, -4, 5],
    [-1, -2, -3],
    [2, 2, 2, 2],
    [0, 4, -3, 7, -1, 2]
]

processor = SignalProcessor(acoustic_samples)
processed_metrics = processor.process_all()

# Calculate final evaluation metric
valid_metrics = [m for m in processed_metrics if m > 0]
mean_metric = sum(valid_metrics) / len(valid_metrics) if valid_metrics else 0
variance_components = [(m - mean_metric)**2 for m in valid_metrics]
metric_variance = sum(variance_components) / len(variance_components) if variance_components else 0

final_metric = int(math.exp(mean_metric + metric_variance))
print(f"Result: {final_metric}")