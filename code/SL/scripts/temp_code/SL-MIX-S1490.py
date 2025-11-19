import heapq
from collections import deque

class Item:
    def __init__(self, item_id, priority, timestamp):
        self.item_id = item_id
        self.priority = priority
        self.timestamp = timestamp
    
    def __lt__(self, other):
        if self.priority == other.priority:
            return self.timestamp < other.timestamp
        return self.priority < other.priority

inventory_queue = []
expedited_count = 0
operations_log = [
    ("ADD", "WIDGET_001", 5, 100),
    ("ADD", "GADGET_002", 3, 101),
    ("ADD", "TOOL_003", 7, 102),
    ("PROCESS",),
    ("ADD", "DEVICE_004", 2, 103),
    ("ADD", "SENSOR_005", 6, 104),
    ("PROCESS",),
]

for op in operations_log:
    if op[0] == "ADD":
        _, item_id, priority, timestamp = op
        hash_val = hash(item_id) % 100
        is_expedited = (hash_val % 2 == 0)
        final_priority = priority * 2 if is_expedited else priority
        heapq.heappush(inventory_queue, Item(item_id, final_priority, timestamp))
        expedited_count += 1 if is_expedited else 0
    elif op[0] == "PROCESS":
        if inventory_queue:
            processed_item = heapq.heappop(inventory_queue)
            # Processed items don't affect our count

print(f"Result: {expedited_count}")