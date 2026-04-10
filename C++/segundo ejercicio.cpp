#include <iostream>
#include <cmath>

int main() {

    double num1, num2;

    std::cout << "Primer numero  ";
    std::cin >> num1;
    std::cout << "Segundo numero ";
    std::cin >> num2;
    std::cout << "-------------------------" << std::endl;

    std::cout << "Suma:" << num1 + num2 << std::endl;
    std::cout << "Resta: " << num1 - num2 << std::endl;
    std::cout << "Multiplicacion: " << num1 * num2 << std::endl;
    std::cout << "Division: " << num1 / num2 << std::endl;

    std::cout << "Raiz cuadrada:  " << num1 << ": " << sqrt(num1) << std::endl;

    return 0;
}

