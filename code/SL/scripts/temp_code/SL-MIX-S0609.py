from collections import namedtuple

def process_sensor_readings():
    # Define sensor reading structure
    SensorReading = namedtuple('SensorReading', ['type_id', 'value'])
    
    # Simulated sensor data
    raw_readings = [
        SensorReading(type_id=3, value=142),
        SensorReading(type_id=1, value=87),
        SensorReading(type_id=2, value=205),
        SensorReading(type_id=3, value=96)
    ]
    
    # Process readings with modular adjustments
    adjusted_values = [
        (reading.value * 3 + 7) % 256 if reading.type_id == 1
        else (reading.value + 19) % 256 if reading.type_id == 2
        else (reading.value ** 2 - 4) % 256
        for reading in raw_readings
    ]
    
    # Custom encoding function
    def custom_encode(val):
        if val < 64:
            return val + 192
        elif val < 128:
            return val + 64
        elif val < 192:
            return val - 64
        else:
            return val - 192
    
    # Apply encoding to adjusted values
    encoded_sequence = [custom_encode(v) for v in adjusted_values]
    
    # Final accumulation with modular arithmetic
    encoded_result = 0
    for i, enc_val in enumerate(encoded_sequence):
        match i % 4:
            case 0:
                encoded_result = (encoded_result + enc_val * 2) % 256
            case 1:
                encoded_result = (encoded_result ^ enc_val) % 256
            case 2:
                encoded_result = (encoded_result - enc_val) % 256
            case 3:
                encoded_result = (encoded_result + enc_val) % 256
    
    return encoded_result

# Execute processing and print result
final_value = process_sensor_readings()
print(f"Result: {final_value}")