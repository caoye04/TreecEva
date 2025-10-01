#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>
#include <string>

double computeValue(int n) {
    double sum = 0.0;
    for (int i = 1; i <= n; ++i) {
        sum += std::pow(-1, i + 1) / (2 * i - 1);
    }
    return sum * 4;
}

int main() {
    std::vector<std::vector<int>> matrix = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    int a = matrix[1][2];
    int b = matrix[2][0];
    
    double x = computeValue(10000);
    int y = static_cast<int>(std::round(x));
    
    std::string s = "HELLO";
    int z = 0;
    for (char c : s) {
        z += (c - 'A' + 1);
    }
    
    int result = (a & b) | (y ^ z);
    result <<= 2;
    result -= (matrix[0][0] * matrix[2][2]);
    
    std::cout << "Result: " << result << std::endl;
    return 0;
}