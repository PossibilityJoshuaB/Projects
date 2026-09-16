#include <iostream>
#include "io.h"

int readNumber()
{
    // prompt user for number
    std::cout << "Enter an integer: ";

    // store user number as num
    int num{};
    std::cin >> num;

    // return user input
    return num;
}

void writeAnswer(int answer)
{
    // send the parameter to the console
    std::cout << answer;
}