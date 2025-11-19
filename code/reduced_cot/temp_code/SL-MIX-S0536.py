import math

def signal_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return round(result, 4)
    return wrapper

class FilterOptimizer:
    def __init__(self):
        self.coefficients = {}
    
    def __call__(self, signals):
        # Dictionary comprehension with merging
        base_coeffs = {i: math.log(i+1) for i in range(1, len(signals)+1)}
        adjustment = {i: math.sin(i * 0.1) for i in range(1, len(signals)+1)}
        self.coefficients = base_coeffs | {k: base_coeffs[k] + adjustment[k] for k in base_coeffs}
        return self.compute_optimal_gain(signals)
    
    @signal_decorator
    def compute_optimal_gain(self, signals):
        n = len(signals)
        dp_table = [0] * (n + 1)
        
        # Dynamic programming approach
        for i in range(1, n + 1):
            # Short-circuit evaluation
            if i >= 2 and (signals[i-1] > 0 or signals[i-2] > 0):
                dp_table[i] = max(dp_table[i-1], dp_table[i-2] + signals[i-1] * self.coefficients.get(i, 0))
            else:
                dp_table[i] = dp_table[i-1]
        
        # Switch-case equivalent using dictionary
        gain_strategy = {
            'low': lambda x: x * 0.5,
            'medium': lambda x: x * 1.0,
            'high': lambda x: x * 1.5
        }
        
        avg_signal = sum(signals) / len(signals) if len(signals) > 0 else 0
        
        # Determine strategy based on average signal strength
        if avg_signal < 0.3:
            strategy = 'low'
        elif avg_signal < 0.7 and avg_signal >= 0.3:
            strategy = 'medium'
        else:
            strategy = 'high'
        
        return gain_strategy[strategy](dp_table[n])

# Execution
sensor_readings = [0.1, 0.4, 0.8, 0.2, 0.9, 0.3]
optimizer = FilterOptimizer()
optimal_gain = optimizer(sensor_readings)
print(f"Result: {optimal_gain}")