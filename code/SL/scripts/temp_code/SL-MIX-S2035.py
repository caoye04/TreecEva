from collections import defaultdict
import statistics

class MemoryProfiler:
    def __init__(self):
        self.allocations = []
    
    def __enter__(self):
        return self
    
    def record_allocation(self, size):
        self.allocations.append(size)
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

def compute_moment(data, order):
    if order == 1:
        return statistics.mean(data)
    elif order == 2:
        return statistics.variance(data)
    else:
        mean_val = statistics.mean(data)
        return sum((x - mean_val) ** order for x in data) / len(data)

def design_filter_coefficients(signal_data, max_order):
    with MemoryProfiler() as profiler:
        stats_cache = defaultdict(list)
        for order in range(1, max_order + 1):
            moment = compute_moment(signal_data, order)
            stats_cache[order].append(moment)
            profiler.record_allocation(order * 8)
        
        # Recursive coefficient optimization
        def optimize_taps(order, cache):
            if order <= 1:
                return int(cache[order][0] * 10)
            else:
                prev_result = optimize_taps(order - 1, cache)
                current_stat = cache[order][0]
                return prev_result + int(current_stat * (order + 1))
        
        optimal_taps = optimize_taps(max_order, stats_cache)
    
    return optimal_taps

# Audio signal sample data
signal_samples = [0.5, 1.2, -0.8, 2.1, -1.5, 0.9, 1.8, -0.3]
filter_order = 4

optimal_taps = design_filter_coefficients(signal_samples, filter_order)
print(f"Result: {optimal_taps}")