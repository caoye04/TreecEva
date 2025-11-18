from functools import wraps

def sales_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper

class PieSalesTracker:
    def __enter__(self):
        self.sales_record = set()
        return self.sales_record
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

@sales_logger
def process_daily_sales():
    with PieSalesTracker() as record:
        apple_pie_customers = {101, 102, 103, 104}
        blueberry_pie_customers = {103, 104, 105, 106}
        
        # Add all customers to the record
        record.update(apple_pie_customers)
        record.update(blueberry_pie_customers)
        
        # Some customers bought both types
        duplicate_customers = apple_pie_customers & blueberry_pie_customers
        
        # Final unique customer count
        total_unique_customers = len(record)
        
        return total_unique_customers

final_count = process_daily_sales()
print(f"Result: {final_count}")