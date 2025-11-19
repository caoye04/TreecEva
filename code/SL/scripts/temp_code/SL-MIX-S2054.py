import math

def process_sensor_data(readings):
    transformed = []
    for idx, value in enumerate(readings):
        if value > 0:
            log_val = math.log(value)
            exp_component = math.exp(idx % 3)
            mod_result = int(log_val * exp_component) % 7
            transformed.append(mod_result)
        else:
            transformed.append(0)
    return transformed

def calculate_metric(transformed_values):
    cumulative = 0
    for i, val in enumerate(transformed_values):
        weight = (i + 1) ** 2
        adjusted = val * weight if val % 2 == 0 else val // 2
        cumulative += adjusted
    return cumulative

# Sensor readings from 5 different sources
sensor_readings = [math.e, math.e**2, 0, math.e**3, math.e**4]

# Process the data through two transformation stages
processed_data = process_sensor_data(sensor_readings)
final_metric = calculate_metric(processed_data) if len(processed_data) > 3 else -1

print(f"Result: {final_metric}")