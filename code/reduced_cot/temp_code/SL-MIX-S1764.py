from collections import deque

def process_batches():
    cookie_queue = deque([15, 22, 9, 30])
    
    # Process first batch
    first_batch = cookie_queue.popleft()
    cookie_queue.append(first_batch % 7)
    
    # Process second batch
    second_batch = cookie_queue.popleft()
    cookie_queue.append(second_batch % 7)
    
    return cookie_queue[0]

front_element = process_batches()
print(f"Result: {front_element}")