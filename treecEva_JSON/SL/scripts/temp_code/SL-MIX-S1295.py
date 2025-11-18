from collections import defaultdict
import statistics

class ReportProcessor:
    def __init__(self, filename):
        self.filename = filename
        self.transactions = []
    
    def __enter__(self):
        # Simulate reading transactions from file
        self.transactions = [
            [1200, -500, 300, -100],
            [2000, -800, 450, -200],
            [1500, -600, 350, -150],
            [1800, -700, 400, -180]
        ]
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

# Initialize variables
quarterly_deviations = []
transaction_map = defaultdict(list)
anomaly_score = 0

# Process reports using context manager
with ReportProcessor('q1_report.txt') as q1, \
     ReportProcessor('q2_report.txt') as q2:
    
    reports = [q1.transactions, q2.transactions]
    
    for quarter_idx, quarter_data in enumerate(reports):
        for day_transactions in quarter_data:
            # Calculate daily balance
            daily_balance = sum(day_transactions)
            transaction_map[quarter_idx].append(daily_balance)
            
            # Nested loop to analyze transaction patterns
            positive_count = 0
            negative_count = 0
            for transaction in day_transactions:
                if transaction > 0:
                    positive_count += 1
                else:
                    negative_count += 1
            
            # Calculate pattern ratio
            if negative_count > 0:
                pattern_ratio = positive_count / negative_count
            else:
                pattern_ratio = float('inf')
            
            # Apply anomaly detection logic
            if pattern_ratio < 2.0 and daily_balance < 1000:
                anomaly_score += 1
        
        # Calculate quarterly statistics
        flat_transactions = [item for sublist in transaction_map[quarter_idx] for item in sublist] if isinstance(transaction_map[quarter_idx][0], list) else transaction_map[quarter_idx]
        if len(flat_transactions) > 1:
            quarterly_deviation = statistics.stdev(flat_transactions)
            quarterly_deviations.append(quarterly_deviation)

# Final anomaly score calculation
if len(quarterly_deviations) >= 2:
    avg_deviation = statistics.mean(quarterly_deviations)
    if avg_deviation > 500:
        anomaly_score *= 2

print(f"Result: {anomaly_score}")