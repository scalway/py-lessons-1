#include <iostream>
#include <string>
#include <fstream>
#include <chrono>
using namespace std;

int findInString(string needle, string haystack) {
    for (int i = 0; i < haystack.length(); i++) {
        for (int j = 0; j < needle.length(); j++) {
            if (needle[j] != haystack[i+j]) {
                break;
            }

            if (j == needle.length() - 1) {
                return i;
            }
        }

    }
    return -1;
}

void expectResult(string needle, string haystack, int expectedResult) {
    auto actualResult = findInString(needle, haystack);

    if (actualResult == expectedResult) {
        cout << "OK" << endl;
    }
    else {
        cout << "WRONG RESULT, expeced " << expectedResult << endl;
    }
}

int main()
{
    // na pozniej
    string filename("text.txt");
    ifstream file(filename);

    if (!file.good()) {
        cout << "nie udalo sie otworzyc pliku " << filename << endl;
        return 1;
    }

    string fileContents;
    string line;

    while (getline(file, line)) {
        fileContents += line;
        fileContents += "\n";
    }

    string haystack = fileContents;
    string needle = "ale";

    expectResult("la", haystack, 1);
    expectResult("ola", haystack, -1);
    expectResult("ma", haystack, 4);
    expectResult("kota", haystack, 7);

    auto t1 = std::chrono::high_resolution_clock::now();
    auto result = findInString(needle, haystack);
    auto t2 = std::chrono::high_resolution_clock::now();
    cout << result;

    chrono::duration<double, milli> runningTime = t2 - t1;

    cout << runningTime.count() << "ms";
}
