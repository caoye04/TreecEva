from collections import Counter, defaultdict

def analyze_market_trends(data):
    # Analyze market trends (not relevant to main calculation)
    trend_counter = Counter(data)
    upward_trend = sum(v for k, v in trend_counter.items() if k > 0)
    downward_trend = sum(v for k, v in trend_counter.items() if k < 0)
    
    # Calculate volatility index (distractor)
    volatility = sum(abs(x) for x in data) / len(data) if data else 0
    return upward_trend - downward_trend, volatility

def calculate_portfolio_value(stocks):
    # Main calculation function
    if not stocks:
        return 0
    
    # Extract relevant stock data
    valid_stocks = {}
    for ticker, details in stocks.items():
        if details['active']:
            valid_stocks[ticker] = details['price'] * details['quantity']
    
    # Apply market adjustment factor
    adjustment = 0.85 if sum(valid_stocks.values()) > 10000 else 1.0
    return sum(valid_stocks.values()) * adjustment

# Stock market data
market_data = [-2, 3, -1, 4, 2, -3, 5, 1, -2, 3]
market_trend, volatility_index = analyze_market_trends(market_data)

# Process market sectors (distractor)
sector_performance = defaultdict(list)
sector_performance['tech'] = [5.2, 3.1, -2.0, 7.8]
sector_performance['finance'] = [1.3, -0.5, 2.1, -1.8]
sector_performance['healthcare'] = [3.2, 4.5, 1.2, -0.3]

# Calculate sector averages (distractor)
sector_averages = {}
for sector, values in sector_performance.items():
    sector_averages[sector] = sum(values) / len(values)
    
# Apply sector bias (misleading calculation)
sector_bias = {}
for sector, avg in sector_averages.items():
    bias_factor = 1.0
    if sector == 'tech':
        bias_factor = 1.2
    elif sector == 'finance':
        bias_factor = 0.9
    else:
        bias_factor = 1.1
    sector_bias[sector] = avg * bias_factor

# Stock portfolio data
all_stocks = {
    'AAPL': {'price': 180.5, 'quantity': 15, 'active': True, 'sector': 'tech'},
    'MSFT': {'price': 320.8, 'quantity': 10, 'active': True, 'sector': 'tech'},
    'GOOGL': {'price': 135.2, 'quantity': 8, 'active': False, 'sector': 'tech'},
    'JPM': {'price': 145.6, 'quantity': 12, 'active': True, 'sector': 'finance'},
    'BAC': {'price': 32.4, 'quantity': 30, 'active': False, 'sector': 'finance'},
    'JNJ': {'price': 160.2, 'quantity': 5, 'active': True, 'sector': 'healthcare'}
}

# Apply market conditions (distractor)
if market_trend > 0:
    for ticker in all_stocks:
        if all_stocks[ticker]['sector'] in sector_bias:
            # This adjustment doesn't actually affect the portfolio calculation
            all_stocks[ticker]['market_sentiment'] = sector_bias[all_stocks[ticker]['sector']]

# Filter stocks based on complex conditions
filtered_stocks = {}
for ticker, details in all_stocks.items():
    # Misleading condition (looks important but isn't used)
    sentiment_threshold = 3.0
    has_positive_sentiment = details.get('market_sentiment', 0) > sentiment_threshold
    
    # The actual filtering just copies active stocks
    if details['active']:
        filtered_stocks[ticker] = details

# Calculate portfolio statistics (distractors)
total_quantity = sum(details['quantity'] for details in filtered_stocks.values())
average_price = sum(details['price'] for details in filtered_stocks.values()) / len(filtered_stocks) if filtered_stocks else 0

# This is our target calculation
stock_value = calculate_portfolio_value(filtered_stocks)

# More distractor calculations
diversification_score = len(set(details['sector'] for details in filtered_stocks.values())) * 100
risk_factor = volatility_index * (1 - len(filtered_stocks) / len(all_stocks))
projected_growth = stock_value * (1 + market_trend / 100) - stock_value

print(f"Total stocks: {len(filtered_stocks)}")
print(f"Average price: {average_price:.2f}")
print(f"Diversification: {diversification_score}")
print(f"Risk factor: {risk_factor:.2f}")
print(f"Result: {stock_value}")