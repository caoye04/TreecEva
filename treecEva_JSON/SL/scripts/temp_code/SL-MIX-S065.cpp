#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <map>
#include <cmath>
#include <string>

using namespace std;

double compute_expression(int a, int b, double c) {
    return pow(a, 2) + sqrt(b) * c - (a % b);
}

int main() {
    vector<int> nums = {3, 5, 7, 11, 13};
    map<string, double> constants = {{"pi", 3.14159}, {"e", 2.71828}};
    
    int x = nums[0] * nums[2];
    int y = nums[4] - nums[1];
    double z = constants["pi"] * nums[3];
    
    double expr1 = compute_expression(x, y, z);
    
    string label = "result_" + to_string(y);
    constants[label] = expr1;
    
    int bit_xor = (x & 0xF) ^ (y | 0x3);
    int shifted = (bit_xor << 2) >> 1;
    
    double trig_part = sin(constants["pi"]/2) * cos(0) + tan(constants["pi"]/4);
    
    double final_result = (constants[label] + shifted) * trig_part;
    
    cout << "Result: " << final_result << endl;
    
    return 0;
}