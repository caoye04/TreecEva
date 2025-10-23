#define _USE_MATH_DEFINES
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX_TOKENS 16
#define TOKEN_SIZE 32

struct Token {
    char value[TOKEN_SIZE];
    int priority;
};

struct ConfigParser {
    struct Token tokens[MAX_TOKENS];
    int count;
    volatile int checksum;
};

void tokenize(struct ConfigParser* parser, const char* input) {
    char* input_copy = strdup(input);
    char* token = strtok(input_copy, ",");
    
    while (token != NULL && parser->count < MAX_TOKENS) {
        strncpy(parser->tokens[parser->count].value, token, TOKEN_SIZE-1);
        parser->tokens[parser->count].value[TOKEN_SIZE-1] = '\0';
        parser->tokens[parser->count].priority = strlen(token) > 4 ? 2 : 1;
        parser->count++;
        token = strtok(NULL, ",");
    }
    free(input_copy);
}

int compute_checksum(struct ConfigParser* parser) {
    int sum = 0;
    for (int i = 0; i < parser->count; i++) {
        int val = 0;
        for (int j = 0; parser->tokens[i].value[j] != '\0'; j++) {
            val = (val << 3) ^ parser->tokens[i].value[j];
        }
        sum += (val & 0xFF) * parser->tokens[i].priority;
    }
    return sum;
}

int transform_value(int input) {
    return ((input >> 2) & 0x3F) ^ (input & 0x3F);
}

int main() {
    struct ConfigParser parser = {0};
    const char* config = "ethernet,wifi,bluetooth,usb,pcie,nvme,sata,usb3";
    
    tokenize(&parser, config);
    
    int raw_checksum = compute_checksum(&parser);
    
    // Apply conditional transformation based on checksum properties
    int transformed = (raw_checksum % 7 == 0) ? 
        transform_value(raw_checksum) : 
        (raw_checksum & 0xFF) | ((raw_checksum >> 8) & 0xFF);
    
    // Final checksum calculation with short-circuit evaluation
    int final_checksum = (transformed > 100 && parser.count > 5) ? 
        transformed ^ 0xAA : 
        (transformed < 50 || parser.count < 3) ? 
            transformed + 0x55 : 
            transformed;
    
    printf("Result: %d\n", final_checksum);
    return 0;
}