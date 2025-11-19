import math
import re

def log_transform_logger(func):
    def wrapper(packet_intensity):
        result = func(packet_intensity)
        wrapper.log.append(result)
        return result
    wrapper.log = []
    return wrapper

@log_transform_logger
def scale_packet(intensity):
    return math.log(intensity) if intensity > 0 else 0

packet_data = [math.exp(3), math.exp(2), 0, math.exp(5)]
thresh_pattern = re.compile(r'^[0-9]*\.?[0-9]+$')

scaled_values = [scale_packet(p) for p in packet_data]
valid_scaled = [v for v in scaled_values if thresh_pattern.match(str(v))]

final_intensity = sum(valid_scaled) + math.exp(1)  # Add e for calibration
print(f"Result: {final_intensity}")