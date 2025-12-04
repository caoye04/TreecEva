from collections import Counter

# Calculate customer discount based on purchase history
item_purchases = ["book", "electronics", "book", "clothing", "electronics", "book"]
purchase_counts = Counter(item_purchases)

# Customer details
membership_tier = "gold"  # Options: standard, silver, gold, platinum
purchase_years = 3  # Years as a customer

# Calculate base discount from purchase frequency
base_discount = sum(count for item, count in purchase_counts.items() if count > 1) * 2.5

# Premium tier discounts
tier_discounts = {
    "standard": 0,
    "silver": 5,
    "gold": 10,
    "platinum": 15
}

premium_discount = tier_discounts.get(membership_tier, 0)

# Loyalty bonus calculation
loyalty_bonus = purchase_years * 2

# Determine final discount - take either base discount or the smaller of premium and loyalty
total_discount = max(base_discount, min(premium_discount, loyalty_bonus))

print(f"Result: {total_discount}")