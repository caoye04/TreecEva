import math

def gcd_sum(m, n):
    total = 0
    for i in range(1, m+1):
        for j in range(1, n+1):
            total += math.gcd(i, j)
    return total

# Calculate packaging efficiency for a 4x3 tray
tray_efficiency = gcd_sum(4, 3)
print(f"Result: {tray_efficiency}")