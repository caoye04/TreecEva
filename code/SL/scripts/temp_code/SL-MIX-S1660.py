def encode_reading(value):
    return hash(str(value)) % 1000

def transform_sensor_data(data_points):
    processed = []
    for point in data_points:
        if point > 0 and (point % 2 == 0 or point > 50):
            transformed = encode_reading(point) if point <= 100 else encode_reading(point * 2)
            processed.append(transformed)
        else:
            processed.append(0)
    return processed

class SensorDecoder:
    def __init__(self, factor=10):
        self.factor = factor
    
    def decode(self, values):
        return sum(v * self.factor for v in values if v != 0) + (len(values) if any(v != 0 for v in values) else 0)

sensor_readings = [42, -5, 73, 102, 0, 205, 18]
processed_data = transform_sensor_data(sensor_readings)
decoder = SensorDecoder(7)
encoded_output = decoder.decode(processed_data)
print(f'Result: {encoded_output}')