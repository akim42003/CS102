#include <iostream>
using namespace std;

void prime_factors(int k) {
    if (k == 1) {
        return;
    }
    for (int i = 2; i <= k; i++) {
        if (k % i == 0) { 
            bool is_prime = true;
            for (int j = 2; j*j <= i; j++) {
                if (i % j == 0) { // i is not prime
                    is_prime = false;
                    break;
                }
            }
            if (is_prime) {
                cout << i << " ";
                prime_factors(k / i); 
                return;
            }
        }
    }
}

int main() {
    cout << "Enter a positive integer: ";
    int n = 1;
    cin >> n;
    cout << "The prime factors of " << n << ": ";
    prime_factors(n);
    cout << endl;
}