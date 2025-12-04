# E-commerce order processing system

base_prices = [120, 85, 199, 45, 250]
discount_rate = 0.15
tax_rate = 0.08
shipping_fee = 12.50
promotion_threshold = 500
promotion_amount = 50

# Customer loyalty tiers
loyalty_tiers = {'bronze': 0.05, 'silver': 0.10, 'gold': 0.15}
customer_tier = 'silver'

# Apply tier-based discount first
tier_discount = loyalty_tiers[customer_tier]
discounted_prices = [price * (1 - tier_discount) for price in base_prices]

# Apply seasonal promotion if applicable
original_sum = sum(base_prices)
discounted_sum = sum(discounted_prices)
savings = original_sum - discounted_sum

# Calculate handling fees (not used in final calculation)
handling_fees = [max(5, price * 0.02) for price in base_prices]
total_handling = sum(handling_fees)

# Apply additional discount for bulk orders
bulk_discount = discount_rate if discounted_sum > 400 else 0
after_bulk_discount = [price * (1 - bulk_discount) for price in discounted_prices]

# Apply store credit if eligible
store_credit = 25 if customer_tier in ['silver', 'gold'] else 0
store_credit = 0 if bulk_discount > 0 else store_credit  # Can't combine discounts

# Calculate taxes
pretax_prices = after_bulk_discount
taxes = [price * tax_rate for price in pretax_prices]

# Calculate final prices including tax
final_prices = [pretax + tax for pretax, tax in zip(pretax_prices, taxes)]

# Apply promotional discount if threshold met
subtotal = sum(final_prices)
promo_discount = promotion_amount if subtotal > promotion_threshold else 0

# Calculate final amount with shipping
total_before_shipping = subtotal - promo_discount - store_credit
total_revenue = sum(final_prices)

# Final amount customer pays
final_amount = total_before_shipping + shipping_fee

print(f"Result: {total_revenue}")