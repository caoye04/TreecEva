product_data = "item1:25,item2:18,item3:32,item4:21"
items = product_data.split(',')
price_list = []

for item in items:
    _, price = item.split(':')
    price_list.append(int(price))

enumerate_data = [idx * value for idx, value in enumerate(price_list)]
processed_total = sum(enumerate_data)

print(f"Result: {processed_total}")