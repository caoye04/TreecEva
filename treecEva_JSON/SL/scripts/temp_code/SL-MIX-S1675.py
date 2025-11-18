import hashlib
from collections import defaultdict

def calculate_intrusion_score():
    threat_signatures = [
        b'\x45\x00\x00\x3c',
        b'\x45\x00\x00\x40',
        b'\x45\x00\x00\x54'
    ]
    
    packet_headers = [
        b'\x45\x00\x00\x3c\x1a\x2b',
        b'\x45\x00\x00\x40\x3d\x4e',
        b'\x45\x00\x00\x54\x5f\x6a'
    ]
    
    # Convert threat signatures to hash set for faster lookup
    signature_hashes = frozenset(
        hashlib.md5(sig).hexdigest() for sig in threat_signatures
    )
    
    # Count occurrences of each packet type
    packet_counter = defaultdict(int)
    
    intrusion_score = 0
    
    for header in packet_headers:
        # Extract signature part (first 4 bytes)
        signature_part = header[:4]
        
        # Hash the full header
        header_hash = hashlib.md5(header).hexdigest()
        
        # Update counter
        packet_counter[header_hash] += 1
        
        # Check if signature matches threat database
        if hashlib.md5(signature_part).hexdigest() in signature_hashes and packet_counter[header_hash] <= 2:
            # Calculate weight using lambda function
            weight_func = lambda x, y: (x & 0xF) * (y | 0x3) if x > 0 else 1
            
            # Get byte values for calculation
            first_byte = header[0] if len(header) > 0 else 0
            last_byte = header[-1] if len(header) > 0 else 0
            
            # Apply weighting
            weight = weight_func(first_byte, last_byte)
            
            # Short-circuit evaluation for quick exit
            if weight > 0 and (weight % 2 == 0 or weight < 100):
                intrusion_score += weight
                
                # Early return optimization
                if intrusion_score > 200:
                    break
    
    return intrusion_score

# Execute the function
intrusion_score = calculate_intrusion_score()
print(f"Result: {intrusion_score}")