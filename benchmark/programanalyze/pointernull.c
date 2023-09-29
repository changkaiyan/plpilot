#include <stdio.h>

int main() {
    int *ptr = NULL;
    
    // Accessing a null pointer leads to undefined behavior
    *ptr = 5; 
    
    // Dereferencing a null pointer also leads to undefined behavior
    printf("%d\n", *ptr);
}