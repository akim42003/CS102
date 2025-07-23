#include <iostream>

int higher(int x, int y) {
  int hn = 0;
  if (x > y) {
    hn = x;
  } else {
    hn = y;
  }
  return hn;
}

int main() {
  int value1 = 0;
  int value2 = 0;

  std::cout << "Please enter an integer: ";
  std::cin >> value1;
  std::cout << "Enter another integer: ";
  std::cin >> value2;
  int result = higher(value1, value2);
  std::cout << "The larger integer is " << result << "\n";
}