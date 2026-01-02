def analyze_risk_factor(metrics):
    # Irrelevant risk analysis with decoy logic
    volatility = sum([m['volatility'] for m in metrics]) / len(metrics)
    skewness = sum([m.get('skew', 0) for m in metrics])
    dummy_score = volatility * 0.7 + skewness * 0.3
    return dummy_score


def calculate_exposure(weights, base=1.0):
    # Misleading exposure calculation (dead path)
    total_exposure = base
    for w in weights:
        total_exposure *= (1 + w)
    return total_exposure


def transform_signals(signals):
    # Distractor: signal transformation not used in final result
    transformed = [(s ** 2 + 1) / (s + 0.5) for s in signals if s != 0]
    normalized = [t / max(transformed) for t in transformed]
    return normalized


def compute_portfolio_health(metrics):
    # Partially relevant health metric (red herring)
    active_assets = [m for m in metrics if m['status'] == 'active']
    inactive_ratio = (len(metrics) - len(active_assets)) / len(metrics)
    health_score = 100 * (1 - inactive_ratio ** 0.5)
    return health_score


def compute_threshold(metrics):
    # Core logic hidden among distractions
    capped_values = [min(m['value'], 500) for m in metrics]
    adjusted_caps = [c - m['liability'] for c, m in zip(capped_values, metrics)]
    filtered = [val for val in adjusted_caps if val > 0]
    
    # Decoy intermediate calculations
    average_risk = sum([m['volatility'] * m['liability'] for m in metrics]) / sum([m['liability'] or 1 for m in metrics])
    peak_value = max(capped_values)
    penalty_rate = 0.15 if len(filtered) < 3 else 0.05
    
    # Critical computation buried in noise
    base_threshold = sum(filtered) * (1 - penalty_rate)
    bonus = len(metrics) * 10 if all(m['value'] > 100 for m in metrics) else 0
    final_penalty = sum([m['liability'] for m in metrics if m['status'] == 'frozen'])
    
    # Actual answer computation
    threshold_balance = int(base_threshold + bonus - final_penalty)
    
    # Unused distracting operations
    synthetic_yield = (base_threshold / (sum([m['value'] for m in metrics]) + 1)) * 100
    compliance_flag = synthetic_yield > 2.5 and len(filtered) % 2 == 0
    
    return threshold_balance

# Main execution block
if __name__ == '__main__':
    portfolio_metrics = [
        {'value': 450, 'liability': 80, 'volatility': 0.2, 'status': 'active'},
        {'value': 600, 'liability': 150, 'volatility': 0.35, 'status': 'active'},
        {'value': 300, 'liability': 100, 'volatility': 0.1, 'status': 'frozen'},
        {'value': 520, 'liability': 90, 'volatility': 0.25, 'status': 'active'},
        {'value': 120, 'liability': 30, 'volatility': 0.05, 'status': 'frozen'}
    ]

    # Irrelevant preprocessing
    weights = [m['value'] / sum([m2['value'] for m2 in portfolio_metrics]) for m in portfolio_metrics]
    signals = [m['volatility'] * m['value'] for m in portfolio_metrics]

    # Dead function calls (distraction)
    _ = analyze_risk_factor(portfolio_metrics)
    _ = calculate_exposure(weights, base=1.5)
    _ = transform_signals(signals)
    _ = compute_portfolio_health(portfolio_metrics)

    # Key statement
    threshold_balance = compute_threshold(portfolio_metrics)

    print(f"Result: {threshold_balance}")