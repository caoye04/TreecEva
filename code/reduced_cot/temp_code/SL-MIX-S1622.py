from collections import defaultdict

class PacketValidator:
    def __init__(self):
        self.checksum_registry = defaultdict(int)
        self.packet_count = 0
    
    def process_packet_header(self, header_data):
        # Step 1: Initialize local variables
        segment_mask = 0xF0F0
        base_value = header_data & 0xFF
        
        # Step 2: Apply bitwise transformations
        transformed = (base_value << 4) ^ (base_value >> 2)
        masked_result = transformed & segment_mask
        
        # Step 3: Update registry with arithmetic combination
        registry_key = (header_data >> 8) & 0x0F
        self.checksum_registry[registry_key] += (masked_result + base_value) if (base_value % 3 != 0) else (masked_result - base_value)
        
        # Step 4: Conditional update based on logical operations
        if ((base_value & 0x01) and not (base_value & 0x80)) or (header_data > 0x100):
            self.packet_count += 1
        
        return masked_result

def main():
    validator = PacketValidator()
    packet_headers = [0x1234, 0x5678, 0x9ABC, 0xDEF0, 0x1357, 0x2468]
    intermediate_values = []
    
    # Process each packet header
    for idx, header in enumerate(packet_headers):
        result = validator.process_packet_header(header)
        intermediate_values.append(result)
    
    # Calculate verification code
    accumulator = 0
    for i in range(len(intermediate_values)):
        value = intermediate_values[i]
        key_selector = i & 0x03
        registry_lookup = validator.checksum_registry[key_selector]
        adjustment = (value ^ registry_lookup) if (i % 2 == 0) else (value | registry_lookup)
        accumulator = (accumulator + adjustment) if (adjustment > 0x100) else (accumulator - adjustment)
    
    # Final verification computation
    packet_factor = validator.packet_count * 7
    final_verification_code = (accumulator & 0xFFFF) ^ (packet_factor << 2) if (packet_factor > 10) else (accumulator | packet_factor)
    
    print(f"Result: {final_verification_code}")

if __name__ == "__main__":
    main()