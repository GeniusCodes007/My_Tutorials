#include <iostream>

using namespace std;

int main()
{
    string name;

    cout << "Name: ";
    getline(cin,name);
    //cin>> name;

    if (name.length() > 16)
    {
        cout <<"Name too long"<<endl;
    }
    else{
    cout<< name<<endl;
    }

    name.append("@gmail.com");
    cout<< "For append"<< endl;
    cout<< name<<endl;

    name.clear();
    cout<<endl<<endl<<"After clearing the contents of NAME"<<endl;
    if (name.empty())
    {
        cout<< "You Should Have A Name At Least"<<endl;
    }
    for (int a =1; a < 6; a++)
    {
        cout<< "For-loop A: "<< a <<endl;
        for (int b =1; b <6; b++)
        {
            cout << "For-loop B:    "<< b <<endl;
        }
    }
}
