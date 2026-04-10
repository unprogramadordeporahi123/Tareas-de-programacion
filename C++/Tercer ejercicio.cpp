#include <iostream>
int main() {
    int edad;
    std::cout << "Tu edad: ";
    std::cin >> edad;

    if (edad < 18) {
        std::cout << "Eres un niño" << std::endl;
    } 
    
    else if (edad >= 18 && edad <= 65) {

        std::cout << "Eres un adulto" << std::endl;
    } 
    
    else {

        std::cout << "Eres un anciano" << std::endl;
    }

    return 0;
}