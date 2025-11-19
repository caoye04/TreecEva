import re
import heapq

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def tokenize_hex_data(hex_string):
    pattern = r'[0-9a-fA-F]+'
    tokens = re.findall(pattern, hex_string)
    return [int(token, 16) for token in tokens]

def compute_bitwise_transform(values):
    transformed = []
    for i, val in enumerate(values):
        if i % 3 == 0:
            transformed.append(val << 2)
        elif i % 3 == 1:
            transformed.append(val >> 1)
        else:
            transformed.append(val ^ 0xFF)
    return transformed

def build_linked_heap_structure(data_list):
    heap = []
    head = None
    tail = None
    for item in data_list:
        heapq.heappush(heap, item)
        node = Node(item)
        if not head:
            head = node
            tail = node
        else:
            tail.next = node
            tail = node
    return heap, head

def calculate_final_checksum(linked_head, heap_data):
    checksum = 0.0
    current = linked_head
    while current:
        if current.val & 0x1:
            checksum += float(current.val) * 1.5
        else:
            checksum -= float(current.val) / 2.0
        current = current.next
    
    while heap_data:
        val = heapq.heappop(heap_data)
        if val > 100:
            checksum *= 0.95
        else:
            checksum += val * 0.1
    
    return int(checksum) & 0xFFFF

# Main processing pipeline
raw_input = "a1b2c3d4e5f6"
tokens = tokenize_hex_data(raw_input)
transformed_values = compute_bitwise_transform(tokens)
heap_structure, linked_list_head = build_linked_heap_structure(transformed_values)
final_checksum = calculate_final_checksum(linked_list_head, heap_structure)
print(f"Result: {final_checksum}")