import math

def exponential_smoothing(alpha):
    def decorator(func):
        def wrapper(*args, **kwargs):
            raw_value = func(*args, **kwargs)
            # Simulate stateful smoothing with closure
            if not hasattr(wrapper, 'smoothed'):
                wrapper.smoothed = raw_value
            else:
                wrapper.smoothed = alpha * raw_value + (1 - alpha) * wrapper.smoothed
            return wrapper.smoothed
        return wrapper
    return decorator

class ResourceManager:
    def __enter__(self):
        self.resources = []
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.resources.clear()

def calibrate_reading(raw_temp, offset):
    return raw_temp + math.log(offset) if offset > 0 else raw_temp

@exponential_smoothing(0.3)
def process_sensor_data(temp, offset):
    calibrated = calibrate_reading(temp, offset)
    return calibrated ** 1.5 if calibrated > 0 else calibrated

sensor_readings = [
    (25.4, 1.2),
    (26.1, 1.1),
    (24.8, 1.3),
    (27.3, 0.9),
    (25.9, 1.0)
]

weights = [0.1, 0.2, 0.3, 0.25, 0.15]

with ResourceManager() as rm:
    smoothed_values = [process_sensor_data(temp, offset) for temp, offset in sensor_readings]
    final_aggregate = sum(val * weight for val, weight in zip(smoothed_values, weights))
    rm.resources.append(final_aggregate)

print(f"Result: {final_aggregate}")