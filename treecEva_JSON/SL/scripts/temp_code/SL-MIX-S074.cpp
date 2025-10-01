#define M_PI 3.14159265358979323846
#define _USE_MATH_DEFINES
#include <iostream>
#include <map>
#include <vector>
#include <cmath>
#include <string>

using namespace std;

double calculate_expression(double a, double b, int op) {
    switch(op) {
        case 0: return a + b;
        case 1: return a * b;
        case 2: return pow(a, b);
        case 3: return sqrt(abs(a - b));
        default: return 0;
    }
}

int main() {
    map<string, vector<double>> data = {
        {"group1", {2.5, 3.7, 1.2}},
        {"group2", {4.1, 2.8, 5.5}},
        {"group3", {1.9, 3.3, 2.2}}
    };
    
    map<string, double> group_sums;
    for (auto& entry : data) {
        double sum = 0;
        for (double val : entry.second) {
            sum += val * val;
        }
        group_sums[entry.first] = sum;
    }
    
    vector<double> coefficients = {1.5, 2.0, 0.5};
    double weighted_sum = 0;
    int index = 0;
    for (auto& entry : group_sums) {
        weighted_sum += entry.second * coefficients[index % coefficients.size()];
        index++;
    }
    
    int bitwise_op = (5 << 2) & (24 >> 1);
    double trig_result = sin(M_PI / 4) * cos(M_PI / 3);
    
    map<int, map<string, double>> complex_structure;
    complex_structure[bitwise_op]["weighted"] = weighted_sum;
    complex_structure[bitwise_op]["trig"] = trig_result;
    
    double accumulator = 0;
    for (auto& outer_entry : complex_structure) {
        for (auto& inner_entry : outer_entry.second) {
            if (inner_entry.first == "weighted") {
                accumulator += inner_entry.second / 10.0;
            } else {
                accumulator += inner_entry.second * 100;
            }
        }
    }
    
    double final_result = calculate_expression(accumulator, bitwise_op, 2) - (int)(trig_result * 1000);
    
    cout << "Result: " << final_result << endl;
    return 0;
}