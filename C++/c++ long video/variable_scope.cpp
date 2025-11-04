#include <iostream>

using namespace std;


//Global Variable
int num = 34;

void myNum(int x)
{
    cout <<endl<< "myNum function begins" << endl;
    int num2 = 12;
    cout << "Here, in myNum function, ";
    cout << "We Have Access To The Global Variable: " << num <<endl;
    num = 3;
    cout << "Global is now: ";
    cout << num << endl;
    cout <<endl<< "Our function result is: "<< num2 + x << endl;
    cout << "myNum function ends" << endl;
}


int main()
{
    cout <<"In C++, there are two types of variables that can exist in code"<<endl;
    cout << "The Global Variable and the Local Variable"<< endl;
    cout << "The Global Variable is declared outside every function in the code, even the main function, " ;
    cout << "and it is available to all functions for use." << endl;
    cout << "The Local Variable is declared in a function and is available only to that function for use" << endl;

    cout <<endl<< "For the Global Variable" << endl;
    cout << num << endl;

    cout <<endl<< "For the Local Variable" << endl;
    myNum(9);
    return 0;
}
