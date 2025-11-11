from collections import deque
import math

def exponential_smoothing(data, alpha=0.3):
    smoothed = [data[0]]
    for i in range(1, len(data)):
        smoothed.append(alpha * data[i] + (1 - alpha) * smoothed[-1])
    return smoothed

class SignalProcessor:
    def __init__(self):
        self.processing_buffer = deque()
        self.smoothed_values = []
    
    def ingest_packets(self, packet_sizes):
        for size in packet_sizes:
            if size > 100:
                self.processing_buffer.appendleft(size)  # High priority
            else:
                self.processing_buffer.append(size)      # Standard queue
    
    def apply_transformations(self):
        transformed = []
        while self.processing_buffer:
            val = self.processing_buffer.popleft()
            # Bitwise transformation: XOR with position, then right shift
            pos = len(transformed)
            transformed_val = (val ^ pos) >> 1
            transformed.append(transformed_val)
        return transformed
    
    def optimize_bandwidth(self, signals):
        # Greedy selection of signals that maximize log benefit
        signals_with_benefit = [(s, math.log(s + 1)) for s in signals if s > 0]
        signals_with_benefit.sort(key=lambda x: x[1], reverse=True)
        selected = []
        total_cost = 0
        for signal, benefit in signals_with_benefit:
            if total_cost + signal <= 500:  # Budget constraint
                selected.append(signal)
                total_cost += signal
        return sum(selected)

# Initialize processor
processor = SignalProcessor()

# Ingest packet stream
packets = [42, 150, 75, 200, 30, 128, 90, 255, 60, 180]
processor.ingest_packets(packets)

# Apply signal transformations
transformed_signals = processor.apply_transformations()

# Apply exponential smoothing
smoothed_data = exponential_smoothing(transformed_signals)

# Optimize bandwidth using a greedy approach on smoothed data
signal_processor = SignalProcessor()
signal_processor.ingest_packets([int(x) for x in smoothed_data])
final_signals = signal_processor.apply_transformations()
optimal_bandwidth = signal_processor.optimize_bandwidth(final_signals)

print(f"Result: {optimal_bandwidth}")