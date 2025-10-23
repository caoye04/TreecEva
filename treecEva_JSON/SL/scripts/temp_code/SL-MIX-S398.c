#define _USE_MATH_DEFINES
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define POOL_SIZE 1024

unsigned int hash_string(const char* str) {
    unsigned int hash = 5381;
    int c;
    while ((c = *str++))
        hash = ((hash << 5) + hash) + c;
    return hash;
}

int pattern_match(const char* str, const char* pattern) {
    // Simple wildcard pattern matching
    if (*pattern == '\0') return (*str == '\0');
    if (*pattern == '*') return ((*str != '\0' && pattern_match(str+1, pattern)) || pattern_match(str, pattern+1));
    if (*pattern == '?' || *pattern == *str) return pattern_match(str+1, pattern+1);
    return 0;
}

int main() {
    volatile int permissions_mask = 0xF0F0;
    volatile int access_granted = 0;
    
    // Custom memory pool allocation
    void* mem_pool = malloc(POOL_SIZE);
    if (!mem_pool) return -1;
    
    char* user_token = (char*)mem_pool;
    strcpy(user_token, "admin-user-2023");
    
    char* whitelist_pattern = (char*)((char*)mem_pool + 256);
    strcpy(whitelist_pattern, "admin-*-2023");
    
    unsigned int* token_hash = (unsigned int*)((char*)mem_pool + 512);
    *token_hash = hash_string(user_token);
    
    unsigned int* threshold = (unsigned int*)((char*)mem_pool + 516);
    *threshold = 0x12345678;
    
    int pattern_result = pattern_match(user_token, whitelist_pattern);
    
    // Complex access control logic
    access_granted = (pattern_result && 
                    ((*token_hash & permissions_mask) != 0) && 
                    (*token_hash > *threshold)) ? 
                    ((*token_hash ^ 0xDEADBEEF) & 0xFFFF) : 0;
    
    free(mem_pool);
    printf("Result: %d\n", access_granted);
    return 0;
}