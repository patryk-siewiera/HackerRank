#include <iostream>
#include <string>

using namespace std;

int main() {

    string word1;
    string word2;
    string word1mod;
    string word2mod;

    cin >> word1;
    cin >> word2;


    cout << word1.size() << " " << word2.size() << endl;
    cout << word1 + word2 << endl;

    word1mod = word1;
    word1mod[0] = word2[0];
    word2mod = word2;
    word2mod[0] = word1[0];

    cout << word1mod << " " << word2mod << endl;

    return 0;
}

