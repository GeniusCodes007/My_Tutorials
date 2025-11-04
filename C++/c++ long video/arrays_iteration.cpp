#include <iostream>

using namespace std;

void getArray(int arrays []);
void getArray(string arrays []);
int size_O = 100;
int main()
{
    cout << "From CLion" << endl;
    int numbers [] = {12, 39, 40, 18, 47, 20} ;

    //for-each loop
    for (int numb: numbers)
    {
        cout<< numb << endl;
    }
    getArray(numbers);

    string chars[] = { "a", "b", "c", "d", "e", "f"};
    //getArray(chars);
}


void getArray(int arrays [])
{
    for(int a = 0; a <= size_O; a++ )
    {
        cout << "for content "<< a<< endl;
        cout << arrays[a] << endl;
    }
}

void getArray(string arrays [])
{
    cout <<"arrays"<<endl;
    for (int a =0; a <= size_O; a++)
    {
        cout << arrays[a] << endl;
    }
}
