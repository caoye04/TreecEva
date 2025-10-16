#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>

int main() {
    std::vector<std::string> book_titles = {
        "The Great Gatsby",
        "To Kill a Mockingbird",
        "The Catcher in the Rye",
        "Pride and Prejudice",
        "The Lord of the Rings"
    };
    
    std::string favorite_word = "The";
    int match_counter = 0;
    
    for (const auto& title : book_titles) {
        std::istringstream iss(title);
        std::vector<std::string> tokens;
        std::string word;
        
        while (iss >> word) {
            tokens.push_back(word);
        }
        
        std::sort(tokens.begin(), tokens.end());
        
        if (!tokens.empty() && tokens[0] == favorite_word) {
            match_counter++;
        }
    }
    
    std::cout << "Result: " << match_counter << std::endl;
    return 0;
}