import heapq
from collections import deque

def process_vehicles():
    # State machine for traffic signal
    signal_states = {'RED': 0, 'YELLOW': 1, 'GREEN': 2}
    current_state = 'RED'
    
    # Queue for vehicle arrival order
    vehicle_queue = deque([5, 5, 2, 8, 3])
    
    # Heap for earliest departure times
    departure_heap = [12, 7, 9, 4, 15]
    heapq.heapify(departure_heap)
    
    # Lambda to calculate priority based on vehicle type and wait time
    calc_priority = lambda v, t: (v * 2) + (t % 5)
    
    # Process vehicles using functional pipeline
    waiting_vehicles = list(map(lambda v: calc_priority(v, heapq.heappop(departure_heap)), vehicle_queue))
    
    # Stack for signal transition history
    transition_stack = []
    
    # Simulate signal transitions
    for i in range(len(waiting_vehicles)):
        priority = waiting_vehicles[i]
        
        # Switch-like state transition logic
        if current_state == 'RED' and priority > 10:
            current_state = 'GREEN'
            transition_stack.append(2)
        elif current_state == 'GREEN' and priority <= 10:
            current_state = 'YELLOW'
            transition_stack.append(1)
        elif current_state == 'YELLOW':
            current_state = 'RED'
            transition_stack.append(0)
    
    # Calculate final signal priority
    signal_priority = sum(transition_stack) * len(heapq.nsmallest(3, departure_heap))
    
    return signal_priority

signal_priority = process_vehicles()
print(f"Result: {signal_priority}")