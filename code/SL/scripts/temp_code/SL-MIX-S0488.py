class PieSalesTracker:
    def __init__(self):
        self.total_revenue = 0
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
    
    def add_sale(self, quantity, price_per_item):
        self.total_revenue += quantity * price_per_item

sales_data = [(5, 12.0), (3, 15.0), (7, 10.0)]

with PieSalesTracker() as tracker:
    for quantity, price in sales_data:
        tracker.add_sale(quantity, price)
    
    # Apply promotional discount logic
    if tracker.total_revenue > 100:
        discount = 0.10
    else:
        discount = 0.05
    
    final_revenue = tracker.total_revenue * (1 - discount)

print(f"Result: {final_revenue}")