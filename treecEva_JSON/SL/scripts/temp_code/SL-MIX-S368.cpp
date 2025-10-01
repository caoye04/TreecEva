#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

int main() {
    vector<vector<int>> matrix = {{2, 3, 5}, {7, 11, 13}, {17, 19, 23}};
    int base = 2;
    int exp = 4;
    int power_result = pow(base, exp);
    
    int sum_primes = 0;
    for (int i = 0; i < matrix.size(); i++) {
        for (int j = 0; j < matrix[i].size(); j++) {
            sum_primes += matrix[i][j];
        }
    }
    
    int bitwise_and = power_result & sum_primes;
    int bitwise_or = power_result | sum_primes;
    int bitwise_xor = power_result ^ sum_primes;
    
    int condition_result = (bitwise_and > 50) ? (bitwise_or + 10) : (bitwise_xor - 5);
    
    vector<int> results = {power_result, sum_primes, bitwise_and, bitwise_or, bitwise_xor, condition_result};
    sort(results.begin(), results.end());
    
    int median = (results[2] + results[3]) / 2;
    
    int factorial = 1;
    for (int i = 1; i <= 5; i++) {
        factorial *= i;
    }
    
    int final_result = (median * 3) + (factorial / 10) - (condition_result % 7);
    
    cout << "Result: " << final_result << endl;
    
    return 0;
}