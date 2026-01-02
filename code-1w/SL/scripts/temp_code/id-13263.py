import itertools

# Simulate financial risk assessment with signal processing overlays
def analyze_portfolio_signals(portfolio, market_conditions):
    volatility_log = []
    signal_strength = 0
    adjustment_factor = 1.75
    base_risk = 0.0
    temp_offset = 0  # red herring variable
    ignored_flags = [False, True, False]

    for i, asset in enumerate(portfolio):
        if asset['type'] == 'bond':
            base_risk += 0.1
            continue

        # Real computation mixed with distractions
        recent_trend = asset.get('trend', [])
        if len(recent_trend) == 0:
            volatility_log.append(0)
            continue

        trend_avg = sum(recent_trend) / len(recent_trend)
        if trend_avg > 0:
            signal_strength += 1.5
        elif trend_avg < -0.5:
            signal_strength -= 0.8

        # Distractor: complex but unused transformation
        transformed = [abs(x) ** 0.5 for x in recent_trend if x < 0]
        decay_factor = 0.9 ** len(transformed)  # computed but not used

        volatility_log.append(abs(trend_avg))

    # Unused recursive helper (dead code path)
    def calculate_entropy(data, depth=0):
        if depth > 2 or not data:
            return 0.0
        mid = len(data) // 2
        return calculate_entropy(data[:mid], depth + 1) + (data[mid] if data else 0)

    # Key data structure with cross-references
    risk_profile = {
        'volatility': sum(volatility_log) / len(volatility_log) if volatility_log else 0,
        'strength': signal_strength,
        'flags': ignored_flags
    }

    # Multi-concept mix: bit manipulation and logical checks
    config_flag = 0b1010
    override_mask = 0b1100
    if (config_flag & override_mask) >> 2:
        risk_profile['strength'] *= 1.2

    # Generate weighted impact scores using itertools and zip
    weights = [0.8, 1.3, 0.9, 1.6, 1.1]
    impacts = [0.5, -0.3, 0.7, 0.4, -0.6]
    combined = [w * abs(i) for w, i in zip(weights, impacts)]
    normalized = [c / sum(combined) for c in combined]

    final_weights = []
    for idx, (norm, imp) in enumerate(zip(normalized, impacts)):
        if imp >= 0:
            final_weights.append(norm * (1 + risk_profile['strength']))
        else:
            final_weights.append(norm * (1 - risk_profile['risk_adjustment']) if 'risk_adjustment' in risk_profile else norm * 0.9)

    # Introduce string-based distractor logic
    status_tags = ['stable', 'volatile', 'neutral', 'high_alert']
    tag_summary = ''.join([t[0].upper() for t in status_tags])  # 'SVNHA' - irrelevant

    # Critical execution point embedded in noise
    total_exposure = sum(asset['value'] for asset in portfolio if asset['type'] != 'cash')
    exposure_ratio = total_exposure / market_conditions['total_volume']
    impact_index = min(int(exposure_ratio * 4), 4)  # maps to 0-4 index

    # THIS IS THE KEY STATEMENT
    threshold_balance = final_weights[impact_index] * adjustment_factor

    # More red herrings
    dummy_pairs = list(itertools.combinations_with_replacement([1,2], 2))
    shadow_copy = final_weights[:]
    for _ in range(2):
        shadow_copy = [x * 0.95 for x in shadow_copy]  # decaying copy - never used

    # Final output
    print(f"Result: {threshold_balance}")

# Setup realistic input data
portfolio_data = [
    {'type': 'stock', 'value': 120000, 'trend': [0.2, -0.1, 0.3]},
    {'type': 'bond', 'value': 80000, 'trend': []},
    {'type': 'crypto', 'value': 45000, 'trend': [-0.4, -0.6, -0.3]},
    {'type': 'commodity', 'value': 60000, 'trend': [0.1, 0.2]},
    {'type': 'stock', 'value': 100000, 'trend': [-0.2, 0.1, 0.3]}
]

market_conditions_data = {
    'total_volume': 365000,
    'liquidity_index': 2.3,
    'ignored_thresholds': [0.1, 0.5, 0.9]
}

# Execute
analyze_portfolio_signals(portfolio_data, market_conditions_data)