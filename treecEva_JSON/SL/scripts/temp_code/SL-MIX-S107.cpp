#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

class FibonacciMod {
private:
    vector<int> fib_cache;
    int mod;

public:
    FibonacciMod(int modulo) : mod(modulo) {
        fib_cache.push_back(0);
        fib_cache.push_back(1);
    }
    
    int get(int n) {
        while (fib_cache.size() <= n) {
            int next = (fib_cache[fib_cache.size()-1] + fib_cache[fib_cache.size()-2]) % mod;
            fib_cache.push_back(next);
        }
        return fib_cache[n];
    }
};

int main() {
    FibonacciMod fib_mod(100);
    vector<int> node_values;
    
    // Level 0: 1 node (index 1)
    // Level 1: 2 nodes (indices 2,3)
    // Level 2: 4 nodes (indices 4,5,6,7)
    // Level 3: 8 nodes (indices 8,9,10,11,12,13,14,15)
    
    for (int i = 1; i <= 15; i++) {
        node_values.push_back(fib_mod.get(i));
    }
    
    int total_sum = accumulate(node_values.begin(), node_values.end(), 0);
    
    cout << "Result: " << total_sum << endl;
    return 0;
}