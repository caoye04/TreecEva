#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>
#include <string>

using namespace std;

int main() {
    // Initialize variables
    int x = 15;
    int y = 28;
    double z = 3.7;
    
    // Bitwise operations
    int a = (x & y) | ((int)z << 2);
    int b = (x ^ y) & (~(int)z);
    
    // Mathematical operations
    double c = pow(z, 2.5) + log(z + 2.0);
    int d = (int)(c * 100) % 128;
    
    // String operations
    string s1 = "Hello";
    string s2 = "World";
    string s3 = s1 + s2;
    int e = s3.length() * 3 - (s1[0] - 'A');
    
    // Vector operations
    vector<int> v = {a, b, d, e};
    int f = 0;
    for(int i = 0; i < v.size(); i++) {
        f += v[i] * (i + 1);
    }
    
    // Complex calculation
    int g = (f >> 2) ^ (e & d);
    double h = sqrt(g + c);
    int final_result = (int)(h * 1000) % 10000;
    
    cout << "Result: " << final_result << endl;
    return 0;
}