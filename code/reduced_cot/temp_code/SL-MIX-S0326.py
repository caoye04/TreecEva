class DailyLogger:
    def __enter__(self):
        self.log = []
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        pass
    
    def log_sales(self, day, sales):
        self.log.append((day, sales))

fib_prev, fib_curr = 1, 1
total_pies = 1
discount_day = -1

with DailyLogger() as logger:
    logger.log_sales(1, 1)
    if 1 % 5 == 0 and 1 % 2 == 0:
        discount_day = 1
    
    if discount_day == -1:
        total_pies += 1
        logger.log_sales(2, 1)
        if total_pies % 5 == 0 and 2 % 2 == 0:
            discount_day = 2
    
    day = 3
    while discount_day == -1:
        fib_next = fib_prev + fib_curr
        total_pies += fib_next
        logger.log_sales(day, fib_next)
        
        if total_pies % 5 == 0 and day % 2 == 0:
            discount_day = day
        
        fib_prev, fib_curr = fib_curr, fib_next
        day += 1

print(f"Result: {discount_day}")