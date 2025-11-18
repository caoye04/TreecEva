cookie_sales = {
    'chocolate_chip': {101, 102, 103, 104, 105},
    'oatmeal_raisin': {103, 104, 105, 106, 107},
    'sugar_cookie': {108, 109}
}

promotion_qualifiers = cookie_sales['chocolate_chip'] & cookie_sales['oatmeal_raisin']
qualifying_customer_count = len(promotion_qualifiers)
print(f'Result: {qualifying_customer_count}')