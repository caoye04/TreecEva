from collections import defaultdict, deque
import heapq

def process_fragments():
    doc_queue = deque(['alpha', 'beta', 'gamma', 'delta'])
    freq_map = defaultdict(int)
    priority_heap = []
    
    # Process initial documents
    while doc_queue:
        fragment = doc_queue.popleft()
        transformed = ''.join([chr((ord(c) - ord('a') + 3) % 26 + ord('a')) for c in fragment])
        hash_val = hash(transformed) % 100
        freq_map[hash_val] += 1
        heapq.heappush(priority_heap, (-len(transformed), hash_val))
    
    # Apply secondary transformations
    temp_stack = []
    for _ in range(2):
        if priority_heap:
            _, hash_key = heapq.heappop(priority_heap)
            temp_stack.append(hash_key)
    
    # Update frequencies from stack
    while temp_stack:
        key = temp_stack.pop()
        freq_map[key] *= 2
        heapq.heappush(priority_heap, (-freq_map[key], key))
    
    # Calculate final metric
    top_entries = [heapq.heappop(priority_heap)[0] for _ in range(min(3, len(priority_heap)))]
    final_metric = sum(abs(x) for x in top_entries) + len(freq_map)
    return final_metric

final_metric = process_fragments()
print(f"Result: {final_metric}")