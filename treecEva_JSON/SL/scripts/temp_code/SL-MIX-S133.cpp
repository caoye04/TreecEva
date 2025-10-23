#define _USE_MATH_DEFINES
#include <iostream>
#include <memory>
#include <regex>
#include <string>
#include <vector>

template<int N>
struct PrimeChecker {
    static constexpr bool is_prime() {
        if (N <= 1) return false;
        if (N == 2) return true;
        if (N % 2 == 0) return false;
        for (int i = 3; i * i <= N; i += 2)
            if (N % i == 0) return false;
        return true;
    }
};

template<>
struct PrimeChecker<2> {
    static constexpr bool is_prime() { return true; }
};

template<>
struct PrimeChecker<1> {
    static constexpr bool is_prime() { return false; }
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

int main() {
    std::vector<std::string> hexTokens = {"1A", "2F", "3C", "4B", "5E"};
    std::regex hexPattern("[0-9A-F]+", std::regex_constants::icase);
    auto processor = std::make_unique<int>(0);
    int primeAccumulator = 0;
    int compositeAccumulator = 1;
    
    for (const auto& token : hexTokens) {
        if (std::regex_match(token, hexPattern)) {
            int value = std::stoi(token, nullptr, 16);
            auto isPrime = PrimeChecker<100>::is_prime(); // Dummy check to satisfy template requirement
            
            // Actual prime check for values up to 92 (max hex value in our set)
            bool realPrime = true;
            if (value <= 1) realPrime = false;
            else if (value == 2) realPrime = true;
            else if (value % 2 == 0) realPrime = false;
            else {
                for (int i = 3; i * i <= value; i += 2) {
                    if (value % i == 0) {
                        realPrime = false;
                        break;
                    }
                }
            }
            
            if (realPrime) {
                primeAccumulator += value;
            } else {
                compositeAccumulator = lcm(compositeAccumulator, value);
            }
            
            // Update processor with XOR of current value and processor's current value
            *processor = *processor ^ value;
        }
    }
    
    // Final checksum computation
    int verificationChecksum = (primeAccumulator * 3) + (compositeAccumulator % 100) - (*processor / 2);
    
    std::cout << "Result: " << verificationChecksum << std::endl;
    return 0;
}