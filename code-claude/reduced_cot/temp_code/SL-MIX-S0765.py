from collections import Counter
import itertools

def calculate_optimal_discount(history, cart):
    # Analysis of purchase history
    item_counts = Counter(itertools.chain.from_iterable(history))
    
    # Calculate loyalty score (not used in final calculation)
    loyalty_score = sum(item_counts.values()) / len(item_counts)
    
    # Extract current cart value
    cart_total = sum(cart.values())
    
    # Potential discounts based on different criteria
    volume_discount = 0.05 if cart_total > 150 else 0
    
    # Item popularity discount (not used in final calculation)
    popular_items = [item for item, count in item_counts.items() if count > 2]
    popularity_bonus = len([item for item in cart.keys() if item in popular_items]) * 0.01
    
    # Calculate seasonal multiplier
    season_code = 'SUMMER'
    season_multiplier = sum([ord(c) % 5 for c in season_code]) / 10
    
    # First-time buyer check (distraction - all buyers have history)
    first_time_bonus = 0.10 if not history else 0
    
    # Tier-based discount calculation
    tier_threshold = [100, 200, 300]
    tier_rates = [0.02, 0.05, 0.08]
    
    tier_discount = 0
    for threshold, rate in zip(tier_threshold, tier_rates):
        if cart_total > threshold:
            tier_discount = rate
    
    # Apply seasonal effect to tier discount
    tier_discount = tier_discount * season_multiplier
    
    # Calculate optimal discount percentage
    optimal_discount = max(volume_discount, tier_discount) * 100
    
    # Apply rounding for marketing purposes
    return round(optimal_discount, 1)

# Purchase history - list of previous purchases
purchase_history = [
    ['shoes', 'shirt', 'pants'],
    ['shoes', 'accessory'],
    ['shirt', 'socks', 'accessory']
]

# Current shopping cart - item:price mapping
current_cart = {
    'shoes': 95.00,
    'jacket': 120.00,
    'scarf': 25.50
}

# Calculate the optimal discount for this customer
optimal_discount = calculate_optimal_discount(purchase_history, current_cart)
print(f"Result: {optimal_discount}")
