#include <iostream>

using namespace std;

int size_O = 100;

int main ()
{
    cout << "Arrays In C++" << endl;
    int myArray [9] = {12, 30, 83, 28, 19, 37, 28, 37, 92};

    cout << "Size: " << sizeof(myArray) << endl;

    myArray[5] = 3;

    for (const int member : myArray) {
        cout << member << endl;
    }

    int b [3] = {4, 4, 89};
    int a [3] = {2, 4, 11};

    cout << "" << endl;
}
