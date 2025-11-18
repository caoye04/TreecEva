class SensorNode:
    def __init__(self, sensor_id, calibration_value):
        self.sensor_id = sensor_id
        self.calibration_value = calibration_value
        self.next = None

def process_calibration_sequence(head):
    current = head
    accumulator = 0
    
    while current and current.calibration_value > 0:
        sensor_type = current.sensor_id % 4
        
        match sensor_type:  # Python 3.10+ match statement (switch/case)
            case 0:  # Temperature sensor
                transformed = (current.calibration_value ** 2) & 0xFF
            case 1:  # Pressure sensor
                transformed = (current.calibration_value << 2) | 0x0F
            case 2:  # Humidity sensor
                transformed = ~(current.calibration_value ^ 0xAA) & 0xFF
            case 3:  # Light sensor
                transformed = (current.calibration_value + 17) % 256
            case _:  # Default case
                transformed = current.calibration_value
        
        # Short-circuit evaluation in conditional
        if transformed > 0 and (transformed & 0x80) == 0:
            accumulator ^= transformed
        elif transformed <= 0 or (transformed & 0x40) != 0:
            accumulator |= transformed
        
        current = current.next
    
    return accumulator

def create_sensor_chain():
    # Creating linked list with list comprehension
    sensors = [SensorNode(i, val) for i, val in enumerate([42, -5, 128, 63, 200])]
    
    # Linking nodes
    for i in range(len(sensors)-1):
        sensors[i].next = sensors[i+1]
    
    return sensors[0] if sensors else None

# Main execution
sensor_chain_head = create_sensor_chain()
final_checksum = process_calibration_sequence(sensor_chain_head)
print(f"Result: {final_checksum}")