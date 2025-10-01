#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>

using namespace std;

double compute_expression(int a, int b, double c) {
    return pow(a, 2) + sqrt(b) * sin(c);
}

int bitwise_transform(int x, int y) {
    return (x << 2) ^ (y >> 1) & 0xF;
}

string process_string(const string& s, int shift) {
    string res = s;
    for (char& ch : res) {
        if (isalpha(ch)) {
            if (islower(ch)) {
                ch = ((ch - 'a' + shift) % 26) + 'a';
            } else {
                ch = ((ch - 'A' + shift) % 26) + 'A';
            }
        }
    }
    return res;
}

int main() {
    vector<vector<int>> matrix = {{2, 3, 5}, {7, 11, 13}, {17, 19, 23}};
    
    int sum_primes = 0;
    for (const auto& row : matrix) {
        for (int val : row) {
            sum_primes += val;
        }
    }
    
    double expr_result = compute_expression(matrix[1][1], sum_primes, 1.5708);
    
    string secret = "XyZ";
    string transformed = process_string(secret, 3);
    
    int hash_code = 0;
    for (char c : transformed) {
        hash_code = (hash_code * 31) + static_cast<int>(c);
    }
    
    int bitwise_val = bitwise_transform(hash_code, static_cast<int>(expr_result));
    
    vector<double> logs;
    for (int i = 1; i <= 5; ++i) {
        logs.push_back(log(static_cast<double>(i * 10)));
    }
    
    double log_sum = 0;
    for (double l : logs) {
        log_sum += l;
    }
    
    int result = static_cast<int>(expr_result) ^ bitwise_val ^ static_cast<int>(log_sum);
    
    cout << "Result: " << result << endl;
    
    return 0;
}