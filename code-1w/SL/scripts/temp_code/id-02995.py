from collections import Counter
def calculate_score(items, factors):
    count = Counter(items)
    total = 0
    for key in count:
        if key in factors:
            total += count[key] * factors[key]
    return total

def main():
    data = ('apple', 'banana', 'apple', 'cherry', 'banana', 'apple')
    weights = {'apple': 3, 'banana': 2, 'cherry': 1}
    temp_value = sum(len(item) for item in data)  # Irrelevant calculation
    unused_list = [1, 2, 3, 4]
    result = calculate_score(data, weights)
    print(f"Result: {result}")

main()