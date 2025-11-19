import re
from functools import wraps

def state_tracking(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        result = func(self, *args, **kwargs)
        self.transition_log.append(f"{func.__name__} -> {result}")
        return result
    return wrapper

class DocumentProcessor:
    def __init__(self):
        self.signature_registry = set()
        self.state = 'INITIAL'
        self.transition_log = []
    
    @state_tracking
    def process_signature(self, sig_text):
        patterns = {
            'ALPHA': r'^[A-Za-z]+$',
            'NUMERIC': r'^\d+$',
            'ALPHANUM': r'^[A-Za-z0-9]+$'
        }
        
        match_result = None
        for pattern_type, pattern in patterns.items():
            if re.match(pattern, sig_text):
                match_result = pattern_type
                break
        
        state_map = {
            ('INITIAL', 'ALPHA'): 'TEXT_READY',
            ('TEXT_READY', 'NUMERIC'): 'ID_ASSIGNED',
            ('ID_ASSIGNED', 'ALPHANUM'): 'VALIDATED',
            ('VALIDATED', 'ALPHA'): 'FINALIZED'
        }
        
        next_state = state_map.get((self.state, match_result), 'ERROR')
        self.state = next_state
        
        if next_state == 'FINALIZED':
            self.signature_registry.add(hash(sig_text) % 1000)
        
        return next_state
    
    def run_analysis(self, documents):
        for doc in documents:
            self.process_signature(doc)
        return len(self.signature_registry)

doc_signatures = ['abc', '123', 'abc123', 'def', '456', 'def456', 'ghi']
processor = DocumentProcessor()
final_registry_count = processor.run_analysis(doc_signatures)
print(f"Result: {final_registry_count}")