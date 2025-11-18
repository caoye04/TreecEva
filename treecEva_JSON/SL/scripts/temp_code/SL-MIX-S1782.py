from functools import wraps

def call_tracker(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        return func(*args, **kwargs)
    wrapper.call_count = 0
    return wrapper

class FilterProcessor:
    def __init__(self):
        self.coefficients_cache = {}
    
    @call_tracker
    def compute_coefficient(self, order):
        if order in self.coefficients_cache:
            return self.coefficients_cache[order]
        if order <= 1:
            result = 1
        else:
            result = self.compute_coefficient(order-1) + 2 * self.compute_coefficient(order-2)
        self.coefficients_cache[order] = result
        return result

# Signal processing pipeline
processor = FilterProcessor()
signal_orders = [i for i in range(1, 6)]
filter_weights = []

for idx, order in enumerate(signal_orders):
    coeff = processor.compute_coefficient(order)
    if coeff > 10:
        break
    weight = coeff * (idx + 1)
    filter_weights.append(weight)
    if processor.compute_coefficient.call_count >= 8:
        break

# Calculate final filter strength
final_filter_strength = sum(filter_weights) + len(processor.coefficients_cache)
print(f"Result: {final_filter_strength}")