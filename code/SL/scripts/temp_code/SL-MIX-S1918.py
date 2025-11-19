from functools import reduce

def apply_transform(x):
    return (x ^ (x << 2)) & 0xFFFF

def is_anomalous(fragment):
    transformed = apply_transform(fragment)
    return (transformed & 0xF0F0) == 0xF0F0

class SignalProcessor:
    def __init__(self):
        self.anomaly_count = 0
        self.total_processed = 0
    
    def process(self, fragments):
        anomaly_score = 0
        for frag in fragments:
            self.total_processed += 1
            if is_anomalous(frag):
                self.anomaly_count += 1
                anomaly_score ^= frag
                if self.anomaly_count >= 3:
                    break
        return anomaly_score

signal_fragments = [0x1234, 0xABCD, 0xF0F0, 0x5678, 0xFFFF, 0x0F0F]
processor = SignalProcessor()
anomaly_score = processor.process(signal_fragments)
print(f"Result: {anomaly_score}")