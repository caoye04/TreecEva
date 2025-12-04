# Calculate the total cost for a customer order with tiered discounts

def apply_special_offers(cart_items):
    # This would apply special offers but is not used in this calculation
    special_rates = [0.05, 0.10, 0.15]
    return sum(rate * item for rate, item in zip(special_rates, cart_items))

# Product prices
product_prices = [120, 85, 45, 30, 75]
quantities = [2, 0, 1, 3, 1]

# Calculate base cost before tax
base_items = []
for idx, (price, qty) in enumerate(zip(product_prices, quantities)):
    if qty > 0:
        base_items.append(price * qty)
    else:
        # Skip items with zero quantity
        continue

# Additional processing that doesn't affect the result
potential_savings = [5, 8, 12, 15, 20]
max_potential_discount = max(potential_savings)

# Base cost calculation
base_cost = sum(base_items)

# Tax information
tax_rates = {'standard': 0.08, 'reduced': 0.05, 'exempt': 0.0}
tax_rate = tax_rates['standard']

# Calculate applicable discounts
discounts = []
loyal_customer = True
first_purchase = False
holiday_season = True

if loyal_customer:
    discounts.append(25)
    
    # This branch is never taken due to first_purchase being False
    if first_purchase:
        discounts.append(15)
        
if holiday_season:
    seasonal_discount = 10
    discounts.append(seasonal_discount)
    
# Unused discount calculation
coupon_values = [5, 10, 15]
for i, coupon in enumerate(coupon_values):
    if i % 2 == 0:
        # Even indexed coupons are processed differently
        coupon = coupon * 1.5

# Calculate final price
total_cost = base_cost * (1 + tax_rate) - max(discounts)

# Unused reward points calculation
reward_points = int(total_cost / 10)
bonus_multiplier = 2 if loyal_customer else 1
total_points = reward_points * bonus_multiplier

print(f"Result: {total_cost}")