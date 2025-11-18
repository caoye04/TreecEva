import heapq
import hashlib

def crypto_hash_verify(documents):
    priority_queue = []
    hash_map = {}
    
    # Process documents and generate hashes
    for idx, doc in enumerate(documents):
        doc_hash = hashlib.sha256(doc.encode()).hexdigest()
        hash_value = sum(ord(c) for c in doc_hash[:8])  # Sum first 8 chars
        hash_map[doc] = hash_value
        heapq.heappush(priority_queue, (hash_value, idx))
    
    verification_score = 0
    
    # Verification process with nested loop analysis
    for i in range(len(documents)):
        current_hash, doc_idx = heapq.heappop(priority_queue)
        doc_content = documents[doc_idx]
        
        # Nested loop for cross-document hash comparison
        for j in range(len(doc_content)):
            char_code = ord(doc_content[j])
            if char_code & 0x01:  # Check if LSB is set
                verification_score += (current_hash >> 2) & 0x0F  # Extract bits 2-5
            else:
                verification_score ^= char_code & 0x07  # XOR with lower 3 bits
    
    return verification_score

doc_collection = [
    "CONFIDENTIAL_REPORT_Q3",
    "ENCRYPTED_PAYLOAD_001",
    "SECURITY_AUDIT_FINDINGS",
    "PRIVACY_COMPLIANCE_DOC"
]

verification_score = crypto_hash_verify(doc_collection)
print(f"Result: {verification_score}")