def compute_document_signature(text_blocks, priority_indices=[3, 1, 4]):
    # Initialize document metadata
    block_count = len(text_blocks)
    metadata = {
        "blocks": block_count,
        "priority": sum(priority_indices),
        "checksum": 0,
        "version": "2.3.1"
    }
    
    # Process blocks using different algorithms
    hash_value = 0x1234  # Base hash seed
    secondary_hash = 0x5678  # Secondary hash (distraction)
    tertiary_value = 0  # Tertiary tracking (unused)
    
    # Track character frequencies for analysis (distraction)
    char_freq = {}
    for c in ''.join(text_blocks):
        if c.isalnum():
            char_freq[c] = char_freq.get(c, 0) + 1
    
    # Apply transformations to each block
    for idx, block in enumerate(text_blocks):
        # Calculate block weight
        weight = len(block) % 16
        if idx in priority_indices:
            weight = (weight * 2) | 0x1
        else:
            secondary_hash = (secondary_hash + ord(block[0]) if block else 0) & 0xFFFF
        
        # Update hash with block data
        for char_idx, char in enumerate(block):
            char_value = ord(char)
            if char_idx % 3 == 0:  # Only process every third character
                hash_value = ((hash_value << 1) ^ char_value) & 0xFFFF
            elif char.isdigit():  # Track digits separately (distraction)
                tertiary_value += int(char)
    
    # Apply bit manipulations based on metadata
    mask_values = [0xF00D, 0xBEEF, 0xCAFE, 0xDEAD]
    selected_masks = [mask_values[i % len(mask_values)] for i in priority_indices]
    
    # Combine masks (distraction path)
    combined_mask = 0
    for mask in selected_masks:
        combined_mask |= (mask & 0xFF)
    
    # Process metadata with bit operations
    metadata_bits = block_count << 8 | (len(priority_indices) & 0xFF)
    potential_keys = [metadata_bits, combined_mask, hash_value & 0xFF]
    
    # Calculate final masks
    primary_mask = 0
    final_mask = 0
    
    # Process character frequency insights (distraction)
    frequent_chars = sorted(char_freq.items(), key=lambda x: x[1], reverse=True)[:3]
    for char, freq in frequent_chars:
        primary_mask = (primary_mask + ord(char)) % 256
    
    # Generate signature components
    for i, (mask, key) in enumerate(zip(mask_values, potential_keys)):
        if i < len(priority_indices):
            # Apply priority index transformation
            p_idx = priority_indices[i]
            final_mask = (final_mask + (mask >> (p_idx % 8))) & 0xFFFF
    
    # Calculate document signature
    signature = 0
    for idx, val in enumerate([hash_value, metadata_bits, combined_mask]):
        if idx in set(priority_indices):
            signature ^= val
    
    # Apply final transformation
    final_hash = (hash_value ^ final_mask) & 0xFFFF
    
    # Debug information (distraction)
    debug_info = {
        "secondary": secondary_hash,
        "tertiary": tertiary_value,
        "signature": signature
    }
    
    print(f"Result: {final_hash}")
    return final_hash

# Test document with blocks of text
text_blocks = [
    "Document begins",
    "Section A: Introduction",
    "This contains important information",
    "Section B: Data analysis",
    "Conclusion and summary"
]

result = compute_document_signature(text_blocks)