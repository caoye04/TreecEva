def find_balance(items, left, right):
    if not items:
        return abs(left - right)
    head, tail = items[0], items[1:]
    include = find_balance(tail, left + head, right - head)
    exclude = find_balance(tail, left, right)
    return min(include, exclude)

weights = [12, 4, 7, 9, 3, 8]
checksum = sum(w ** 2 for w in weights) // len(weights)

equilibrium_point = find_balance(weights, left=0, right=sum(weights))
equilibrium_point = equilibrium_point * 2.5

Result: {equilibrium_point}