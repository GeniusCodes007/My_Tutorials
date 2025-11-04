//
// Created by GENIUS DEXTER on 03/10/2025.
//
#include <iostream>

using namespace std;

class StackClass
{
    private:

    int top;
    int array[5];

    public:
    StackClass() {
        top = -1;
        for (int i = 0; i <5; i++) {
            array[i] = 0;
        }
    }

    bool isEmpty() {
        if (top == -1)
            return true;
        else
            return false;
    }

    bool isFull() {
        if (top == 4)
            return true;
        else
            return false;
    }

    void push(int val) {
        if (isFull()) {
            cout << "Stack Overflow" << endl;
        }else {
            top++;
            array[top] = val;
        }
    }

    int pop() {
        if (isEmpty()) {
            cout << "Stack Underflow" << endl;
            return 0;
        } else {
            const int popVal = array[top];
            array[top] = 0;
            top-- ;
            return popVal;
        }
    }

    int count() {
        return top+1;
    }

    int peek(int pos) {
        if (isEmpty()) {
            cout << "Stack Underflow" << endl;
            return 0;
        } else {
            return array[pos];
        }
    }

    void replace(int pos, int val) {
        array[pos] = val;
        cout << "value changed at position: "<< pos << endl;
    }

    void display() {
        cout << "All Values of Stack --> " << endl;
        for (int i : array) {
            cout << i << endl;
        }
    }
};


int main()
{
    cout << "A Stack is " << endl;
    cout << "Important functions in working with stack data stuctures" << endl;
    cout << "push(): Overflow status" << endl;
    cout << "pop(): Underflow status" << endl;
    cout << "isEmpty()" << endl;
    cout << "isfull()" << endl;
    cout << "peek()" << endl;
    cout << "count()" << endl;
    cout << "change()" << endl;
    cout << "display()" << endl;
}