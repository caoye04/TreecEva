#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>
#include <string>

double computeValue(int n) {
    if (n <= 1) return 1.0;
    double val = 0.0;
    for(int i = 1; i <= n; ++i) {
        val += pow(-1, i+1) * pow(i, 1.0/i);
    }
    return val;
}

int main() {
    std::vector<std::vector<int>> matrix = {{2, 3, 5}, {7, 11, 13}, {17, 19, 23}};
    int product = 1;
    for(const auto& row : matrix) {
        for(int elem : row) {
            product *= elem;
        }
    }
    
    std::string s = "COMPUTE";
    int ascii_sum = 0;
    for(char c : s) {
        ascii_sum += static_cast<int>(c);
    }
    
    double x = computeValue(5);
    int y = static_cast<int>(floor(x * 100));
    
    int result = (product ^ ascii_sum) & y;
    
    std::cout << "Result: " << result << std::endl;
    return 0;
}