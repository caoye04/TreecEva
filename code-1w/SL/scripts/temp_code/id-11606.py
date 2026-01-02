from itertools import cycle

def analyze_financial_cycle(transactions, noise_factor=0.05):
    base_trend = [100, -50, 75, -25, 200, -180]
    fluctuation_mask = [1, -1, 0, 1, -1]
    
    # Simulate extended transaction sequence
    extended_ops = []
    for i, op in enumerate(transactions):
        scaled_op = op * (1 + noise_factor) if i % 2 == 0 else op * (1 - noise_factor)
        extended_ops.append(int(scaled_op))
    
    # Add irrelevant smoothing pass
    smoothed = []
    for j in range(len(extended_ops)):
        window = extended_ops[max(0, j-1):j+2]
        avg = sum(window) / len(window)
        smoothed.append(round(avg))
    
    # Core balance tracking with distractions
    current_balance = 500
    peak_balance = 500
    temp_offset = 0
    debug_log = []
    pattern_tracker = {'surges': 0, 'dips': 0}
    
    # Use cycle for repeating micro-adjustments
    adjustment_stream = cycle([2, -3, 1])
    
    for k, amount in enumerate(smoothed):
        # Inject minor periodic adjustment (semi-relevant)
        micro_adj = next(adjustment_stream)
        current_balance += amount + micro_adj
        
        # Update peak (critical logic)
        if current_balance > peak_balance:
            peak_balance = current_balance
        
        # Distractor: track pattern anomalies that don't affect result
        if amount > 0:
            pattern_tracker['surges'] += 1
            if amount > 100:
                temp_offset += 10
        elif amount < 0:
            pattern_tracker['dips'] += 1
            if k % 3 == 0:
                debug_log.append(f'Dip at {k}')
        
        # Irrelevant early threshold check
        if current_balance > 1000 and k < 5:
            current_balance -= 50
    
    # Unused aggregation
    total_fluctuation = sum(abs(f) for f in fluctuation_mask)
    surge_to_dip_ratio = pattern_tracker['surges'] / max(1, pattern_tracker['dips'])
    
    return peak_balance

# Input with semantic meaning
daily_transfers = [120, -80, 95, -45, 300, -150, 60, -70]
result = analyze_financial_cycle(daily_transfers)
print(f"Target result: {result}")