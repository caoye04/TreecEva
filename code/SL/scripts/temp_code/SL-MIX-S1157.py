import re
from collections import defaultdict

def decode_packet_signature(encoded_sig):
    # Step 1: Reverse the string and convert to uppercase
    step1 = encoded_sig[::-1].upper()
    
    # Step 2: Apply regex to extract hexadecimal values
    hex_values = re.findall(r'[0-9A-F]{2}', step1)
    
    # Step 3: Convert hex to integers and perform arithmetic
    integers = [int(h, 16) for h in hex_values]
    transformed = [(x * 3 + 7) % 256 for x in integers]
    
    # Step 4: Bitwise operations
    bitwise_results = []
    for i, val in enumerate(transformed):
        if i % 3 == 0:
            bitwise_results.append(val << 2)
        elif i % 3 == 1:
            bitwise_results.append(val >> 1)
        else:
            bitwise_results.append(val ^ 0xFF)
    
    # Step 5: Floating point operations
    float_ops = [float(x) / 2.5 for x in bitwise_results]
    
    # Step 6: Aggregate using a defaultdict
    agg = defaultdict(float)
    for i, val in enumerate(float_ops):
        agg[i % 4] += val
    
    # Step 7: Calculate final threat score
    threat_score = sum(agg.values()) * 1.7
    return round(threat_score, 2)

# Encoded packet signature
packet_data = "a1b2c3d4e5f6"

# Process the packet
target_result = decode_packet_signature(packet_data)
print(f"Target result: {target_result}")