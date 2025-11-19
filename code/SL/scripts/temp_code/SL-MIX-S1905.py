from collections import deque
from functools import reduce
from itertools import combinations

def process_shipment_id(shipment_id, station_id):
    # Apply modular arithmetic transformation
    transformed = (shipment_id * 3 + station_id * 7) % 13
    
    # Apply combinatorial operation
    if transformed > 0:
        comb_count = len(list(combinations(range(transformed), min(2, transformed))))
        transformed = (transformed + comb_count) % 11
    
    return transformed

def quality_control_process(shipments):
    station_queue = deque([1, 2, 3, 4])  # Stations in order
    processed_stack = []  # Stack for processed identifiers
    
    for shipment in shipments:
        temp_id = shipment
        stations_copy = deque(station_queue)
        
        # Process through each station
        while stations_copy:
            station = stations_copy.popleft()
            temp_id = process_shipment_id(temp_id, station)
        
        # Push to stack
        processed_stack.append(temp_id)
    
    # Calculate final identifier using reduce
    final_identifier = reduce(lambda x, y: (x + y) % 17, processed_stack, 0)
    return final_identifier

# Initial shipment identifiers
shipments_batch = [15, 22, 8, 31]

# Execute the quality control process
final_identifier = quality_control_process(shipments_batch)
print(f"Result: {final_identifier}")