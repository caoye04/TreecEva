from collections import deque
import math

class WeatherStationNode:
    def __init__(self, station_id):
        self.station_id = station_id
        self.next = None
        self.prev = None

def create_circular_station_network(station_count):
    if station_count <= 0:
        return None
    
    head = WeatherStationNode(1)
    current = head
    
    for i in range(2, station_count + 1):
        new_node = WeatherStationNode(i)
        current.next = new_node
        new_node.prev = current
        current = new_node
    
    # Make it circular
    current.next = head
    head.prev = current
    
    return head

def compute_spatial_variance(readings):
    n = len(readings)
    if n == 0:
        return 0
    mean = sum(readings) / n
    variance = sum((x - mean) ** 2 for x in readings) / n
    return variance

def main():
    # Initialize station network
    station_network = create_circular_station_network(7)
    
    # Simulated sensor readings with bitwise-encoded metadata
    raw_readings = [0b11010110, 0b10111001, 0b01101110, 0b11100011, 0b10011101, 0b01010011, 0b11110000]
    
    # Process readings through stack-based calculation engine
    calculation_stack = deque()
    
    # Apply bitwise transformations to extract temperature component
    processed_temps = []
    for reading in raw_readings:
        # Extract temperature bits (middle 4 bits)
        temp_component = (reading >> 2) & 0b1111
        # Apply correction using XOR with station ID
        corrected_temp = temp_component ^ ((reading & 0b11) + 1)
        processed_temps.append(corrected_temp)
        calculation_stack.append(corrected_temp)
    
    # Perform stack-based calculations
    calculation_results = []
    while len(calculation_stack) > 1:
        a = calculation_stack.pop()
        b = calculation_stack.pop()
        # Combine using bitwise OR and arithmetic mean
        combined = (a | b) + (a + b) // 2
        calculation_results.append(combined)
        if len(calculation_stack) > 0:
            calculation_stack.appendleft(combined)
    
    # Statistical normalization
    temp_variance = compute_spatial_variance(processed_temps)
    temp_mean = sum(processed_temps) / len(processed_temps)
    
    # Calculate anomaly score using geometric properties
    # Treat station IDs as points on a circle and compute angular distances
    angular_distances = []
    current_station = station_network
    for _ in range(7):
        next_station = current_station.next
        # Angular distance between adjacent stations
        angle_diff = abs(next_station.station_id - current_station.station_id)
        # Normalize by circle circumference
        normalized_angle = (angle_diff * 360) / 7
        angular_distances.append(normalized_angle)
        current_station = next_station
    
    angle_variance = compute_spatial_variance(angular_distances)
    
    # Final anomaly score computation
    # Combine temperature statistics with spatial geometry using bitwise operations
    temp_factor = int(temp_variance) & 0xFF
    spatial_factor = int(angle_variance) << 2
    
    # Compute final normalized anomaly score
    raw_anomaly = (temp_factor ^ spatial_factor) + int(temp_mean)
    normalized_anomaly_score = (raw_anomaly * 100) // (int(temp_variance) + int(angle_variance) + 1)
    
    print(f"Result: {normalized_anomaly_score}")

if __name__ == "__main__":
    main()