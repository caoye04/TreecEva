import statistics

def compute_portfolio_risk():
    # Portfolio asset data: {asset_id: (value, volatility, correlation_factor)}
    assets = {
        'AAPL': (120000, 0.25, 0.8),
        'GOOGL': (95000, 0.30, 0.7),
        'TSLA': (75000, 0.45, 0.9),
        'AMZN': (110000, 0.28, 0.75)
    }
    
    # Lambda for dynamic risk weighting based on asset value
    risk_weight = lambda value: 1.2 if value > 100000 else 0.9
    
    # Dictionary comprehension to calculate weighted risks
    weighted_risks = {asset: volatility * risk_weight(value) * correlation
                      for asset, (value, volatility, correlation) in assets.items()
                      if value > 50000 and volatility > 0.2}
    
    # Short-circuit evaluation for conditional risk adjustment
    high_risk_flag = len([v for v in assets.values() if v[1] > 0.4]) > 0
    market_condition_factor = 1.1 if high_risk_flag and len(assets) >= 4 else 1.0
    
    # Calculate portfolio risk score using statistical measures
    raw_risks = list(weighted_risks.values())
    avg_risk = statistics.mean(raw_risks)
    risk_variance = statistics.variance(raw_risks) if len(raw_risks) > 1 else 0
    
    # Final risk score calculation
    portfolio_risk_score = (avg_risk * market_condition_factor) + (risk_variance * 10)
    
    return portfolio_risk_score

# Execute and print result
portfolio_risk_score = compute_portfolio_risk()
print(f"Result: {portfolio_risk_score}")