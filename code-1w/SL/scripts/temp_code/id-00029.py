import base64

def normalize_frequency(freq):
    return round((freq - 1000) / 100, 2)

class SignalProcessor:
    def __init__(self, data):
        self.raw_data = data
        self.processed_signals = []
    
    def __enter__(self):
        encoded_segments = self.raw_data.split('|')
        for segment in encoded_segments:
            try:
                decoded_bytes = base64.b64decode(segment)
                freq_str = decoded_bytes.decode('utf-8')
                freq_val = float(freq_str)
                normalized_freq = normalize_frequency(freq_val)
                self.processed_signals.append(normalized_freq)
            except Exception:
                continue
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

def compute_stellar_hash(signals):
    product = 1
    for s in signals:
        product *= (int(s * 100) + 1)
    return product % 997

encoded_data = "MTIwMA==|MTMwMA==|MTE1MA==|MTQwMA==|MTI1MA=="
with SignalProcessor(encoded_data) as processor:
    sorted_signals = sorted(processor.processed_signals, reverse=True)
    window_avg = sum(sorted_signals[:3]) / 3
    adjusted_signals = [s + window_avg for s in sorted_signals]
    stellar_checksum = compute_stellar_hash(adjusted_signals)
print(f"Result: {stellar_checksum}")