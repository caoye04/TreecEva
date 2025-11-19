from functools import reduce
import math

class FixedPointContext:
    def __init__(self, precision=3):
        self.precision = precision
        self.multiplier = 10 ** precision
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
    
    def quantize(self, value):
        return round(value * self.multiplier) / self.multiplier

def compute_weighted_sum(readings_batch):
    weights = [0.1, 0.3, 0.2, 0.4]
    return sum(r * w for r, w in zip(readings_batch, weights))

# Sensor data batches
sensor_data = [
    [23.4567, 12.7891, 34.5678, 45.6789],
    [11.1111, 22.2222, 33.3333, 44.4444],
    [55.5555, 66.6666, 77.7777, 88.8888]
]

with FixedPointContext(precision=2) as fp_ctx:
    processed_batches = list(map(lambda batch: [fp_ctx.quantize(x) for x in batch], sensor_data))
    weighted_sums = list(map(compute_weighted_sum, processed_batches))
    aggregated_signal = reduce(lambda acc, val: fp_ctx.quantize(acc + math.sqrt(val)), weighted_sums, 0.0)

print(f"Result: {aggregated_signal}")