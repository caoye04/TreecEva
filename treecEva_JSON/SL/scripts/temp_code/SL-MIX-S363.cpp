#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

constexpr bool is_prime(int n) {
    if (n <= 1) return false;
    if (n <= 3) return true;
    if (n % 2 == 0 || n % 3 == 0) return false;
    for (int i = 5; i * i <= n; i += 6)
        if (n % i == 0 || n % (i + 2) == 0)
            return false;
    return true;
}

int gcd(int a, int b) {
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

int main() {
    std::vector<int> cipher_keys = {77, 143, 91, 195, 133};
    int security_index = 0;
    
    for (size_t i = 0; i < cipher_keys.size(); ++i) {
        int key = cipher_keys[i];
        int factor_count = 0;
        
        for (int j = 2; j <= key; ++j) {
            if (is_prime(j) && key % j == 0) {
                factor_count++;
            }
        }
        
        if (factor_count > 1) {
            security_index += factor_count * gcd(key, static_cast<int>(i+1));
        } else {
            security_index -= key;
        }
    }
    
    std::cout << "Result: " << security_index << std::endl;
    return 0;
}