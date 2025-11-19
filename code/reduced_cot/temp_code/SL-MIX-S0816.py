class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def sum_linked_list(head):
    total = 0
    current = head
    while current:
        total += current.val
        current = current.next
    return total

def process_sensor_data(raw_timestamps):
    # Create linked list from raw timestamps
    sensor_buffer = create_linked_list(raw_timestamps)
    
    # Calculate base delay as sum of all timestamps
    base_delay = sum_linked_list(sensor_buffer)
    
    # Apply correction factor using arithmetic operations
    correction_factor = (base_delay * 3 - 17) // 4
    
    # Apply secondary adjustment using modulo
    secondary_adjustment = (correction_factor + 5) % 7
    
    # Final compensation calculation
    final_compensation = (base_delay - correction_factor) * secondary_adjustment
    
    return final_compensation

# Sensor timestamp data (in milliseconds)
sensor_readings = [12, 28, 35, 44, 19]

# Process the sensor data
final_compensation = process_sensor_data(sensor_readings)
print(f"Result: {final_compensation}")