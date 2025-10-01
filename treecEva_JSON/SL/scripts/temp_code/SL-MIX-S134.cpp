#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <map>
#include <cmath>
#include <string>

using namespace std;

double complexCalculation(int a, int b, double c) {
    return pow(a, 2) + sqrt(b) * sin(c);
}

int main() {
    // Initialize complex nested data structures
    vector<map<string, vector<int>>> data = {
        {{"group1", {12, 24, 36}}, {"group2", {5, 10, 15}}},
        {{"group3", {7, 14, 21}}, {"group4", {3, 6, 9}}}
    };
    
    // Mathematical constants
    double pi = 3.14159;
    double e = 2.71828;
    
    // Initialize variables
    int x = data[0]["group1"][1];  // 24
    int y = data[1]["group3"][2];  // 21
    double z = pi * e;
    
    // Perform complex calculations
    double val1 = complexCalculation(x, y, z);
    double val2 = log(val1) + cos(x * y);
    
    // String manipulations for index calculations
    string s1 = "compute";
    string s2 = "process";
    int lenDiff = abs(static_cast<int>(s1.length()) - static_cast<int>(s2.length()));
    
    // Update data structure based on calculations
    data[0]["group1"][0] = static_cast<int>(val2) % 100;
    
    // Bitwise operations
    int bitwise = (x & y) | (lenDiff << 2);
    
    // Multiple assignment and tuple unpacking simulation
    int a, b, c;
    a = b = c = 0;
    if (val2 > 100) {
        a = static_cast<int>(val2 / 10);
        b = static_cast<int>(val2 / 100);
        c = static_cast<int>(val2 / 1000);
    } else {
        a = x;
        b = y;
        c = lenDiff;
    }
    
    // Final calculation sequence
    double result = 0;
    for (int i = 0; i < 3; i++) {
        result += pow(data[0]["group1"][i], 1.5) * sin(bitwise + i);
    }
    
    result = result / (a + b + c + 1);
    result = floor(result * 1000) / 1000; // Round to 3 decimal places
    
    // Execution Point Y
    cout << "Result: " << result << endl;
    
    return 0;
}