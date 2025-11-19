import math

class BlockNode:
    def __init__(self, value):
        self.value = value
        self.hash = 0
        self.next = None

def calculate_statistics(values):
    if not values:
        return 0, 0
    mean_val = sum(values) / len(values)
    variance = sum((x - mean_val) ** 2 for x in values) / len(values)
    std_dev = math.sqrt(variance) if variance > 0 else 0
    return mean_val, std_dev

def hash_string(s):
    hash_val = 0
    for char in s:
        hash_val = (hash_val * 31 + ord(char)) & 0xFFFFFFFF
    return hash_val

# Initialize linked list with string-hashed values
values = [hash_string("alpha"), hash_string("beta"), hash_string("gamma"), hash_string("delta"), hash_string("epsilon")]
head = None
prev = None
for val in values:
    node = BlockNode(val)
    if prev:
        prev.next = node
    else:
        head = node
    prev = node

# Process the blocks and compute hashes
current = head
previous_hashes = []
anomaly_count = 0
block_index = 0

while current:
    if block_index == 0:
        current.hash = current.value & 0xFFFFFFFF
    else:
        current.hash = (previous_hashes[-1] ^ current.value) & 0xFFFFFFFF
    
    previous_hashes.append(current.hash)
    
    # Anomaly detection after the first block
    if block_index > 0:
        prev_values = []
        temp = head
        while temp != current:
            prev_values.append(temp.value)
            temp = temp.next
        
        if len(prev_values) > 0:
            mean_val, std_dev = calculate_statistics(prev_values)
            if std_dev > 0 and abs(current.value - mean_val) > 2 * std_dev:
                anomaly_count += 1
    
    current = current.next
    block_index += 1

print(f"Result: {anomaly_count}")