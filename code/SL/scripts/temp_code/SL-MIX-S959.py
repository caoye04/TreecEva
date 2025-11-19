import math
from functools import wraps

def memoize(func):
    cache = {}
    @wraps(func)
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

class InterestCalculator:
    def __init__(self):
        self.rate_cache = {1: 0.05, 2: 0.06, 3: 0.07}
    
    @memoize
    def compute_rate(self, year):
        return self.rate_cache.get(year, 0.04)
    
    def compound_growth(self, principal, years):
        amount = principal
        for y in range(1, years + 1):
            rate = self.compute_rate(y)
            amount *= math.exp(rate)
        return amount

calculator = InterestCalculator()
total_compounded_amount = calculator.compound_growth(1000, 3)
print(f'Result: {round(total_compounded_amount)}')