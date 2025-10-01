#include <iostream>
#include <string>
#include <cmath>
#include <vector>
using namespace std;

struct DataPoint {
    int x;
    double y;
    string label;
};

int main() {
    vector<DataPoint> points = {{10, 3.5, "alpha"}, {20, 2.0, "beta"}, {30, 1.5, "gamma"}};
    int a = points[0].x;
    double b = points[1].y;
    string s = points[2].label;
    
    int c = (a << 2) & 0xFF;
    double d = pow(b, 3) + sqrt(c);
    
    int e = static_cast<int>(d) ^ 0x0F;
    string sub = s.substr(1, 3);
    int f = sub.length() * 100 + e;
    
    int g = (f >> 3) | (c & 0x07);
    double h = log(static_cast<double>(g)) / log(2.0);
    
    int result = static_cast<int>(h * 1000) % 256;
    
    return 0;
}