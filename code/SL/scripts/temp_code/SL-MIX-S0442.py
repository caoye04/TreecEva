import heapq
import itertools
import statistics

def compute_skewness_approx(data):
    if len(data) < 2:
        return 0
    mean_val = statistics.mean(data)
    variance = statistics.variance(data) if len(data) > 1 else 0
    third_moment = sum((x - mean_val)**3 for x in data) / len(data)
    return third_moment / (variance**1.5) if variance > 0 else 0

class SpectralWindowProcessor:
    def __init__(self, window_size=5):
        self.window_size = window_size
        self.metric_heap = []
    
    def process_signal(self, signal_segments):
        scores = []
        for segment in signal_segments:
            # Generate all combinations of window_size elements
            window_combinations = list(itertools.combinations(segment, self.window_size))
            segment_scores = []
            for window in window_combinations:
                var = statistics.variance(window) if len(window) > 1 else 0
                skew = compute_skewness_approx(window)
                # Combinatorial weight based on index positions
                weight = sum(window) * len([x for x in window if x > statistics.mean(window)])
                score = (var * 0.5) + (abs(skew) * 0.3) + (weight * 0.2)
                segment_scores.append(score)
            
            # Use ternary to determine segment aggregation
            agg_score = max(segment_scores) if segment_scores else 0
            scores.append(agg_score)
        
        # Maintain top 3 scores in a min-heap
        for score in scores:
            if len(self.metric_heap) < 3:
                heapq.heappush(self.metric_heap, score)
            elif score > self.metric_heap[0]:
                heapq.heapreplace(self.metric_heap, score)
        
        return statistics.mean(self.metric_heap) if self.metric_heap else 0

# Signal processing pipeline
processor = SpectralWindowProcessor(window_size=4)

# Audio feature segments (each sub-array represents a time segment)
audio_segments = [
    [23, 45, 12, 67, 89, 34],
    [15, 78, 29, 53, 64, 91, 37],
    [42, 18, 76, 25, 83, 59, 11, 68],
    [33, 72, 28, 95, 16, 47, 84]
]

# Process all segments and get final metric
final_metric_score = processor.process_signal(audio_segments)

# Apply final transformation using logical operations
is_high_energy = final_metric_score > 50
is_stable = final_metric_score < 100
adjusted_score = final_metric_score * 1.5 if (is_high_energy and is_stable) else \
                 final_metric_score * 0.8 if (not is_high_energy) else \
                 final_metric_score * 0.9

print(f"Result: {round(adjusted_score, 2)}")