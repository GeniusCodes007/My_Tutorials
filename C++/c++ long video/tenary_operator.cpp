#include <iostream>
using namespace std;

int main()
{


    cout << "The Tenary Operator comes like this: '?:'"<< endl;

    cout << "To Use The Tenary Operator: ";

    cout <<endl<< "Bear in mind, it works like an if-else statement. ";

    cout <<endl<< "The part before '?' is similar to the 'if' side while the part after the ':' is the 'else' side. ";

    cout <<endl<< "Take the line code below into consideration, and study the result it gives at different inputs";

    cout <<endl<<endl<< "age <= 18 ? cout<<endl<< 'Try Again When You Are 19 or Older' : cout << 'Congrats!!! You're Welcome'<< endl;" ;

    int age;

    cout <<endl<<endl<< "Enter Your Age:  ";

    cin>> age;

    age < 19 ? cout<<endl<< "Try Again When You Are 19 or Older" : cout << "Congrats!!! You're Welcome"<< endl;
}
