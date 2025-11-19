import heapq

def process_bakery_orders():
    # Priority mapping: higher number means higher priority
    priorities = {'apple': 3, 'cherry': 2, 'blueberry': 1}
    
    # Orders received throughout the day
    orders = ['blueberry', 'apple', 'cherry', 'apple', 'blueberry', 'cherry', 'apple']
    
    # Initialize max heap (using negative values since heapq is min heap)
    priority_heap = []
    
    # Process each order
    for pie_type in orders:
        heapq.heappush(priority_heap, -priorities[pie_type])
    
    # Calculate sum of priorities in the heap
    priority_sum = 0
    while priority_heap:
        priority_sum += (-heapq.heappop(priority_heap))
    
    return priority_sum

final_priority_sum = process_bakery_orders()
print(f"Result: {final_priority_sum}")