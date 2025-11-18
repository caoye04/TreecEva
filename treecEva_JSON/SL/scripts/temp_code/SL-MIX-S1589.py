import heapq
from dataclasses import dataclass
from typing import List, Tuple

def recursive_filter(data: List[int], threshold: int, depth: int = 0) -> List[int]:
    if depth >= 3 or not data:
        return data
    
    filtered = []
    for i, val in enumerate(data):
        if i % 2 == 0:
            if val > threshold:
                filtered.append(val // 2)
            else:
                filtered.append(val * 2)
        else:
            filtered.append(val)
    
    # Recursive call with modified data
    return recursive_filter(filtered[:-1], threshold + 1, depth + 1)

def process_seismic_data(raw_readings: List[int]) -> int:
    # Stage 1: Apply recursive filter
    filtered_data = recursive_filter(raw_readings.copy(), 10)
    
    # Stage 2: Priority queue processing
    priority_queue = []
    for i, reading in enumerate(filtered_data):
        priority_value = reading * (-1 if i % 2 == 0 else 1)
        heapq.heappush(priority_queue, (priority_value, reading))
    
    # Stage 3: Extract and transform top elements
    extracted_values = []
    for _ in range(min(3, len(priority_queue))):
        _, value = heapq.heappop(priority_queue)
        transformed = value ** 2 if value < 0 else value // 2
        extracted_values.append(transformed)
    
    # Stage 4: Conditional aggregation
    aggregate = 0
    for i, val in enumerate(extracted_values):
        match i:
            case 0:
                aggregate += val * 3
            case 1:
                aggregate -= val
            case 2:
                aggregate += val // 2
            case _:
                aggregate += val
    
    return aggregate

# Main execution
seismic_readings = [15, -8, 22, 4, -16, 9, 30, -5]
final_amplitude_sum = process_seismic_data(seismic_readings)
print(f"Result: {final_amplitude_sum}")