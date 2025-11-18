import math

def process_packet_headers():
    # Encoded packet headers as hexadecimal strings
    packet_headers = ['0x1A2B', '0x3C4D', '0x5E6F', '0x7890']
    
    # Convert hex strings to integers and apply initial transformation
    header_values = [int(header, 16) for header in packet_headers]
    transformed_values = [val ^ 0xFF00 for val in header_values]
    
    # Apply floating point transformation: multiply by sqrt(2) and take floor
    float_transformed = [math.floor(val * math.sqrt(2)) for val in transformed_values]
    
    # Bitwise operations: shift left by 2, then AND with 0xFFFF
    shifted_and_masked = [(val << 2) & 0xFFFF for val in float_transformed]
    
    # Create a dictionary mapping original values to processed values
    processing_map = {orig: proc for orig, proc in zip(header_values, shifted_and_masked)}
    
    # Merge with another dictionary containing correction factors
    correction_factors = {0x1A2B: 0x0001, 0x3C4D: 0x0002, 0x5E6F: 0x0003, 0x7890: 0x0004}
    merged_dict = {k: v | correction_factors.get(k, 0) for k, v in processing_map.items()}
    
    # Calculate checksum using XOR reduction
    checksum = 0
    for val in merged_dict.values():
        checksum ^= val
    
    # Final adjustment: convert to 16-bit signed integer representation
    if checksum & 0x8000:
        final_checksum = checksum - 0x10000
    else:
        final_checksum = checksum
        
    return final_checksum

final_checksum = process_packet_headers()
print(f"Result: {final_checksum}")