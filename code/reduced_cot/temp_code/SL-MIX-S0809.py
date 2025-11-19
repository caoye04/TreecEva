palette = ['FF5733', '33FF57', '3357FF', 'FF33F5', '5733FF']
count = sum(1 for color in palette if int(color[:2], 16) > 128)
print(f"Result: {count}")