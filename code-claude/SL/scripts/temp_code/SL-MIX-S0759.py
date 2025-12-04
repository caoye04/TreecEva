def analyze_market_sentiment(news_articles):
    # Analyze market sentiment from news (distractor function)
    positive_words = {'bullish', 'growth', 'profit', 'surge', 'gain'}
    negative_words = {'bearish', 'crash', 'loss', 'decline', 'risk'}
    
    word_counts = {}
    for article in news_articles:
        words = article.lower().split()
        for word in words:
            if word in positive_words or word in negative_words:
                word_counts[word] = word_counts.get(word, 0) + 1
    
    sentiment_score = sum(word_counts.get(word, 0) for word in positive_words) - \
                      sum(word_counts.get(word, 0) for word in negative_words)
    return sentiment_score * 0.1

def simulate_market_conditions():
    # Simulates various market conditions (distractor function)
    market_conditions = {
        'volatility': 8.5,
        'trading_volume': 12500000,
        'interest_rate': 3.25,
        'market_cap': 2800000000
    }
    
    # Complex calculation that doesn't affect the result
    adjusted_volatility = market_conditions['volatility'] * \
                         (1 + market_conditions['interest_rate']/100)
    
    # This value is never used
    market_health = (market_conditions['trading_volume'] / 10000000) * \
                   (market_conditions['market_cap'] / 1000000000)
    
    return adjusted_volatility

def calculate_portfolio_metrics(holdings):
    # Calculate various portfolio metrics (partially relevant)
    total_value = sum(coin['amount'] * coin['price'] for coin in holdings)
    total_cost = sum(coin['amount'] * coin['cost_basis'] for coin in holdings)
    
    # Distractor calculations
    diversity_score = len(set(coin['symbol'] for coin in holdings))
    risk_factor = sum(coin['volatility'] * (coin['amount'] * coin['price'] / total_value) 
                     for coin in holdings if 'volatility' in coin)
    
    # Only return what's needed
    return {'value': total_value, 'cost': total_cost}

def apply_tax_rules(profit, tax_bracket=0.25):
    # Apply tax rules to profit (distractor with some relevance)
    standard_deduction = 12500
    capital_gains_threshold = 40000
    
    if profit <= 0:
        return 0
    
    taxable_profit = max(0, profit - standard_deduction)
    
    # Misleading calculation that isn't used
    progressive_tax = 0
    if taxable_profit > capital_gains_threshold:
        progressive_tax = (taxable_profit - capital_gains_threshold) * 0.35 + \
                         capital_gains_threshold * tax_bracket
    else:
        progressive_tax = taxable_profit * tax_bracket
    
    # The actual calculation we use
    flat_tax = profit * 0.15
    return flat_tax

def calculate_final_profit():
    # Initial portfolio - these are the values that matter
    crypto_holdings = [
        {'symbol': 'BTC', 'amount': 0.75, 'price': 28000, 'cost_basis': 22000, 'volatility': 0.65},
        {'symbol': 'ETH', 'amount': 12, 'price': 1800, 'cost_basis': 1200, 'volatility': 0.58},
        {'symbol': 'SOL', 'amount': 50, 'price': 90, 'cost_basis': 120, 'volatility': 0.72}
    ]
    
    # Distractor data
    market_news = [
        "Bitcoin sees bullish trend amid institutional adoption",
        "Crypto markets face risk of regulatory crackdown",
        "Analysts predict growth in Ethereum ecosystem",
        "Market crash fears loom as inflation rises"
    ]
    
    # More distractors
    sentiment = analyze_market_sentiment(market_news)
    market_volatility = simulate_market_conditions()
    
    # Calculation that matters
    metrics = calculate_portfolio_metrics(crypto_holdings)
    gross_profit = metrics['value'] - metrics['cost']
    
    # Misleading intermediate calculation
    adjusted_profit = gross_profit * (1 + sentiment/100) * (1 - market_volatility/100)
    
    # Distractor branch that's never taken
    if sentiment > 50 and market_volatility < 2:
        # This never executes
        bonus_profit = gross_profit * 0.1
        gross_profit += bonus_profit
    
    # This is what actually determines the result
    taxes = apply_tax_rules(gross_profit)
    net_profit = gross_profit - taxes
    
    # Final result is the answer
    crypto_profit = int(net_profit)
    print(f"Target result: {crypto_profit}")
    return crypto_profit

# Execute the calculation
crypto_profit = calculate_final_profit()