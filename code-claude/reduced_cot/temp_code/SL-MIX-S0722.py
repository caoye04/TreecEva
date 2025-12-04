from collections import Counter, defaultdict
import math

def analyze_transaction_patterns(transactions):
    # Analyze spending patterns (not used in final calculation)
    spending_patterns = defaultdict(list)
    for t in transactions:
        if 'amount' in t and 'category' in t:
            spending_patterns[t['category']].append(t['amount'])
    
    # Calculate average spending per category (distractor)
    avg_spending = {cat: sum(amounts)/len(amounts) 
                  for cat, amounts in spending_patterns.items()}
    return avg_spending

def extract_transaction_metrics(transactions):
    # Extract timestamps (used in final calculation)
    timestamps = [t.get('timestamp', 0) for t in transactions if 'status' in t]
    
    # Calculate frequency metrics (distractor)
    hourly_freq = Counter([t.get('timestamp', 0) % 24 for t in transactions])
    peak_hour = max(hourly_freq.items(), key=lambda x: x[1])[0] if hourly_freq else 0
    
    # Extract amounts (used in final calculation)
    amounts = [t.get('amount', 0) for t in transactions if t.get('status') == 'completed']
    
    return timestamps, amounts, peak_hour

def calculate_risk_factor(transactions):
    # Calculate artificial risk factor (distractor)
    risk_score = 0
    for t in transactions:
        if t.get('amount', 0) > 1000:
            risk_score += 5
        if t.get('flagged', False):
            risk_score += 10
    
    # Apply logarithmic scaling (distractor)
    scaled_risk = math.log(risk_score + 1) * 10 if risk_score > 0 else 0
    return scaled_risk

def filter_transactions(transactions, min_amount=0):
    # Filter transactions (used in final calculation)
    valid_transactions = [t for t in transactions if t.get('status') == 'completed']
    
    # Apply minimum amount filter (distractor path)
    if min_amount > 0:
        filtered = [t for t in valid_transactions if t.get('amount', 0) >= min_amount]
        return filtered
    
    return valid_transactions

def calculate_priority(transactions):
    # Extract key metrics
    timestamps, amounts, peak_hour = extract_transaction_metrics(transactions)
    
    # Irrelevant risk calculation (distractor)
    risk_factor = calculate_risk_factor(transactions)
    potential_fraud_count = sum(1 for t in transactions if t.get('flagged', False))
    
    # Calculate priority components (only some are used)
    recency_factor = max(timestamps) - min(timestamps) if timestamps else 0
    volume_metric = sum(amounts) if amounts else 0
    frequency_factor = len(transactions) / (recency_factor + 1)
    
    # Misleading intermediate results (distractors)
    composite_score = (volume_metric / 100) * frequency_factor
    adjusted_risk = risk_factor * (1 + potential_fraud_count / 10)
    
    # The actual priority calculation
    if recency_factor > 0 and amounts:
        priority = (volume_metric / recency_factor) * (len(amounts) / len(transactions))
    else:
        priority = volume_metric * 0.5
    
    return int(priority)

# Transaction dataset
transactions = [
    {'id': 'tx001', 'amount': 250, 'category': 'shopping', 'timestamp': 1625, 'status': 'completed'},
    {'id': 'tx002', 'amount': 1500, 'category': 'travel', 'timestamp': 1630, 'status': 'completed', 'flagged': True},
    {'id': 'tx003', 'amount': 120, 'category': 'dining', 'timestamp': 1628, 'status': 'pending'},
    {'id': 'tx004', 'amount': 800, 'category': 'shopping', 'timestamp': 1635, 'status': 'completed'},
    {'id': 'tx005', 'amount': 75, 'category': 'dining', 'timestamp': 1640, 'status': 'completed'},
    {'id': 'tx006', 'amount': 350, 'category': 'utilities', 'timestamp': 1642, 'status': 'completed'},
]

# Analyze patterns (distractor)
spending_insights = analyze_transaction_patterns(transactions)

# Apply minimum amount filter (distractor)
min_threshold = 100
high_value_transactions = filter_transactions(transactions, min_threshold)

# Main processing flow
filtered_transactions = filter_transactions(transactions)
priority_score = calculate_priority(filtered_transactions)

# Alternative scoring (distractor)
risk_assessment = calculate_risk_factor(transactions)
composite_rating = (priority_score + risk_assessment) / 2

print(f"Result: {priority_score}")