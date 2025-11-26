def calculate_data_metrics(packet_data):
    # Irrelevant helper function - dead code path
    total_chars = len(packet_data)
    vowel_count = sum(1 for c in packet_data.lower() if c in 'aeiou')
    consonant_ratio = (total_chars - vowel_count) / max(1, total_chars)
    return consonant_ratio * 100

def process_network_packet(data_stream):
    # Distractor computations
    temp_buffer = data_stream.encode('utf-8')
    byte_sum = sum(temp_buffer)  # Misleading intermediate
    
    # Main logic path
    char_frequencies = {}
    for char in data_stream:
        char_frequencies[char] = char_frequencies.get(char, 0) + 1
    
    # Complex mixed operations
    unique_chars = len(char_frequencies)
    total_chars = len(data_stream)
    
    # Bitwise operations with string manipulation
    checksum_seed = ord(data_stream[0]) if data_stream else 0
    xor_mask = checksum_seed ^ 0b10101010
    
    # String methods and conditional logic
    processed_chars = []
    for i, char in enumerate(data_stream):
        if i % 2 == 0:
            processed_chars.append(char.upper())
        else:
            processed_chars.append(char.lower())
    
    transformed_string = ''.join(processed_chars)
    
    # Final calculation with multiple steps
    char_value_sum = sum(ord(c) for c in transformed_string)
    normalization_factor = max(1, unique_chars)
    
    # Key computation chain
    base_value = (char_value_sum // normalization_factor) & xor_mask
    checksum_adjustment = (len(data_stream) % 16) << 4
    final_checksum = (base_value | checksum_adjustment) % 256
    
    # Unused distraction
    unused_metric = calculate_data_metrics(data_stream)
    
    return final_checksum

# Main execution with distractor variables
original_data = "NetworkPacket2024"
backup_data = "BackupStream"  # Irrelevant variable

# Distractor operations
backup_hash = sum(ord(c) for c in backup_data)  # Dead code
packet_size = len(original_data)
header_size = 8  # Misleading constant

# Critical execution point
final_checksum = process_network_packet(original_data)

print(f"Result: {final_checksum}")