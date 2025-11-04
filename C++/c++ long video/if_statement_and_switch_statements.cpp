#include <iostream>
using namespace std;

int main()
{
    int age;
    cout << "Age:  ";
    cin >> age;
    if (age < 19)
    {
        cout <<"Sorry, you are not mature enough"<<endl;
    }else
    {
        cout<< "Congrats!!! You're Welcome"<< endl;
    }

    int monthNumber;
    cout<< "Enter Your Month Number:  ";
    cin >> monthNumber;
    switch(monthNumber)
    {
    case 1:
        cout<< "JANUARY CHILD"<< endl;
        break;

    case 2:
        cout<< "FEBRUARY CHILD"<< endl;
        break;

    case 3:
        cout<< "MARCH CHILD"<< endl;
        break;

    case 4:
        cout<< "APRIL CHILD"<< endl;
        break;

    case 5:
        cout<< "MAY CHILD"<< endl;
        break;

    case 6:
        cout<< "JUNE CHILD"<< endl;
        break;

    case 7:
        cout<< "JULY CHILD"<< endl;
        break;

    case 8:
        cout<< "AUGUST CHILD"<< endl;
        break;

    case 9:
        cout<< "SEPTEMBER CHILD"<< endl;
        break;

    case 10:
        cout<< "OCTOBER CHILD"<< endl;
        break;

    case 11:
        cout<< "NOVEMBER CHILD"<< endl;
        break;

    case 12:
        cout<< "DECEMBER CHILD"<< endl;
        break;

    default:
        cout<<"Which Month Should "<< monthNumber<< " be?"<< endl;
    }

    cout << "Done" << endl;
}
