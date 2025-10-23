#define _USE_MATH_DEFINES
#include <iostream>
#include <string>
#include <vector>

constexpr int TOKEN_NUMBER = 1;
constexpr int TOKEN_OPERATOR = 2;
constexpr int TOKEN_IDENTIFIER = 4;

constexpr int classify_token(const std::string& token) {
    if (token.empty()) return 0;
    if (std::isdigit(token[0])) return TOKEN_NUMBER;
    if (token == "+" || token == "-" || token == "*" || token == "/") return TOKEN_OPERATOR;
    return TOKEN_IDENTIFIER;
}

int process_tokens_recursive(const std::vector<std::string>& tokens, size_t index, int accumulated_flags) {
    if (index >= tokens.size()) return accumulated_flags;
    
    int current_flag = classify_token(tokens[index]);
    bool is_valid = (current_flag != 0) && !(accumulated_flags & current_flag);
    
    if (is_valid) {
        return process_tokens_recursive(tokens, index + 1, accumulated_flags | current_flag);
    } else {
        return process_tokens_recursive(tokens, index + 1, accumulated_flags & ~current_flag);
    }
}

int main() {
    std::vector<std::string> token_sequence = {"var1", "+", "123", "*", "func"};
    int initial_flags = TOKEN_NUMBER | TOKEN_OPERATOR;
    int final_token_flags = process_tokens_recursive(token_sequence, 0, initial_flags);
    std::cout << "Result: " << final_token_flags << std::endl;
    return 0;
}