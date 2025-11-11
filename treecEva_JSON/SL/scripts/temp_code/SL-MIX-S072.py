import hashlib
from collections import defaultdict

def classify_packet(header_data):
    hash_value = hashlib.md5(header_data.encode()).hexdigest()
    # Convert first 4 hex chars to int for classification
    classification = int(hash_value[:4], 16) % 5
    return classification

def apply_security_protocol(protocol_id, packet_count):
    protocols = {
        0: lambda x: x * 2,
        1: lambda x: x + 5,
        2: lambda x: x ^ 0xFF,
        3: lambda x: x << 2,
        4: lambda x: x - 3
    }
    return protocols.get(protocol_id, lambda x: x)(packet_count)

packet_headers = [
    "192.168.1.1:80->10.0.0.1:443",
    "172.16.0.5:22->192.168.1.100:22",
    "10.0.0.50:53->8.8.8.8:53",
    "192.168.1.25:443->172.16.0.1:80",
    "10.0.0.25:8080->192.168.1.1:80"
]

# Initialize tracking structures
protocol_counts = defaultdict(int)
security_score = 0

# Process packets through nested loops
for header in packet_headers:
    # First level classification
    primary_class = classify_packet(header)
    protocol_counts[primary_class] += 1
    
    # Second level processing with pattern matching
    if '->' in header:
        src_dst = header.split('->')
        src_parts = src_parts = src_dst[0].split(':')
        dst_parts = dst_parts = src_dst[1].split(':')
        
        # Nested loop for detailed analysis
        for i in range(min(len(src_parts), len(dst_parts))):
            if src_parts[i].isdigit() and dst_parts[i].isdigit():
                src_val = int(src_parts[i])
                dst_val = int(dst_parts[i])
                
                # Apply security protocol based on conditions
                if src_val > 1000 and dst_val < 100:
                    security_score += apply_security_protocol(primary_class, src_val % 10)
                elif src_val < 100 and dst_val > 1000:
                    security_score -= apply_security_protocol(primary_class, dst_val % 10)
                else:
                    security_score ^= (src_val + dst_val) & 0xF

# Final adjustment based on protocol distribution
for protocol_id, count in protocol_counts.items():
    if count > 1:
        security_score = apply_security_protocol(protocol_id, security_score)
    
print(f"Result: {security_score}")