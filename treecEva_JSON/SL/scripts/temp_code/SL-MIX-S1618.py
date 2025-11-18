from collections import defaultdict

daily_sales = {
    'chocolate_chip_cookie': 20,
    'banana_bread': 30,
    'croissant': 25,
    'blueberry_muffin': 15,
    'oatmeal_cookie': 10,
    'cinnamon_roll': 40
}

total_sales = sum(daily_sales.values())
half_total = total_sales / 2

high_volume_items = {item for item, qty in daily_sales.items() if qty > half_total}
non_cookie_items = {item for item in daily_sales if 'cookie' not in item}

qualifying_items = high_volume_items & non_cookie_items

print(f"Result: {len(qualifying_items)}")