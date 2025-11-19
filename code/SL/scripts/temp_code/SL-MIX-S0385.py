from collections import defaultdict
import statistics

def exchange_validator(transactions, index=0, accumulated_error=0.0):
    if index >= len(transactions):
        return accumulated_error
    
    current = transactions[index]
    predicted_rate = current['predicted']
    actual_rate = current['actual']
    volume = current['volume']
    
    error = abs(predicted_rate - actual_rate) * volume
    
    if error > 0.01 * volume:  # Significant discrepancy threshold
        adjusted_error = error * 1.5
    else:
        adjusted_error = error
    
    return exchange_validator(transactions, index + 1, accumulated_error + adjusted_error)

class DiscrepancyTracker:
    def __init__(self):
        self.discrepancies = defaultdict(list)
    
    def record(self, currency_pair, error_value):
        self.discrepancies[currency_pair].append(error_value)
    
    def compute_score(self):
        scores = []
        for pair, errors in self.discrepancies.items():
            if len(errors) > 1:
                mean_error = statistics.mean(errors)
                variance_error = statistics.variance(errors)
                score = mean_error * (1 + variance_error)
                scores.append(score)
            else:
                scores.append(errors[0] * 1.1)
        
        if scores:
            return sum(scores) / len(scores)
        return 0.0

# Transaction data
exchange_data = [
    {'predicted': 1.20, 'actual': 1.22, 'volume': 10000},
    {'predicted': 1.20, 'actual': 1.19, 'volume': 15000},
    {'predicted': 0.85, 'actual': 0.87, 'volume': 20000},
    {'predicted': 0.85, 'actual': 0.84, 'volume': 25000},
    {'predicted': 1.10, 'actual': 1.12, 'volume': 30000}
]

# Process transactions
raw_discrepancy = exchange_validator(exchange_data)

# Track discrepancies by currency pairs (simplified to just major pairs)
pairs = ['EUR/USD', 'GBP/USD', 'USD/JPY']
tracker = DiscrepancyTracker()

for i, transaction in enumerate(exchange_data):
    pair = pairs[i % len(pairs)]
    error = abs(transaction['predicted'] - transaction['actual']) * transaction['volume']
    tracker.record(pair, error)

# Compute final score
tracked_score = tracker.compute_score()
final_discrepancy_score = raw_discrepancy + tracked_score

print(f"Result: {final_discrepancy_score}")