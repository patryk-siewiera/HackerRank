#include <iostream>
#include <cstdio>

using namespace std;

int main() {
    string num[10] = {"-----", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};

    int low, high, count;
    cin >> low;
    cin >> high;

    count = high - low + 1;

    for (int i = 0; i < count; i++) {
        if (low <= 9) {
            cout << num[low] << endl;
        } else {
            if (low % 2 == 0) {
                cout << "even" << endl;
            } else {
                cout << "odd" << endl;
            }
        }
        low++;
    }


    return 0;
}
