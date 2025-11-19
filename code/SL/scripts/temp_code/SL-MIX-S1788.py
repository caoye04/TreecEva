def track_ingredient_usage(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        wrapper.total_flour += result
        return result
    wrapper.total_flour = 0
    return wrapper

class BakeryItem:
    def __init__(self, name, flour_per_unit):
        self.name = name
        self.flour_per_unit = flour_per_unit
    
    @track_ingredient_usage
    def prepare_batch(self, quantity):
        return self.flour_per_unit * quantity

# Bakery operations
flour_tracker = BakeryItem.prepare_batch
Croissant = BakeryItem('Croissant', 75)
Baguette = BakeryItem('Baguette', 120)

# Preparing batches
Croissant.prepare_batch(24)
Baguette.prepare_batch(15)
Croissant.prepare_batch(18)
total_flour_consumption = BakeryItem.prepare_batch.total_flour
print(f'Result: {total_flour_consumption}')