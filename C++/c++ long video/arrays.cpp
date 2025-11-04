#include <iostream>

using namespace std;

int main()
{
    string chars[] = { "a", "b", "c", "d", "e", "f"};
    chars[2] = "hsuju";
    cout << chars[5] <<endl;
    for (int a = 0; a <= 5; a++)
    {
        cout << "this is for chars: "<< chars[a] << endl;
    }

    int number[3];
    number[0] =23;
    number[1] = 58;
    number[2] = 90;
    number[3] = 21;
    cout << number [3];


}
