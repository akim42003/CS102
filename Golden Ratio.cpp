
/**
 * CS-102 Project 01: Calculates the golden ratio to a given precision.
 * @file golden_ratio.cpp
 * @author(s) 
 * @date
 */
#include <cmath>
#include <iostream>

const double GOLDEN_RATIO = 1.618033988749895;

// Controls the operation of the program.
int main() {
    float ratio = 0;
    float tolerance = 0;
    float old_num =  1;
    float new_num = 1;
    float temp = 0;
    std::cout << "Enter a tolerance: ";
    std::cin >> tolerance;
    while (std::abs(GOLDEN_RATIO - ratio) > tolerance){
        temp = old_num;
        ratio = new_num/temp;
        old_num = new_num;
        new_num += temp;
    }
    std::cout << old_num << " " << temp;
}