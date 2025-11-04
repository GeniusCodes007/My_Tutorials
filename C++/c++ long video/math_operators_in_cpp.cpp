#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    //Basically,
    int x = 28;
    int y = 41;

    //For max
    cout <<"For max" << endl;
    cout<< "Considering x: "<< x<< " and y: "<< y<< endl;
    cout << max(x, y) << endl;

    //For min
    cout <<endl<<"For min" << endl;
    cout<< "Considering x: "<< x<< " and y: "<< y<< endl;
    cout << min(x, y) << endl;

    //For modulo
    cout <<endl<<"For modulo" << endl;
    cout<< "Considering x: "<< x<< " and y: "<< y<< endl;
    cout << y % x << endl;

    //For These Include The cmath module
    cout <<endl<<endl<<endl<< "For the following include the cmath module" << endl;

    //For pow
    cout <<endl<<"For pow" << endl;
    cout << pow(2, 3) << endl;

    //For square root
    cout <<endl<<"For square root" << endl;
    cout << sqrt(225) << endl;

    //For abs
    cout <<endl<<"For abs" << endl;
    cout << abs(-23) << endl;

    double a;
    double b;
    double c;
    double d;
    double e;
    double f;

    //For round
    cout <<endl<<"For round" << endl;
    a = 38.23;
    cout<< "Considering a: "<< a<< endl;
    cout << round(a) << endl;
    b = 23.58;
    cout<< "Considering b: "<< b<< endl;
    cout<< round(b)<< endl;

    //For ceil
    cout<<endl <<"For ceil" << endl;
    c = 23.75;
    cout << "Considering c: " <<c << endl;
    cout << ceil(c) << endl;
    d = 49.12;
    cout << "Considering d: " <<d << endl;
    cout << ceil(d) << endl;

    //For floor
    cout<<endl <<"For floor" << endl;
    e = 23.75;
    cout << "Considering e: " <<e << endl;
    cout << floor(e) << endl;
    f = 49.12;
    cout << "Considering f: " <<f << endl;
    cout << floor(f) << endl;
}
