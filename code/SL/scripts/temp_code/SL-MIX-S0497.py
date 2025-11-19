from collections import Counter
import itertools

def calculate_security_score(messages):
    # Initialize tracking variables
    char_pool = frozenset(''.join(messages))
    frequency_map = Counter()
    cumulative_shift = 0
    
    # Process each message with string transformations
    for idx, msg in enumerate(messages):
        # Apply Caesar cipher with index-based shift
        shifted_msg = ''.join(chr((ord(c) - ord('a') + idx) % 26 + ord('a')) if c.isalpha() else c for c in msg.lower())
        
        # Update frequency map with transformed characters
        frequency_map.update(shifted_msg)
        
        # Conditional logic with short-circuit evaluation
        if idx > 0 and len(msg) > 5 and msg[0] != msg[-1]:
            # Perform set intersection with character pool
            msg_chars = set(msg.lower())
            common_chars = msg_chars & char_pool
            cumulative_shift += len(common_chars) * idx
    
    # Calculate base score from most frequent characters
    top_chars = frequency_map.most_common(3)
    base_score = sum(count * (ord(char) - ord('a') + 1) for char, count in top_chars)
    
    # Apply modular transformation
    mod_factor = (len(messages) * 7) % 13
    adjusted_score = (base_score * mod_factor) % 1000
    
    # Combine with cumulative shift using modular arithmetic
    final_score = (adjusted_score + cumulative_shift) % 10000
    
    return final_score

# Test data representing intercepted messages
intercepted_messages = [
    "alpha",
    "bravocharlie",
    "deltaechofoxtrot",
    "golfhotelindia"
]

final_score = calculate_security_score(intercepted_messages)
print(f"Result: {final_score}")