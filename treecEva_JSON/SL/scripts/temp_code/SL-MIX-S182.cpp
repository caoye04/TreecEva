#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <algorithm>

constexpr bool is_prime(int n) {
    if (n <= 1) return false;
    if (n <= 3) return true;
    if (n % 2 == 0 || n % 3 == 0) return false;
    for (int i = 5; i * i <= n; i += 6)
        if (n % i == 0 || n % (i + 2) == 0)
            return false;
    return true;
}

template<int N>
struct Factorial {
    static constexpr int value = N * Factorial<N - 1>::value;
};

template<>
struct Factorial<0> {
    static constexpr int value = 1;
};

int gcd(int a, int b) {
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

int lcm(int a, int b) {
    return (a / gcd(a, b)) * b;
}

int compute_signal_path(int n) {
    if (n <= 1) return 1;
    int path_sum = 0;
    for (int i = 1; i <= n; ++i) {
        if (is_prime(i)) {
            path_sum += i * Factorial<3>::value;
        } else if (i % 2 == 0) {
            path_sum += lcm(i, 4);
        } else {
            path_sum += compute_signal_path(n - 1);
        }
    }
    return path_sum;
}

int main() {
    int base_frequency = 5;
    int modulation_factor = 3;
    bool is_optimal = (base_frequency > 3) && (modulation_factor < 5);
    
    int transmission_efficiency = 0;
    
    if (is_optimal || !is_prime(modulation_factor)) {
        transmission_efficiency = compute_signal_path(base_frequency);
    } else {
        transmission_efficiency = Factorial<4>::value;
    }
    
    std::cout << "Result: " << transmission_efficiency << std::endl;
    return 0;
}