from collections import defaultdict
import math

def tokenize_signature(raw_signature):
    tokens = []
    for i in range(0, len(raw_signature), 4):
        token = raw_signature[i:i+4]
        if len(token) == 4:
            tokens.append(int.from_bytes(token.encode(), 'big'))
    return tokens

def is_suspicious_pattern(token):
    # Check if token has alternating bit pattern (e.g., 0101... or 1010...)
    return (token & 0xAAAAAAAA) == 0 or (token & 0x55555555) == 0

class PacketAnalyzer:
    def __init__(self):
        self.pattern_frequency = defaultdict(int)
        self.threat_score = 0
    
    def process_packet_batch(self, packet_signatures):
        batch_threat = 0
        for signature in packet_signatures:
            tokens = tokenize_signature(signature)
            for token in tokens:
                if is_suspicious_pattern(token):
                    self.pattern_frequency[token] += 1
                    # Bitwise operations to calculate threat level
                    threat_indicator = (token & 0xFF) ^ ((token >> 8) & 0xFF)
                    batch_threat += threat_indicator * self.pattern_frequency[token]
        self.threat_score += batch_threat & 0xFFFF

# Simulate processing a batch of 128 network packets
analyzer = PacketAnalyzer()
packet_data = [
    "PKT001THREAT_SIG1",
    "PKT002SAFE_PATTERN",
    "PKT003THREAT_SIG2",
    "PKT004THREAT_SIG1",
    "PKT005THREAT_SIG3"
] * 25 + ["PKT126THREAT_SIG1", "PKT127THREAT_SIG2", "PKT128THREAT_SIG1"]

analyzer.process_packet_batch(packet_data)
print(f"Result: {analyzer.threat_score}")