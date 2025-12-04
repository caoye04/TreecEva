def analyze_signal_strength(values, threshold=75):
    # Signal strength analyzer (not relevant to main task)
    strength = sum(v for v in values if v > threshold)
    noise = sum(v for v in values if v <= threshold)
    return strength - noise if strength > noise * 2 else 0

def calculate_compression_ratio(data, metadata):
    # This function calculates the compression ratio for the processed data
    if not data or 'format' not in metadata:
        return 0.0
    
    # Calculate basic compression metrics
    original_size = len(data)
    compression_factor = metadata.get('base_factor', 2)
    
    # Apply format-specific adjustments
    format_type = metadata['format']
    if format_type == 'binary':
        # Binary format uses bitwise operations for compression
        checksum = 0
        for value in data:
            checksum ^= value & 0xFF
        
        # Calculate binary compression ratio using XOR patterns
        pattern_efficiency = (checksum / 255) if checksum else 0.5
        ratio = (original_size / (compression_factor + pattern_efficiency)) / 10
    elif format_type == 'text':
        # Text compression uses character frequency (not used in this dataset)
        char_counts = {}
        for value in data:
            char_counts[value] = char_counts.get(value, 0) + 1
        entropy = len(char_counts) / original_size
        ratio = (original_size / (compression_factor * entropy)) / 10
    else:
        # Default algorithm for other formats
        unique_values = len(set(data))
        ratio = (original_size / (compression_factor * max(1, unique_values / 2))) / 10
    
    return round(ratio, 2)

# Initialize data for compression analysis
signal_readings = [82, 67, 91, 105, 49, 72, 84, 65, 95, 102]
signal_quality = analyze_signal_strength(signal_readings)

# Process the data for compression
processed_data = []
filter_threshold = 80
quality_factor = 1 if signal_quality > 100 else 0

# Apply data transformations based on quality factor
for i, reading in enumerate(signal_readings):
    # Complex processing with several distractors
    processed_value = reading
    
    # Irrelevant transformation 1
    noise_reduction = (reading % 10) * quality_factor
    
    # Main transformation logic
    if reading > filter_threshold:
        # High value processing
        processed_value = reading & 0xF0  # Keep high bits only
    else:
        # Low value processing with distractor calculations
        temp_value = reading ^ (i * 2)  # XOR with index (distractor)
        unused_metric = temp_value % 7  # Unused calculation
        processed_value = reading
    
    # Another distractor calculation that doesn't affect the result
    alternative_value = (reading + i) if i % 2 == 0 else (reading - i)
    
    # Add the processed value to our dataset
    processed_data.append(processed_value)

# Create metadata for the compression algorithm
metadata = {
    'format': 'binary',
    'base_factor': 4,
    'timestamp': 1635724800,  # Distractor
    'quality_score': signal_quality,  # Distractor
    'alternative_format': 'text'  # Distractor
}

# Prepare alternative metadata (distractor)
alt_metadata = metadata.copy()
alt_metadata['format'] = 'text'

# Calculate the optimal compression ratio
optimal_compression = calculate_compression_ratio(processed_data, metadata)

# Distractor calculations
text_compression = calculate_compression_ratio(processed_data, alt_metadata)
no_compression = len(processed_data) / 10

# Display results
print(f"Signal quality: {signal_quality}")
print(f"Text compression: {text_compression}")
print(f"Result: {optimal_compression}")