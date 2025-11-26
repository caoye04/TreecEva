x = 17
y = 42
z = x + y  # irrelevant calculation
result = x if x % 3 == 0 else y
print(f"Result: {result}")