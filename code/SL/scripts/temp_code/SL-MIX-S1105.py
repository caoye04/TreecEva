def fib_seq(start1, start2, days):
    seq = [start1, start2]
    for _ in range(2, days):
        seq.append(seq[-1] + seq[-2])
    return seq

croissant_sales = fib_seq(5, 8, 10)
muffin_sales = fib_seq(7, 11, 10)
scone_sales = fib_seq(3, 5, 10)

filtered_total = 0
for i in range(10):
    if croissant_sales[i] >= 20 and muffin_sales[i] >= 15:
        filtered_total += croissant_sales[i] + muffin_sales[i] + scone_sales[i]

print(f"Result: {filtered_total}")