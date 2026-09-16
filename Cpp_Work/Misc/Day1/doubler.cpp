#include <iostream>

int getUserInput();

int main()
{
    int num{getUserInput()};
    std::cout << "Your number doubled is: " << num * 2 << "\n";

    return 0;
}