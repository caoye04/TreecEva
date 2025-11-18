from statistics import median

temperatures = [12, 15, 14, 10, 16, 13, 11]
median_temp = median(temperatures)
squared_differences = [(temp - median_temp) ** 2 for temp in temperatures]
fluctuation_index = sum(squared_differences)

print(f"Result: {fluctuation_index}")