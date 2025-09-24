import math
from typing import List, Dict, Tuple

class Asset:
    def __init__(self, symbol: str, initial_price: float):
        self.symbol = symbol
        self.current_price = initial_price
        self.price_history = [initial_price]
        self.volatility = 0.0
        self.trend = 0.0
    
    def update_price(self, new_price: float):
        self.price_history.append(new_price)
        if len(self.price_history) > 1:
            returns = [(self.price_history[i] / self.price_history[i-1] - 1) 
                      for i in range(1, len(self.price_history))]
            self.volatility = math.sqrt(sum(r*r for r in returns) / len(returns)) if returns else 0
            self.trend = sum(returns) / len(returns) if returns else 0
        self.current_price = new_price

class Portfolio:
    def __init__(self, initial_cash: float):
        self.cash = initial_cash
        self.positions = {}  # symbol -> quantity
        self.total_profit = 0.0
        self.max_drawdown = 0.0
        self.peak_value = initial_cash
        self.trade_count = 0
        
    def get_position_value(self, asset: Asset) -> float:
        return self.positions.get(asset.symbol, 0) * asset.current_price
    
    def get_total_value(self, assets: List[Asset]) -> float:
        return self.cash + sum(self.get_position_value(asset) for asset in assets)

class RiskManager:
    def __init__(self, max_position_size: float, stop_loss_pct: float):
        self.max_position_size = max_position_size
        self.stop_loss_pct = stop_loss_pct
        self.var_limit = 0.15  # Value at Risk limit
        
    def calculate_position_risk(self, quantity: float, asset: Asset) -> float:
        return abs(quantity) * asset.current_price * asset.volatility
    
    def check_risk_limits(self, portfolio: Portfolio, assets: List[Asset]) -> bool:
        total_risk = sum(self.calculate_position_risk(portfolio.positions.get(asset.symbol, 0), asset) 
                        for asset in assets)
        total_value = portfolio.get_total_value(assets)
        return total_risk / total_value < self.var_limit if total_value > 0 else True

class AdaptiveStrategy:
    def __init__(self):
        self.momentum_threshold = 0.02
        self.mean_reversion_threshold = 0.05
        self.correlation_window = 5
        self.strategy_weights = {'momentum': 0.4, 'mean_reversion': 0.3, 'pairs_trading': 0.3}
        
    def calculate_correlation(self, asset1: Asset, asset2: Asset) -> float:
        # 确保有足够的价格历史数据
        if len(asset1.price_history) < self.correlation_window or len(asset2.price_history) < self.correlation_window:
            return 0.0
        
        # 使用正确的索引范围
        start_idx = max(0, len(asset1.price_history) - self.correlation_window)
        end_idx = len(asset1.price_history)
        
        if end_idx - start_idx < 2:  # 至少需要2个数据点来计算回报率
            return 0.0
        
        returns1 = [asset1.price_history[i] / asset1.price_history[i-1] - 1 
                   for i in range(start_idx + 1, end_idx)]
        returns2 = [asset2.price_history[i] / asset2.price_history[i-1] - 1 
                   for i in range(start_idx + 1, end_idx)]
        
        if not returns1 or not returns2 or len(returns1) != len(returns2):
            return 0.0
            
        mean1, mean2 = sum(returns1) / len(returns1), sum(returns2) / len(returns2)
        cov = sum((returns1[i] - mean1) * (returns2[i] - mean2) for i in range(len(returns1)))
        var1 = sum((r - mean1) ** 2 for r in returns1)
        var2 = sum((r - mean2) ** 2 for r in returns2)
        
        denominator = math.sqrt(var1 * var2)
        return cov / denominator if denominator > 0 else 0.0
    
    def generate_signals(self, assets: List[Asset], portfolio: Portfolio) -> Dict[str, float]:
        signals = {}
        
        for i, asset in enumerate(assets):
            signal_strength = 0.0
            
            # Momentum signal
            if abs(asset.trend) > self.momentum_threshold:
                momentum_signal = 1.0 if asset.trend > 0 else -1.0
                signal_strength += momentum_signal * self.strategy_weights['momentum']
            
            # Mean reversion signal
            if len(asset.price_history) >= 3:
                recent_change = (asset.current_price / asset.price_history[-3]) - 1
                if abs(recent_change) > self.mean_reversion_threshold:
                    reversion_signal = -1.0 if recent_change > 0 else 1.0
                    signal_strength += reversion_signal * self.strategy_weights['mean_reversion']
            
            # Pairs trading signal
            for j, other_asset in enumerate(assets):
                if i != j:
                    correlation = self.calculate_correlation(asset, other_asset)
                    if abs(correlation) > 0.7:  # High correlation
                        if len(asset.price_history) > 0 and len(other_asset.price_history) > 0:
                            spread = (asset.current_price / asset.price_history[0]) - \
                                    (other_asset.current_price / other_asset.price_history[0])
                            if abs(spread) > 0.1:
                                pairs_signal = -0.5 if spread > 0 else 0.5
                                signal_strength += pairs_signal * self.strategy_weights['pairs_trading']
            
            signals[asset.symbol] = signal_strength
        
        return signals

class TradingSystem:
    def __init__(self, initial_cash: float):
        self.portfolio = Portfolio(initial_cash)
        self.risk_manager = RiskManager(max_position_size=0.3, stop_loss_pct=0.05)
        self.strategy = AdaptiveStrategy()
        self.transaction_cost = 0.001  # 0.1% per trade
        self.slippage_factor = 0.0005
        
    def execute_trade(self, asset: Asset, target_quantity: float) -> bool:
        current_quantity = self.portfolio.positions.get(asset.symbol, 0)
        quantity_delta = target_quantity - current_quantity
        
        if abs(quantity_delta) < 0.01:  # Minimum trade size
            return False
        
        # Calculate trade cost with slippage
        trade_value = abs(quantity_delta) * asset.current_price
        slippage = trade_value * self.slippage_factor
        transaction_cost = trade_value * self.transaction_cost
        total_cost = slippage + transaction_cost
        
        # Check if we have enough cash for buy orders
        if quantity_delta > 0:  # Buying
            required_cash = trade_value + total_cost
            if required_cash > self.portfolio.cash:
                return False
            self.portfolio.cash -= required_cash
        else:  # Selling
            self.portfolio.cash += trade_value - total_cost
        
        # Update position
        self.portfolio.positions[asset.symbol] = target_quantity
        self.portfolio.trade_count += 1
        
        return True
    
    def process_market_event(self, assets: List[Asset], new_prices: List[float]):
        # Update asset prices
        for asset, price in zip(assets, new_prices):
            asset.update_price(price)
        
        # Update portfolio metrics
        current_value = self.portfolio.get_total_value(assets)
        if current_value > self.portfolio.peak_value:
            self.portfolio.peak_value = current_value
        
        drawdown = (self.portfolio.peak_value - current_value) / self.portfolio.peak_value
        self.portfolio.max_drawdown = max(self.portfolio.max_drawdown, drawdown)
        
        # Generate trading signals
        signals = self.strategy.generate_signals(assets, self.portfolio)
        
        # Execute trades based on signals and risk management
        for asset in assets:
            if not self.risk_manager.check_risk_limits(self.portfolio, assets):
                continue  # Skip trading if risk limits exceeded
            
            signal = signals.get(asset.symbol, 0)
            current_position = self.portfolio.positions.get(asset.symbol, 0)
            current_value = self.portfolio.get_total_value(assets)
            
            # Calculate target position size
            max_position_value = current_value * self.risk_manager.max_position_size
            if asset.current_price > 0:
                target_quantity = (signal * max_position_value) / asset.current_price
            else:
                target_quantity = 0
            
            # Apply risk scaling based on volatility
            if asset.volatility > 0:
                risk_scaling = min(1.0, 0.1 / asset.volatility)
                target_quantity *= risk_scaling
            
            # Execute trade
            self.execute_trade(asset, target_quantity)
        
        # Update total profit
        initial_value = 10000  # Initial cash
        self.portfolio.total_profit = current_value - initial_value

def run_trading_simulation():
    # Initialize system
    system = TradingSystem(initial_cash=10000)
    
    # Create assets
    assets = [
        Asset("STOCK_A", 100),
        Asset("STOCK_B", 50)
    ]
    
    # Market events: [STOCK_A_price, STOCK_B_price]
    market_events = [
        [100, 50], [102, 48], [98, 52], [105, 49], 
        [99, 53], [103, 47], [97, 55], [106, 46]
    ]
    
    # Process each market event
    for i, event in enumerate(market_events):
        print(f"Processing market event {i+1}: {event}")
        system.process_market_event(assets, event)
        print(f"Portfolio value: {system.portfolio.get_total_value(assets):.2f}")
        print(f"Cash: {system.portfolio.cash:.2f}")
        print(f"Positions: {system.portfolio.positions}")
        print(f"Total profit: {system.portfolio.total_profit:.2f}")
        print("---")
    
    return system.portfolio.total_profit

if __name__ == "__main__":
    result = run_trading_simulation()
    print(f"Final total profit: {result:.2f}")