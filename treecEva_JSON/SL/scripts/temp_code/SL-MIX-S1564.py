from collections import defaultdict
import statistics

def normalize_decorator(func):
    def wrapper(*args, **kwargs):
        data = func(*args, **kwargs)
        mean_val = statistics.mean(data)
        return [x / mean_val for x in data]
    return wrapper

class FrequencyAnalyzer:
    def __init__(self, signals):
        self.signals = signals
    
    @normalize_decorator
    def get_clean_frequencies(self):
        # Remove values outside 2 standard deviations
        mean_sig = statistics.mean(self.signals)
        stdev_sig = statistics.stdev(self.signals)
        lower_bound = mean_sig - 2 * stdev_sig
        upper_bound = mean_sig + 2 * stdev_sig
        filtered = [x for x in self.signals if lower_bound <= x <= upper_bound]
        return filtered

# Simulated deep space signal data (in Hz)
space_signals = [200, 210, 205, 500, 215, 220, 190, 225, 180, 230, 195, 600, 235, 185]
analyzer = FrequencyAnalyzer(space_signals)
normalized_freqs = analyzer.get_clean_frequencies()

# Compute ranked dispersion
ranked_freqs = sorted(normalized_freqs)
rank_map = defaultdict(int)
for idx, freq in enumerate(ranked_freqs):
    rank_map[idx] = freq

dispersion_sum = 0
for i in range(1, len(ranked_freqs)):
    if ranked_freqs[i] > ranked_freqs[i-1]:
        diff = ranked_freqs[i] - ranked_freqs[i-1]
        dispersion_sum += diff * (i+1)

final_metric = round(dispersion_sum, 2)
print(f"Result: {final_metric}")