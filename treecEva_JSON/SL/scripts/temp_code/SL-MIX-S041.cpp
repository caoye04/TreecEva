#define M_PI 3.14159265358979323846
#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>
#include <string>

using namespace std;

double computeExpression(double x, int n) {
    double sum = 0.0;
    for (int i = 1; i <= n; ++i) {
        sum += pow(x, i) / tgamma(i + 1); // tgamma(n) = (n-1)!
    }
    return sum;
}

int main() {
    vector<vector<int>> matrix = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    vector<int> flat;
    
    // Flatten the matrix
    for (const auto& row : matrix) {
        for (int val : row) {
            flat.push_back(val);
        }
    }
    
    // Compute sum of squares
    long long sumOfSquares = 0;
    for (int val : flat) {
        sumOfSquares += static_cast<long long>(val) * val;
    }
    
    // Perform modular arithmetic
    int modulus = 1000000007;
    long long modSum = sumOfSquares % modulus;
    
    // Bitwise operations
    int xorResult = 0;
    for (int val : flat) {
        xorResult ^= val;
    }
    
    // Trigonometric adjustment
    double angle = static_cast<double>(xorResult);
    double sinAdjustment = sin(angle * M_PI / 180.0);
    
    // String manipulation
    string s = "COMPUTE";
    int charSum = 0;
    for (char c : s) {
        charSum += static_cast<int>(c);
    }
    
    // Final computation
    double intermediate = computeExpression(sinAdjustment, 10);
    double result = intermediate * modSum + charSum;
    
    cout << "Result: " << static_cast<long long>(round(result)) % modulus << endl;
    
    return 0;
}