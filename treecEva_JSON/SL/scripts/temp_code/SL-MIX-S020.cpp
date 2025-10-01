#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <map>
#include <cmath>
#include <string>

using namespace std;

double complex_calc(int a, double b, string s) {
    double res = 0.0;
    for (char c : s) {
        res += (c - 'a' + 1);
    }
    return pow(a, b) + log(res + 1);
}

int main() {
    vector<map<string, int>> data = {
        {{"x", 2}, {"y", 3}},
        {{"x", 5}, {"y", 7}},
        {{"x", 11}, {"y", 13}}
    };
    
    double accumulator = 0.0;
    int counter = 0;
    
    for (auto& m : data) {
        int x = m["x"];
        int y = m["y"];
        
        if ((x & y) > 0) {
            accumulator += complex_calc(x, y, string(1, char('a' + counter)));
        } else {
            accumulator -= sqrt(x + y);
        }
        
        counter++;
    }
    
    int bitwise_xor = data[0]["x"] ^ data[1]["y"];
    int shift_result = bitwise_xor << 1;
    
    double final_result = (accumulator * shift_result) / (counter + 1);
    
    cout << "Result: " << final_result << endl;
    
    return 0;
}