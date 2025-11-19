import math
from itertools import combinations

def evaluate_band_frequency(band_id, amplitude):
    return math.log(amplitude + 1) * (band_id ** 2)

def apply_filter_mask(value, mask):
    return value & mask if value > 10 else value | mask

class SignalProcessor:
    def __init__(self):
        self.processing_score = 0
        self.band_data = {1: 15, 2: 8, 3: 32, 4: 5}
    
    def process_signals(self):
        band_mask = 0b1100
        active_bands = [k for k, v in self.band_data.items() if v > 10]
        
        for band_id in active_bands:
            amplitude = self.band_data[band_id]
            raw_score = evaluate_band_frequency(band_id, amplitude)
            masked_score = apply_filter_mask(int(raw_score), band_mask)
            
            # Short-circuit evaluation with ternary operator
            self.processing_score += masked_score if masked_score > 20 else (
                masked_score * 2 if amplitude < 20 else masked_score // 2
            )
        
        # Additional processing based on combinations
        combo_count = sum(1 for _ in combinations(active_bands, 2))
        self.processing_score = self.processing_score if combo_count > 3 else self.processing_score * combo_count
        
        return self.processing_score

# Main execution
processor = SignalProcessor()
final_score = processor.process_signals()
print(f"Result: {final_score}")