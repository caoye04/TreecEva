import itertools

# Network packet headers encoded as hexadecimal strings
packet_headers = ['0x1A2B', '0x3C4D', '0x5E6F']

# Known malicious patterns database
malicious_patterns = {
    '1A2', 'A2B', '3C4', 'C4D', '5E6', 'E6F',
    '2B3', '4D5', '1A3', '3C5', '2B4', '4D6'
}

# Extract hex values without '0x' prefix
hex_values = [header[2:] for header in packet_headers]

# Generate all possible 3-character substrings from each hex value
all_substrings = set()
for hex_val in hex_values:
    for i in range(len(hex_val) - 2):
        substring = hex_val[i:i+3]
        all_substrings.add(substring)

# Count how many unique substrings match malicious patterns
detected_matches = all_substrings & malicious_patterns
suspicious_count = len(detected_matches)

# Additional processing: check if any pattern appears in multiple headers
pattern_sources = {}
for idx, hex_val in enumerate(hex_values):
    for i in range(len(hex_val) - 2):
        substring = hex_val[i:i+3]
        if substring in malicious_patterns:
            if substring not in pattern_sources:
                pattern_sources[substring] = set()
            pattern_sources[substring].add(idx)

# Count patterns that appear in multiple headers
multi_source_patterns = sum(1 for sources in pattern_sources.values() if len(sources) > 1)
suspicious_count += multi_source_patterns

print(f"Result: {suspicious_count}")