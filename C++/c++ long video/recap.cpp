#include <iostream>
using namespace std;

//Using namespaces 

namespace record1
{
    int age = 19;
}

namespace record2
{
    int age = 22;
}


int main()
{
    cout << "This is Record 1: " << record1::age << endl;

    cout << "This is Record 2: " << record2::age << endl;

    //Taking inputs
    string name;
    cout << "Enter Your Name: " << endl;
    cin >> name; 
    cout << "Your Name Is " << name << endl;

    string name2;
    cout << "Enter Your Name: " << endl;
    cin >> name2; 
    cout << "(Again) Your Name Is " << name2 << endl;

    string fullName;
    cout << "Enter Your Full Name: " <<endl;
    getline (cin >> ws, fullName); 
    cout << "Your Full Name Is " << fullName << endl;
}