import math

class CallTracker:
    def __init__(self, func):
        self.func = func
        self.call_count = 0
    
    def __call__(self, *args, **kwargs):
        self.call_count += 1
        return self.func(*args, **kwargs)

class ResourceLimiter:
    def __init__(self, limit):
        self.limit = limit
        self.used = 0
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
    
    def consume(self, amount):
        if self.used + amount <= self.limit:
            self.used += amount
            return True
        return False

@CallTracker
def calculate_growth(base_population, rate, time):
    return base_population * math.exp(rate * time)

@CallTracker
def apply_stress(population, stress_factor):
    return population / (1 + math.log(stress_factor))

initial_bacteria = 1000
nutrient_rate = 0.05
incubation_time = 12
stress_level = 2.5
resource_quota = 5000

final_colony_size = 0

with ResourceLimiter(resource_quota) as resources:
    if resources.consume(initial_bacteria) and nutrient_rate > 0:
        intermediate_population = calculate_growth(initial_bacteria, nutrient_rate, incubation_time)
        if intermediate_population < resource_quota or not resources.consume(intermediate_population):
            final_colony_size = apply_stress(intermediate_population, stress_level)
        else:
            final_colony_size = intermediate_population
    else:
        final_colony_size = initial_bacteria

print(f"Result: {int(final_colony_size)}")