#define _USE_MATH_DEFINES
#include <iostream>
#include <memory>

template<int N>
class TribonacciFilter {
public:
    static int compute() {
        if (N == 0) return 1;
        if (N == 1) return 1;
        if (N == 2) return 2;
        
        int prev3 = 1, prev2 = 1, prev1 = 2;
        int current = 0;
        
        for (int i = 3; i <= N; ++i) {
            int sum = prev1 + prev2 + prev3;
            int gcd_val = gcd(prev1, prev2);
            current = sum / gcd_val;
            prev3 = prev2;
            prev2 = prev1;
            prev1 = current;
        }
        return current;
    }
    
private:
    static int gcd(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }
};

template<>
class TribonacciFilter<0> {
public:
    static int compute() { return 1; }
};

template<>
class TribonacciFilter<1> {
public:
    static int compute() { return 1; }
};

template<>
class TribonacciFilter<2> {
public:
    static int compute() { return 2; }
};

int main() {
    auto filter_state = std::make_unique<int>(0);
    
    int tribonacci_result = TribonacciFilter<7>::compute();
    *filter_state = tribonacci_result;
    
    std::cout << "Result: " << tribonacci_result << std::endl;
    return 0;
}