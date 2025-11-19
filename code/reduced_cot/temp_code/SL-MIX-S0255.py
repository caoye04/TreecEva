from collections import deque
from functools import reduce
from operator import xor

def process_packets():
    packet_headers = [0x1A, 0x2B, 0x3C, 0x4D, 0x5E]
    accepted_signatures = deque(maxlen=3)
    validation_keys = {0x10, 0x20, 0x30}
    mask = 0xF0
    
    for header in packet_headers:
        # Step 1: Bitwise filtering
        if header & mask != 0:
            # Step 2: Signature generation using XOR
            signature = header ^ 0xAA
            
            # Step 3: Check if signature is in validation keys
            if signature in validation_keys:
                # Step 4: Add to sliding window (queue)
                accepted_signatures.append(signature)
            else:
                # Step 5: Apply secondary filter using set operations
                temp_set = frozenset([signature & 0x0F, (signature >> 4) & 0x0F])
                if len(temp_set.intersection(validation_keys)) > 0:
                    accepted_signatures.append(signature)
    
    # Step 6: Generate final verification code using reduce and XOR
    if accepted_signatures:
        final_verification_code = reduce(xor, accepted_signatures, 0)
    else:
        final_verification_code = 0
    
    return final_verification_code

final_verification_code = process_packets()
print(f"Result: {final_verification_code}")