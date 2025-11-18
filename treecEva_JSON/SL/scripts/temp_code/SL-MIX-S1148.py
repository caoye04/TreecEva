import re

def process_packet_id(packet_id):
    # Extract numeric parts using regex
    numbers = [int(x) for x in re.findall(r'\d+', packet_id)]
    
    # Apply modular arithmetic to combine numbers
    result = 0
    for num in numbers:
        result = (result * 13 + num) % 100
    return result

# Process a sample packet identifier
packet_identifier = "PKT_2023_456_XYZ_789"
verification_code = process_packet_id(packet_identifier)
print(f"Result: {verification_code}")