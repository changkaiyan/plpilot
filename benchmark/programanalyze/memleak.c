#include <stdlib.h>

int main() {
    int* ptr;
    
    // Allocate memory
    ptr = malloc(sizeof(int) * 100); 
    
    // Use the memory
    for (int i = 0; i < 100; i++) {
        ptr[i] = i; 
    }
    
    // Forget to free the memory! Leads to memory leak
    printf("Done using memory\n"); 
}