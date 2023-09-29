#include <iostream>

int add(int a, int b) {
    // Precondition: <<a > 0 && b > 0>>
    
    
    // Add numbers 
    int result = a + b;
    
    // Postcondition: <<result > a && result > b>>
    
    return result; 
}

int main() {  
    std::cout << add(2, 3) << std::endl;   // Prints 5
    std::cout << add(0, 5) << std::endl;   // Prints <<Precondition violated!>> 
                                            // Prints 0 
    std::cout << add(3, 2) << std::endl;   // Prints <<Postcondition violated!>>
                                            // Prints 0
}