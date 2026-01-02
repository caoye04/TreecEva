import math
from collections import deque

def priority_calculator(weight_factor):
    def decorator(func):
        def wrapper(*args, **kwargs):
            base_value = func(*args, **kwargs)
            return base_value * weight_factor + 10
        return wrapper
    return decorator

class OperationLogger:
    def __enter__(self):
        self.log = []
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
    
    def record(self, operation):
        self.log.append(operation)

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

@priority_calculator(3)
def calculate_base_priority(items):
    return sum(items) % 7

shipment_stack = []
order_queue = deque()

with OperationLogger() as logger:
    # Process incoming shipments
    shipment_stack.append([5, 12, 8])
    logger.record("Pushed shipment 1")
    
    shipment_stack.append([3, 9, 15])
    logger.record("Pushed shipment 2")
    
    shipment_stack.append([7, 4, 11])
    logger.record("Pushed shipment 3")
    
    shipment_stack.append([2, 14, 6])
    logger.record("Pushed shipment 4")
    
    # Process outgoing orders
    order_queue.append((1, 20))
    logger.record("Queued order 1")
    
    order_queue.append((2, 25))
    logger.record("Queued order 2")
    
    order_queue.append((3, 30))
    logger.record("Queued order 3")
    
    # Calculate priorities
    priorities = []
    temp_stack = []
    
    # Pop all from stack and calculate priorities
    while shipment_stack:
        items = shipment_stack.pop()
        priority = calculate_base_priority(items)
        priorities.append(priority)
        temp_stack.append(priority)
    
    # Restore stack
    while temp_stack:
        shipment_stack.append(temp_stack.pop())
    
    # Process orders using queue
    processed_orders = 0
    while order_queue and processed_orders < 3:
        order_id, amount = order_queue.popleft()
        # Find matching priority using binary search
        sorted_priorities = sorted(priorities)
        index = binary_search(sorted_priorities, amount % 10)
        if index != -1:
            priorities[index] += order_id
        processed_orders += 1
    
    final_priority_score = sum(priorities) + len(logger.log)

print(f"Result: {final_priority_score}")