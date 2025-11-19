monthly_celsius = [2.3, 4.1, 7.8, 12.5, 17.2, 21.0, 23.4, 22.1, 18.7, 13.3, 7.9, 3.6]

celsius_to_fahrenheit = lambda c: c * 9/5 + 32

monthly_fahrenheit = [celsius_to_fahrenheit(temp) for temp in monthly_celsius]

sorted_fahrenheit = sorted(monthly_fahrenheit, reverse=True)

average_top3_fahrenheit = sum(sorted_fahrenheit[:3]) / 3.0

print(f"Result: {average_top3_fahrenheit}")