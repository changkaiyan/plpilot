
#include <iostream>

int main() {
    // Variables 
    bool a = true;
    bool b = false;
    bool c = true;
    
    // Verification statement 
    if (a && b -> c) { 
        std::cout << "a && b -> c is true" << std::endl;
    } else {
        std::cout << "a && b -> c is false" << std::endl; 
    }
    <<!(a && b -> c)>>
    // Output: a && b -> c is false 
    
    // Variables 
    bool x = true;
    bool y = true; 
    bool z = true;
    
    // Verification statement
    if (x && y -> z) {
        std::cout << "<<x && y -> z>> is true" << std::endl;
    } else {
        std::cout << "<<x && y -> z>> is false" << std::endl;
    }  
    
    <<x && y -> z>>
    // Output: <<x && y -> z>> is true 
}
