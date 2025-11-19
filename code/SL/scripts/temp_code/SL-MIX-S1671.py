from collections import deque
import math

def transform_entropy(entropy_deque):
    # Apply logarithmic scaling to the first element
    first_element = entropy_deque.popleft()
    scaled_first = int(math.log2(first_element + 1)) if first_element > 0 else 0
    entropy_deque.appendleft(scaled_first)
    
    # Perform XOR folding on the deque
    while len(entropy_deque) > 1:
        left = entropy_deque.popleft()
        right = entropy_deque.pop()
        folded = left ^ right
        entropy_deque.append(folded)
    
    return entropy_deque[0]

def generate_session_key(initial_pool):
    # Convert list to deque for efficient operations
    entropy_buffer = deque(initial_pool)
    
    # Apply exponential amplification to even positions
    for i in range(0, len(entropy_buffer), 2):
        entropy_buffer[i] = int(math.pow(entropy_buffer[i], 1.5))
    
    # Bitwise rotation of odd positions
    for i in range(1, len(entropy_buffer), 2):
        entropy_buffer[i] = ((entropy_buffer[i] << 2) | (entropy_buffer[i] >> 6)) & 0xFF
    
    # Transform the entropy through multiple rounds
    round_keys = []
    for _ in range(3):
        working_copy = deque(entropy_buffer)
        round_key = transform_entropy(working_copy)
        round_keys.append(round_key)
        # Update buffer with shifted values for next round
        entropy_buffer.rotate(1)
    
    # Combine round keys using bitwise operations
    session_key = round_keys[0]
    for i in range(1, len(round_keys)):
        if i % 2 == 1:
            session_key &= round_keys[i]
        else:
            session_key |= round_keys[i]
    
    return session_key

# Initial entropy pool for session key generation
initial_entropy_pool = [12, 45, 67, 89, 23, 156, 78, 203]
session_key = generate_session_key(initial_entropy_pool)
print(f"Result: {session_key}")