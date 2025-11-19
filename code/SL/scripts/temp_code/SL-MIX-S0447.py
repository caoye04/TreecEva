from collections import defaultdict
import hashlib

def process_document_signatures():
    # State machine states
    states = ['INIT', 'PARSE', 'HASH', 'VERIFY']
    current_state = 0
    
    # Document signatures
    signatures = ['doc_alpha_2023', 'doc_beta_2024', 'doc_gamma_2025']
    
    # Hash accumulator initialized with a base value
    hash_accumulator = 1000.5
    
    # Process each signature through state machine
    for sig in signatures:
        # State transition: INIT -> PARSE
        if states[current_state] == 'INIT':
            transformed_sig = sig.upper().replace('_', '-')
            current_state = 1
        
        # State transition: PARSE -> HASH
        if states[current_state] == 'PARSE':
            # String hashing with floating point conversion
            sig_hash = int(hashlib.md5(transformed_sig.encode()).hexdigest(), 16) % 1000
            hash_accumulator += sig_hash * 1.5
            current_state = 2
        
        # State transition: HASH -> VERIFY
        if states[current_state] == 'HASH':
            # Bitwise operation and arithmetic
            hash_accumulator = (int(hash_accumulator) & 0xFF) + (hash_accumulator * 0.7)
            current_state = 3
        
        # State transition: VERIFY -> INIT (for next iteration)
        if states[current_state] == 'VERIFY':
            hash_accumulator -= 50.25
            current_state = 0
    
    # Final verification score calculation
    verification_score = int(hash_accumulator) ^ 0xAA
    return verification_score

# Execute the document processing
final_score = process_document_signatures()
print(f"Result: {final_score}")