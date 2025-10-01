#define M_PI 3.14159265358979323846
#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>
#include <string>

using namespace std;

double complex_calculation(int a, int b, double c) {
    return pow(a, 2) + sqrt(b) * c - (a & b);
}

int main() {
    vector<vector<int>> matrix = {{2, 3, 5}, {7, 11, 13}, {17, 19, 23}};
    vector<double> results;
    string key = "CRYPTO";
    int shift = 3;
    double accumulator = 0.0;
    
    for (int i = 0; i < matrix.size(); i++) {
        for (int j = 0; j < matrix[i].size(); j++) {
            int value = matrix[i][j];
            double calc = complex_calculation(value, i+j, 1.5);
            results.push_back(calc);
        }
    }
    
    for (int i = 0; i < results.size(); i++) {
        accumulator += results[i];
    }
    
    int xor_result = 0;
    for (char c : key) {
        xor_result ^= (int)c;
    }
    
    int bit_shifted = (xor_result << shift) | (xor_result >> (32-shift));
    
    double final_result = accumulator + bit_shifted - (M_PI * 100);
    
    // Execution point Y
    cout << "Result: " << final_result << endl;
    
    return 0;
}