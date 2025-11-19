chocolate_chip_count = 480
oatmeal_raisin_count = 720

gcd_value = lambda a, b: a if b == 0 else gcd_value(b, a % b)
package_size = gcd_value(chocolate_chip_count, oatmeal_raisin_count)
total_packages = (chocolate_chip_count + oatmeal_raisin_count) // package_size if package_size > 0 else 0

cookie_distribution = [package_size for _ in range(total_packages)]
unique_package_count = len(set(cookie_distribution))
final_result = unique_package_count if unique_package_count > 0 else -1

print(f'Result: {final_result}')