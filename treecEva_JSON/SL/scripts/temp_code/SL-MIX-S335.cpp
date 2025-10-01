#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>
#include <string>

using namespace std;

double complex_calc(int a, double b, vector<int>& v) {
    double res = 0.0;
    for (int i = 0; i < v.size(); i++) {
        if (i % 2 == 0) {
            res += pow(v[i], 2) * sin(b);
        } else {
            res -= sqrt(abs(v[i])) * cos(b);
        }
    }
    return res + a;
}

int main() {
    vector<int> data = {4, -9, 16, -25, 36};
    int x = 5;
    double y = 1.5708; // Approximately pi/2
    string s = "Hello";
    
    // Perform bitwise operations
    int mask = 0xF0; // 240 in decimal
    int val = 0x55;  // 85 in decimal
    int bitwise_result = (mask & val) | ((mask ^ val) >> 2);
    
    // Manipulate string
    s += " World";
    int str_len = s.length();
    
    // Complex calculation with function call
    double calc_result = complex_calc(x, y, data);
    
    // Final computation
    double result = 0.0;
    if ((bitwise_result > 30) && (str_len == 11)) {
        result = (calc_result * 2.5) - floor(calc_result / 3.0);
    } else {
        result = (calc_result * 1.5) + ceil(calc_result / 4.0);
    }
    
    // Execution Point Y
    cout << "Result: " << result << endl;
    return 0;
}