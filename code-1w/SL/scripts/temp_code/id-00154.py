from functools import reduce

def process_document_ids():
    # Historical document identifiers
    doc_ids = ['DOC-1923-A', 'MAN-1845-B', 'LET-1901-C']
    
    # Character to integer mapping for encoding
    char_map = {chr(i): i - 64 for i in range(65, 91)}  # A=1, B=2, ..., Z=26
    char_map.update({str(i): i for i in range(10)})      # '0'=0, '1'=1, ..., '9'=9
    char_map.update({'-': 27})
    
    # Encoding function
    encode = lambda s: [char_map[c] for c in s if c in char_map]
    
    # Process each document ID
    encoded_sequences = list(map(encode, doc_ids))
    
    # Apply modular arithmetic transformation
    transformed = [
        [((x * 17) + 13) % 31 for x in seq]
        for seq in encoded_sequences
    ]
    
    # Frequency analysis using dictionary comprehension
    freq_analysis = {
        i: len([seq for seq in transformed if i < len(seq) and seq[i] % 3 == 0])
        for i in range(max(len(seq) for seq in transformed))
    }
    
    # Merge with base frequencies using dictionary merging
    base_freq = {i: 1 for i in range(10)}
    merged_freq = base_freq | {k: v + 1 for k, v in freq_analysis.items()}
    
    # Calculate checksum using functional programming
    checksum_components = [
        reduce(lambda a, b: (a + b) % 29, seq, 0)
        for seq in transformed
    ]
    
    # Final encoded checksum
    encoded_checksum = sum(checksum_components) % 100
    
    return encoded_checksum

result = process_document_ids()
print(f"Result: {result}")