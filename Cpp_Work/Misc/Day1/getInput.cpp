#include <iostream>

int getUserInput()
{
    std::cout << "Enter an integer here: ";

    int num{};
    std::cin >> num;

    return num;
}
