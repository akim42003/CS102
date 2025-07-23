#include <iostream>
#include <string>

using namespace std;

class WALLET {
private:
  string type;
  int cash_money;

public:
  WALLET();
  WALLET(int i);
  void add_cash(int i);
  int get_amount();
};

WALLET::WALLET() {
  cash_money = 0;
}

WALLET::WALLET(int i) {
  cash_money = i;
}

void WALLET::add_cash(int i) { 
  cash_money += i; }

int WALLET::get_amount() { 
  return cash_money; }

int main() {
  int add = 0;
  WALLET wallet(100);
  cout << "Initial balance: " << wallet.get_amount() << "\n";
  cout << "How much do you want to add: ";
  cin >> add;
  wallet.add_cash(add);
  cout << "Final balance: " << wallet.get_amount() << "\n";
}