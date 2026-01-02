items = ['sensor', 'actuator', 'controller', 'transmitter']
weights = [12.5, 8.3, 19.7, 5.2]
factors = [1, 2, 3, 4]

item_map = {name: idx for idx, name in enumerate(items)}
positions = [item_map[item] for item in items if len(item) > 7]

total_weight = 0
for i, w in enumerate(weights):
    if i % 2 == 0:
        for pos in positions:
            if pos == i:
                total_weight += weights[i] * factors[pos]