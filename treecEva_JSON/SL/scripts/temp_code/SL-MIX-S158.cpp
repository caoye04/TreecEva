#define _USE_MATH_DEFINES
#include <iostream>
#include <map>
#include <vector>
#include <cmath>
#include <string>

using namespace std;

int main() {
    map<string, vector<int>> data = {
        {"alpha", {2, 4, 6, 8}},
        {"beta", {1, 3, 5, 7}},
        {"gamma", {10, 20, 30}}
    };
    
    map<string, double> processed;
    
    for (auto& entry : data) {
        double sum = 0;
        for (int val : entry.second) {
            sum += pow(val, 2) + log(val + 1);
        }
        processed[entry.first] = sum;
    }
    
    vector<double> temp;
    for (auto& p : processed) {
        temp.push_back(p.second);
    }
    
    double product = 1;
    for (double val : temp) {
        product *= val;
    }
    
    int bit_mask = 0xF0;  // 240 in decimal
    int shift_val = 3;
    int bitwise_result = (static_cast<int>(product) & bit_mask) >> shift_val;
    
    double trig_result = sin(processed["alpha"]) + cos(processed["beta"]); 
    
    double final_result = bitwise_result ^ static_cast<int>(trig_result * 1000);
    
    cout << "Result: " << final_result << endl;
    
    return 0;
}