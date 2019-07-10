#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int number;
    int tab[number];

    cin >> number;

    for (int i =0; i<number;i++){
        cin>> tab[i];
    }

    for (int j = 0; j<number; j++){
        cout << tab[number-j-1] << " ";
    }

    return 0;
}
