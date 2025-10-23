#define _USE_MATH_DEFINES
#include <iostream>
#include <string>
#include <vector>

constexpr long long MOD = 1000000007;
constexpr long long BASE = 31;

template<typename T>
constexpr T power(T base, int exp, T mod) {
    T result = 1;
    while (exp > 0) {
        if (exp % 2 == 1) result = (result * base) % mod;
        base = (base * base) % mod;
        exp /= 2;
    }
    return result;
}

int main() {
    std::vector<std::string> tokens = {"123", "+", "(", "abc", "*", ")", "-", "456"};
    long long hash_value = 0;
    int position = 0;
    
    enum State { START, NUMBER, OPERATOR, PAREN };
    State current_state = START;
    
    auto process_char = [&](char c) -> State {
        if (c >= '0' && c <= '9') return NUMBER;
        else if (c == '+' || c == '-' || c == '*' || c == '/') return OPERATOR;
        else if (c == '(' || c == ')') return PAREN;
        else return START;
    };
    
    for (const auto& token : tokens) {
        for (char c : token) {
            current_state = process_char(c);
            if (current_state == OPERATOR) {
                long long char_val = static_cast<long long>(c) - '0' + 1;
                long long term = (char_val * power(BASE, position, MOD)) % MOD;
                hash_value = (hash_value + term) % MOD;
                position++;
            }
        }
    }
    
    long long final_hash = hash_value;
    std::cout << "Result: " << final_hash << std::endl;
    return 0;
}