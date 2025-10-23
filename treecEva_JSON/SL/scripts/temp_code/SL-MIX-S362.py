import heapq
from itertools import combinations
from functools import reduce

def amplify_signal(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * 2 if result > 0 else result
    return wrapper

class SignalProcessor:
    def __init__(self, signals):
        self.signals = signals
        self.filter_coefficients = [0.5, 0.3, 0.2]
    
    @amplify_signal
    def process(self):
        # Convert signals to heap
        heap = [-s for s in self.signals]
        heapq.heapify(heap)
        
        # Extract 3 largest signals
        top_signals = [abs(heapq.heappop(heap)) for _ in range(3)]
        
        # Apply filter coefficients using functional approach
        filtered = list(map(lambda x, y: x * y, top_signals, self.filter_coefficients))
        
        # Generate all combinations of 2 filtered signals
        signal_pairs = list(combinations(filtered, 2))
        
        # Calculate combined strength using reduce
        combined_strength = reduce(lambda a, b: a + b[0] * b[1], signal_pairs, 0)
        
        # Ternary operation to determine final adjustment
        adjusted_strength = combined_strength if combined_strength > 10 else combined_strength * 3
        
        return adjusted_strength

# Initialize processor with research data
sensor_readings = [15, -8, 22, -5, 17, 30, -12, 25]
processor = SignalProcessor(sensor_readings)
final_signal_strength = processor.process()
print(f'Result: {final_signal_strength}')