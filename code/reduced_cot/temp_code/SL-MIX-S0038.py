from functools import wraps

def price_tracker(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        base_price = func(*args, **kwargs)
        return round(base_price * 1.2, 2)
    return wrapper

@price_tracker
def compute_batch_expense(flour_kg, butter_kg, yeast_units):
    flour_cost = flour_kg * 3.50
    butter_cost = butter_kg * 7.80
    yeast_cost = yeast_units * 0.15
    return flour_cost + butter_cost + yeast_cost

final_batch_cost = compute_batch_expense(10.5, 5.2, 200)
print(f'Result: {final_batch_cost}')