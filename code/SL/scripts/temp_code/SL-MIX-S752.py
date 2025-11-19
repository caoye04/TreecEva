class ResourceTracker:
    def __init__(self):
        self.resources = 0
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
    
    def consume(self, amount):
        self.resources += amount
        return self.resources

def calculate_base_fee(volume, threshold=1000):
    return volume * 0.001 if volume <= threshold else volume * 0.0015

def is_profitable(volume, price, fee):
    revenue = volume * price
    return revenue > fee and revenue - fee > 50

# Main computation logic
trade_volumes = [500, 1200, 800, 1600, 300]
prices = [40000, 41000, 39000, 42000, 38000]
fees = []

with ResourceTracker() as tracker:
    for i in range(len(trade_volumes)):
        base_fee = calculate_base_fee(trade_volumes[i])
        # Short-circuit evaluation prevents calling consume() when not profitable
        if is_profitable(trade_volumes[i], prices[i], base_fee) and tracker.consume(base_fee) > 0:
            adjusted_fee = base_fee + (base_fee * 0.1 if trade_volumes[i] > 1000 else 0)
            fees.append(adjusted_fee)
        else:
            fees.append(base_fee)
    
    # Greedy selection of maximum fee
    final_fee = max(fees) if fees else 0

print(f'Result: {final_fee}')