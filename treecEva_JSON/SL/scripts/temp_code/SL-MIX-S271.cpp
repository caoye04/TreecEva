#define _USE_MATH_DEFINES
#include <iostream>
#include <queue>
#include <vector>
#include <string>
#include <cmath>
#include <functional>

using namespace std;

typedef long long ll;

ll mod_exp(ll base, ll exp, ll mod) {
    ll result = 1;
    base %= mod;
    while (exp > 0) {
        if (exp & 1) result = (result * base) % mod;
        base = (base * base) % mod;
        exp >>= 1;
    }
    return result;
}

int main() {
    const ll MOD = 1000000007;
    vector<string> tokens = {"alpha", "beta", "gamma", "delta"};
    priority_queue<pair<ll, string>, vector<pair<ll, string>>, greater<>> min_heap;
    
    ll hash_accumulator = 0;
    for (const auto& token : tokens) {
        ll hash_val = 0;
        for (char c : token) {
            hash_val = (hash_val * 31 + c) % MOD;
        }
        ll power_result = mod_exp(hash_val, 3, MOD);
        hash_accumulator = (hash_accumulator + power_result) % MOD;
        min_heap.push({power_result, token});
    }
    
    while (!min_heap.empty()) {
        auto [val, str] = min_heap.top();
        min_heap.pop();
        ll log_val = static_cast<ll>(log(val + 1));
        hash_accumulator = (hash_accumulator + log_val) % MOD;
    }
    
    ll final_hash = hash_accumulator;
    cout << "Result: " << final_hash << endl;
    return 0;
}