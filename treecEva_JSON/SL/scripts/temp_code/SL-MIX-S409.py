class SensorNode:
    def __init__(self, reading, next_node=None):
        self.reading = reading
        self.next = next_node

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def process_sensors(head, valid_range, exclusion_set):
    current = head
    filtered_readings = []
    
    while current and current.reading < 1000:  # Short-circuit protection
        reading = current.reading
        # Apply filtering logic with set operations and short-circuit evaluation
        if reading >= valid_range[0] and reading <= valid_range[1]:
            if reading not in exclusion_set and (reading % 2 == 0 or reading > 50):
                filtered_readings.append(reading)
        current = current.next
    
    # Deduplicate and sort for binary search
    unique_sorted = sorted(list(frozenset(filtered_readings)))
    
    # Find position of special marker value
    marker = 84
    position = binary_search(unique_sorted, marker)
    
    # Calculate final result based on position and list properties
    if position != -1 and len(unique_sorted) > 0:
        target_result = (position + 1) * sum(filter(lambda x: x < marker, unique_sorted))
    else:
        target_result = 0
    
    return target_result

# Initialize sensor linked list: 12 -> 84 -> 43 -> 84 -> 99 -> 12 -> 150 -> 200 -> ...
sensor_data = [12, 84, 43, 84, 99, 12, 150, 200, 75, 300, 84, 500]
head = None
for val in reversed(sensor_data):
    head = SensorNode(val, head)

# Define valid range and exclusion set
operational_range = (10, 250)
noise_signatures = frozenset([43, 99])

# Process sensors and get result
target_result = process_sensors(head, operational_range, noise_signatures)
print(f"Target result: {target_result}")