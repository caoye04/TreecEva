total = 0
outer_noise = 0
for i in range(3):
    outer_noise += i
    for j in range(2):
        total = total + i * j
        inner_noise = j ** 2
result = total