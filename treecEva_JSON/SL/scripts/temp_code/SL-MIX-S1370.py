class FeeTracker:
    def __init__(self):
        self.fee = 0
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
    
    def add_fee(self, amount):
        if amount > 1000:
            self.fee += amount * 0.02
        elif amount > 500:
            self.fee += amount * 0.015
        else:
            self.fee += amount * 0.01

def process_transactions(transactions):
    def calculate_chunk_fees(chunk):
        if len(chunk) <= 1:
            with FeeTracker() as tracker:
                tracker.add_fee(chunk[0] if chunk else 0)
                return tracker.fee
        mid = len(chunk) // 2
        left_fee = calculate_chunk_fees(chunk[:mid])
        right_fee = calculate_chunk_fees(chunk[mid:])
        return left_fee + right_fee
    
    return calculate_chunk_fees(transactions)

transactions_list = [200, 600, 1200, 300, 800]
total_fees = process_transactions(transactions_list)
print(f"Result: {total_fees}")