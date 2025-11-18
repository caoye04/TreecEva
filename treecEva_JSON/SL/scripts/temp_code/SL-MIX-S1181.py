import re
from dataclasses import dataclass
from typing import NamedTuple

class PacketHeader(NamedTuple):
    source_port: int
    dest_port: int
    seq_num: int
    ack_num: int
    flags: int
    window_size: int

@dataclass
class ValidationResult:
    is_valid: bool
    checksum: int
    flags_mask: int

def validate_packet(header: PacketHeader, magic_number: int) -> ValidationResult:
    # Step 1: Calculate initial checksum using modular arithmetic
    base_checksum = (header.source_port + header.dest_port + header.seq_num) % 65537
    
    # Step 2: Apply bitwise operations for flag analysis
    flag_pattern = (header.flags & 0x1F) ^ (magic_number >> 3)
    
    # Step 3: Window size validation with short-circuit evaluation
    valid_window = header.window_size > 0 and header.window_size < 65536 and (header.window_size & (header.window_size - 1)) == 0
    
    # Step 4: Sequence number check with modular comparison
    seq_check = (header.seq_num % 1000) <= 500
    
    # Step 5: Combine validations
    is_valid = valid_window and seq_check
    
    # Step 6: Calculate final checksum
    final_checksum = (base_checksum << 4) | (flag_pattern & 0xF)
    
    return ValidationResult(is_valid, final_checksum, flag_pattern)

def process_suspicious_patterns(log_data: str) -> int:
    # Parse log data for suspicious patterns
    pattern = r'(\d+):(\d+):(\d+):(\d+):(\d+):(\d+)'
    matches = re.findall(pattern, log_data)
    
    if not matches:
        return 0
    
    total_score = 0
    magic_const = 0xACE
    
    for match in matches:
        # Convert strings to integers
        values = [int(x) for x in match]
        
        # Create packet header
        header = PacketHeader(*values)
        
        # Validate packet
        result = validate_packet(header, magic_const)
        
        # Calculate suspicion score based on validation results
        score_component = 0
        if not result.is_valid:
            score_component += (result.checksum & 0xFF) ^ result.flags_mask
        else:
            score_component = (result.checksum >> 2) & 0x3F
        
        total_score = (total_score + score_component) % 1009
    
    return total_score

# Main execution
network_log = "1234:80:123456:789012:24:4096 22:22:987654:321098:17:8192 8080:443:111111:222222:31:16384"
suspicion_score = process_suspicious_patterns(network_log)
print(f"Result: {suspicion_score}")