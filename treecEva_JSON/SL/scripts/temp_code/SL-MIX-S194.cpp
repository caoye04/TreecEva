#define _USE_MATH_DEFINES
#include <iostream>
#include <regex>
#include <string>
#include <memory>

int main() {
    std::shared_ptr<int> auth_counter = std::make_shared<int>(0);
    std::string logs[] = {
        "[INFO] User login attempt",
        "[DEBUG] AUTH_SUCCESS for user admin",
        "[ERROR] Failed login for user guest",
        "[DEBUG] AUTH_SUCCESS for user root",
        "[DEBUG] AUTH_SUCCESS for user developer"
    };
    
    std::regex pattern("AUTH_SUCCESS");
    
    for (const auto& log : logs) {
        if (std::regex_search(log, pattern)) {
            (*auth_counter)++;
        }
    }
    
    int final_count = (*auth_counter) % 1000;
    std::cout << "Result: " << final_count << std::endl;
    
    return 0;
}