from functools import reduce

def generate_lookup_table(size):
    return [reduce(lambda x, y: (x * 3 + y) % 1024, range(1, i+1), 1) for i in range(1, size+1)]

def binary_search_closest(arr, target):
    low, high = 0, len(arr) - 1
    closest = arr[0]
    while low <= high:
        mid = (low + high) // 2
        if abs(arr[mid] - target) < abs(closest - target):
            closest = arr[mid]
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return closest

def process_sensor_data(raw_reading):
    # Apply XOR with mask
    masked = raw_reading ^ 0b11010110101
    # Left shift by 3 positions
    shifted = masked << 3
    # Apply modular arithmetic
    modulated = shifted % 2048
    # Apply another XOR with different mask
    encoded_signal = modulated ^ 0b101010101010
    
    # The lookup table for binary search
    lookup = generate_lookup_table(100)
    
    # This would be used in actual implementation but we want value before this
    # matched_value = binary_search_closest(lookup, encoded_signal)
    
    return encoded_signal

# Sensor reading from device
sensor_raw_value = 1759

final_encoded = process_sensor_data(sensor_raw_value)
print(f"Result: {final_encoded}")