import hashlib
import re
from collections import defaultdict

def custom_hash(s):
    return int(hashlib.md5(s.encode()).hexdigest()[:8], 16) % 1000000

def process_headers(headers):
    # Initialize DP table for checksum optimization
    dp_table = {}
    dp_checksum = 0
    
    # Process each header with regex pattern matching
    for i, header in enumerate(headers):
        # Extract protocol type using regex
        match = re.search(r'proto:(\w+)', header)
        if match:
            proto_type = match.group(1)
            
            # Switch-like pattern matching for protocol handling
            if proto_type in ['TCP', 'UDP']:
                weight = 3
            elif proto_type == 'ICMP':
                weight = 1
            else:
                weight = 2
                
            # Recursive hash calculation with memoization
            def recursive_hash(text, depth=0):
                if depth > 3:  # Limit recursion depth
                    return custom_hash(text)
                if text in dp_table:
                    return dp_table[text]
                
                sub_hash = custom_hash(text[:len(text)//2] if len(text) > 1 else text)
                result = (sub_hash + recursive_hash(text[len(text)//2:], depth+1)) % 1000000
                dp_table[text] = result
                return result
            
            # Calculate header checksum using nested loops
            header_sum = 0
            for j in range(min(len(header), 10)):  # Limit to first 10 chars
                for k in range(j+1):
                    substring = header[k:j+1]
                    header_sum = (header_sum + custom_hash(substring)) % 1000000
            
            # Update DP checksum with weighted combination
            dp_checksum = (dp_checksum + weight * recursive_hash(header) + header_sum) % 1000000
    
    return dp_checksum

# Protocol headers to process
protocol_headers = [
    "src:192.168.1.1,dst:10.0.0.1,proto:TCP,seq:100",
    "src:10.0.0.1,dst:192.168.1.1,proto:UDP,seq:101",
    "type:EchoRequest,proto:ICMP,id:1234",
    "src:172.16.0.1,dst:8.8.8.8,proto:DNS,port:53"
]

# Execute processing and get result
final_checksum = process_headers(protocol_headers)
print(f"Result: {final_checksum}")