import itertools
import string

def analyze_data_packet(packet_data, mode="standard"):
    # Configuration parameters
    base_factors = [2, 3, 5, 7]
    checksum_base = 16
    error_threshold = 0.15
    
    # Process packet headers (not relevant for core calculation)
    header_bytes = [ord(c) % checksum_base for c in packet_data[:4]]
    packet_id = sum(header_bytes) % 1000
    
    # Extract the encoding information
    raw_encoding = packet_data[4:12]
    
    # Calculate some misleading metrics
    entropy = sum(ord(c) for c in raw_encoding) / len(raw_encoding)
    redundancy_factor = (entropy % 10) / 10
    quality_score = 100 - (redundancy_factor * 100)
    
    # Generate potential encoding schemes (this is the relevant part)
    encoding_chars = raw_encoding.lower()
    
    # Filter to valid characters (a-z, 0-9)
    filtered_chars = [c for c in encoding_chars if c in string.ascii_lowercase or c in string.digits]
    
    # Generate all possible 3-character encoding schemes
    potential_encodings = list(itertools.permutations(filtered_chars, 3))
    
    # This is a distraction - not used in final calculation
    if mode == "extended":
        extended_encodings = list(itertools.combinations(filtered_chars, 4))
        composite_score = len(extended_encodings) * redundancy_factor
    else:
        composite_score = 0
        
    # Function to check if an encoding is valid
    def is_valid_encoding(encoding):
        # Basic validity check - must contain at least one letter and one number
        has_letter = any(c in string.ascii_lowercase for c in encoding)
        has_digit = any(c in string.digits for c in encoding)
        
        # Additional checks (mostly distractors)
        if not (has_letter and has_digit):
            return False
        
        # Calculate encoding value (distractor)
        enc_value = sum(ord(c) for c in encoding)
        
        # The actual validity check depends on specific pattern
        # An encoding is valid if it contains exactly one digit
        digit_count = sum(1 for c in encoding if c in string.digits)
        return digit_count == 1
    
    # Count valid encodings
    valid_encodings = len([enc for enc in potential_encodings if is_valid_encoding(enc)])
    
    # More distracting calculations that don't affect the answer
    efficiency_metric = valid_encodings / (len(potential_encodings) or 1)
    adjusted_quality = quality_score * (1 + efficiency_metric)
    
    # Distractor branch that's never executed
    if packet_id < 0:
        valid_encodings = valid_encodings // 2
    
    # Final processing (more distractions)
    transmission_overhead = sum(base_factors) / checksum_base
    if transmission_overhead > error_threshold and mode == "restricted":
        valid_encodings = int(valid_encodings * 0.8)
    
    print(f"Result: {valid_encodings}")
    return valid_encodings

# Test with sample data
packet = "XYZ123abcd456"
result = analyze_data_packet(packet)
