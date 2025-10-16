#define _USE_MATH_DEFINES
#include <iostream>
#include <string>
#include <functional>

class BracketTokenizer {
private:
    int nesting_depth;
    int innermost_count;

public:
    BracketTokenizer() : nesting_depth(0), innermost_count(0) {}
    
    // State machine for tracking bracket nesting
    void process_token(char token) {
        static enum { START, IN_BRACKET } state = START;
        
        switch(state) {
            case START:
                if (token == '[') {
                    nesting_depth++;
                    state = IN_BRACKET;
                }
                break;
            case IN_BRACKET:
                if (token == '[') {
                    nesting_depth++;
                } else if (token == ']') {
                    nesting_depth--;
                    if (nesting_depth == 0) {
                        // Potential innermost pair completed
                        if (is_balanced_pair()) {
                            innermost_count++;
                        }
                    }
                    if (nesting_depth <= 0) {
                        nesting_depth = 0;  // Reset if unbalanced
                        state = START;
                    }
                }
                break;
        }
    }
    
    // Recursive validation of bracket balance
    bool is_balanced_pair() {
        std::function<bool(int, const std::string&, size_t)> validate;
        validate = [&](int depth, const std::string& s, size_t index) -> bool {
            if (index >= s.length()) return depth == 0;
            if (s[index] == '[') return validate(depth + 1, s, index + 1);
            if (s[index] == ']') {
                if (depth <= 0) return false;
                return validate(depth - 1, s, index + 1);
            }
            return validate(depth, s, index + 1);  // Skip non-bracket chars
        };
        
        std::string test_str = "[[]]";
        return validate(0, test_str, 0);
    }
    
    int get_innermost_count() const { return innermost_count; }
};

int main() {
    BracketTokenizer tokenizer;
    std::string input_sequence = "[[[[][]]]][[][[]]]";
    
    for (char c : input_sequence) {
        tokenizer.process_token(c);
    }
    
    std::cout << "Result: " << tokenizer.get_innermost_count() << std::endl;
    return 0;
}