#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>
#include <string>
#include <algorithm>

using namespace std;

double complex_calculation(int a, int b) {
    return pow(a, 2) + sqrt(b) - log10(a + b);
}

int main() {
    vector<vector<int>> matrix = {{2, 3, 5}, {7, 11, 13}, {17, 19, 23}};
    vector<int> flat;
    for (const auto& row : matrix) {
        for (int val : row) {
            flat.push_back(val);
        }
    }
    
    int sum = 0;
    for (int val : flat) {
        sum += val;
    }
    
    double avg = static_cast<double>(sum) / flat.size();
    
    int rounded_avg = static_cast<int>(round(avg));
    
    string binary_str = "";
    int temp = rounded_avg;
    while (temp > 0) {
        binary_str = (char)('0' + (temp % 2)) + binary_str;
        temp /= 2;
    }
    
    int bit_count = 0;
    for (char c : binary_str) {
        if (c == '1') bit_count++;
    }
    
    int x = 0;
    for (int i = 0; i < bit_count; i++) {
        x = (x << 1) | 1;
    }
    
    int y = (x & 0xF) ^ (x >> 2);
    
    double z = complex_calculation(y, bit_count);
    
    int final_result = static_cast<int>(floor(z * 100));
    
    cout << "Result: " << final_result << endl;
    
    return 0;
}