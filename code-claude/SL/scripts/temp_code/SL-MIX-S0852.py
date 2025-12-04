def decode_hex(hex_value):
    # Convert hex to decimal and apply custom transformation
    try:
        decimal_value = int(hex_value, 16)
        transformed = (decimal_value * 3) % 256
        return transformed
    except ValueError:
        return 0

def calculate_checksum(text):
    # Calculate checksum based on character positions
    checksum = 0
    for i, char in enumerate(text):
        if i % 2 == 0:  # Even positions
            checksum += ord(char) * 2
        else:  # Odd positions
            checksum += ord(char) // 2
    return checksum % 100

def analyze_security_level(data):
    # Analyze security level based on character distribution
    digit_count = sum(1 for c in data if c.isdigit())
    letter_count = sum(1 for c in data if c.isalpha())
    special_count = len(data) - digit_count - letter_count
    
    # Higher weight for special characters
    security_score = digit_count + (letter_count * 2) + (special_count * 3)
    return security_score

def parse_metadata(metadata_str):
    # Extract key-value pairs from metadata string
    result = {}
    if not metadata_str or len(metadata_str) < 5:
        return {'version': '1.0', 'status': 'unknown'}
    
    pairs = metadata_str.split(';')
    for pair in pairs:
        if '=' in pair:
            key, value = pair.split('=', 1)
            result[key.strip()] = value.strip()
    
    return result

def calculate_priority(message):
    # Main function to determine message priority
    if not message or len(message) < 10:
        return 0
    
    # Extract components from the message
    parts = message.split('|')
    if len(parts) < 3:
        return 1
    
    content, metadata_str, signature = parts[0], parts[1], parts[2]
    
    # Calculate various metrics (some relevant, some not)
    checksum = calculate_checksum(content)
    security = analyze_security_level(content)
    metadata = parse_metadata(metadata_str)
    
    # Process signature (hex code)
    signature_values = [decode_hex(s) for s in signature.split(':') if len(s) == 2]
    signature_sum = sum(signature_values) if signature_values else 0
    
    # Calculate timestamp influence (misleading calculation)
    timestamp_factor = 0
    if 'timestamp' in metadata:
        try:
            timestamp = int(metadata['timestamp'])
            timestamp_factor = (timestamp % 1000) // 100
        except ValueError:
            timestamp_factor = 2
    
    # Apply complex transformation (distraction)
    transform_map = {'high': 5, 'medium': 3, 'low': 1, 'unknown': 0}
    status_value = transform_map.get(metadata.get('status', 'unknown'), 0)
    complexity_factor = len(content) // 10
    
    # Calculate version weight (relevant)
    version_weight = 0
    if 'version' in metadata:
        version_str = metadata.get('version', '1.0')
        try:
            version_parts = version_str.split('.')
            major = int(version_parts[0]) if len(version_parts) > 0 else 0
            minor = int(version_parts[1]) if len(version_parts) > 1 else 0
            version_weight = (major * 10) + minor
        except (ValueError, IndexError):
            version_weight = 10
    
    # Calculate final priority (the key calculation)
    base_priority = (checksum % 25) + (version_weight * 2)
    priority_level = base_priority + (signature_sum % 10)
    
    # Additional misleading calculations
    alternate_priority = (security // 5) + status_value + complexity_factor
    hybrid_priority = (alternate_priority + priority_level) // 2
    
    # Log various metrics (distraction)
    debug_info = {
        'content_length': len(content),
        'checksum': checksum,
        'security': security,
        'signature_sum': signature_sum,
        'status_value': status_value,
        'version_weight': version_weight,
        'alternate': alternate_priority,
        'hybrid': hybrid_priority
    }
    
    return priority_level

# Test with a sample message
encoded_message = "ALERT-SYSTEM-UPDATE|version=2.3;status=high;timestamp=1642|A5:C2:F1"

# Calculate various metrics for the message
security_level = analyze_security_level(encoded_message)
metadata = parse_metadata(encoded_message.split('|')[1])
checksum_value = calculate_checksum(encoded_message)

# These calculations are distractions
complex_value = security_level * 2 + checksum_value
adjusted_security = security_level + (5 if 'high' in encoded_message else 0)
weighted_factor = len(encoded_message) % 10 + checksum_value % 5

# The key calculation
priority_level = calculate_priority(encoded_message)

# More distractions
modified_priority = priority_level * 2 - weighted_factor
alternate_result = (complex_value % 100) + (modified_priority % 10)

# Final result
print(f"Result: {priority_level}")