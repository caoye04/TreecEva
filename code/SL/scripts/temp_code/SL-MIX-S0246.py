from collections import deque
from functools import reduce

def process_id(tid):
    return ''.join(chr((ord(c) - ord('A') + 3) % 26 + ord('A')) for c in tid)

def compute_weight(code):
    return sum(ord(c) for c in code) % 100

tracking_ids = ['XYZ987', 'ABC123', 'DEF456']
processing_queue = deque()
checksum_stack = []

for tid in tracking_ids:
    processed = process_id(tid)
    if len(processed) >= 6 and processed[:3].isalpha():
        processing_queue.append(processed)

while processing_queue:
    item = processing_queue.popleft()
    weight = compute_weight(item)
    if weight > 50 or (weight % 7 == 0 and weight != 0):
        checksum_stack.append(weight)
    else:
        adjusted = weight + 10 if weight <= 25 else weight - 5
        checksum_stack.append(adjusted)

final_checksum = reduce(lambda x, y: (x ^ y) & 0xFF, checksum_stack, 0)
print(f"Result: {final_checksum}")