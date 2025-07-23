#include <iostream>
#include <string>

using namespace std;

int hex_to_decimal(string hex_num) {
    int decimal_num = 0;
    int power = 1;
    for (int i = hex_num.length() - 1; i >= 0; i--) {
        int digit = 0;
        if (hex_num[i] >= '0' && hex_num[i] <= '9') {
            digit = hex_num[i] - '0';
        } else if (hex_num[i] >= 'a' && hex_num[i] <= 'f') {
            digit = hex_num[i] - 'a' + 10;
        }
        decimal_num += digit * power;
        power *= 16;
    }
    return decimal_num;
}

int main() {
    string s = "abbc";
    int decimal_num = hex_to_decimal(s);
    if(decimal_num != -1){
        cout << "Hexadecimal: " << s << endl;
        cout << "Decimal: " << decimal_num << endl;
    }
    return 0;
}
