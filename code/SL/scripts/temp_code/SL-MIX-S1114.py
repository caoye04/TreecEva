import hashlib

def encode_char(c):
    return (ord(c) * 17 + 23) % 256

class DocumentProcessor:
    def __init__(self):
        self.state = 'INIT'
        self.processed_count = 0
        self.digest_values = []
    
    def process_documents(self, docs):
        for doc in docs:
            # State transition: INIT -> VALIDATE
            if self.state == 'INIT':
                self.state = 'VALIDATE'
            
            # Validation state
            if self.state == 'VALIDATE':
                valid_chars = [c for c in doc if c.isalnum() or c.isspace()]
                cleaned_doc = ''.join(valid_chars)
                self.state = 'NORMALIZE'
            
            # Normalization state
            if self.state == 'NORMALIZE':
                normalized = cleaned_doc.lower().strip()
                char_matrix = []
                for i in range(0, len(normalized), 5):
                    segment = normalized[i:i+5]
                    encoded_segment = [encode_char(c) for c in segment]
                    char_matrix.append(encoded_segment)
                self.state = 'HASH'
            
            # Hashing state
            if self.state == 'HASH':
                segment_hashes = []
                for row in char_matrix:
                    segment_str = ''.join(chr(val) for val in row if val > 0)
                    if segment_str:
                        hash_val = hash(segment_str) % 10000
                        segment_hashes.append(hash_val)
                doc_digest = sum(segment_hashes) % 1000
                self.digest_values.append(doc_digest)
                self.processed_count += 1
                self.state = 'COMPLETE'
            
            # Reset state for next document
            if self.state == 'COMPLETE':
                self.state = 'INIT'
        
        # Final aggregation
        final_digest = 0
        for i, digest in enumerate(self.digest_values):
            weight = (i + 1) * 7
            final_digest = (final_digest + (digest * weight)) % 997
        return final_digest

technical_abstracts = [
    "Machine learning algorithms optimize neural network parameters",
    "Quantum computing leverages superposition for parallel processing",
    "Blockchain technology ensures distributed consensus mechanisms"
]

processor = DocumentProcessor()
final_digest = processor.process_documents(technical_abstracts)
print(f"Result: {final_digest}")