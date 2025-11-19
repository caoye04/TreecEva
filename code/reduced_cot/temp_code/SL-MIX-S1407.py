import re
from contextlib import contextmanager

class PacketAnalyzer:
    def __init__(self):
        self.suspicious_count = 0
        
    def log_suspicious(self, func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if result:
                self.suspicious_count += 1
            return result
        return wrapper

@contextmanager
def decrypt_context(state_array, index):
    original_state = state_array[index]
    state_array[index] = 1
    try:
        yield state_array
    finally:
        state_array[index] = original_state

def analyze_packet_headers(headers_matrix, analyzer):
    @analyzer.log_suspicious
    def check_pattern(header_row):
        pattern = r'^[0-9a-f]{2}(?:[0-9a-f]{2}){3}$'
        return bool(re.match(pattern, ''.join(map(chr, header_row[:8]))))
    
    state_tracker = [0] * len(headers_matrix)
    anomaly_counter = 0
    
    for i, row in enumerate(headers_matrix):
        with decrypt_context(state_tracker, i) as tracker:
            if sum(tracker) > 2 and check_pattern(row):
                anomaly_counter += sum(1 for x in row if x % 3 == 0)
            elif i % 2 == 1:
                tracker[i] = tracker[i-1] if i > 0 else 0
                if tracker[i] == 1:
                    anomaly_counter -= sum(row) % 5
    
    return anomaly_counter + analyzer.suspicious_count * 10

# Packet header data (ASCII values of hex representations)
packets = [
    [48, 49, 50, 51, 52, 53, 54, 55, 97, 98],
    [99, 100, 101, 102, 48, 49, 50, 51, 102, 101],
    [50, 52, 54, 56, 97, 99, 49, 51, 53, 55],
    [98, 97, 100, 99, 102, 101, 53, 50, 51, 52]
]

firm = PacketAnalyzer()
anomaly_score = analyze_packet_headers(packets, firm)
print(f'Result: {anomaly_score}')