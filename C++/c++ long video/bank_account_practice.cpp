#include <iostream>

using namespace std;

double accBalance = 0;

void balance()
{
    cout << "Balance: "<< accBalance<<endl<<endl;
}

void deposit(long amountInvolved)
{
    if (amountInvolved >= 0)
    {
        accBalance += amountInvolved;
        cout << amountInvolved <<" deposited successfully" <<endl<<endl;
    }else{
    cout << "I Think You Meant A Withdrawal" << endl<<endl;
    }
}

void withdraw(long amountInvolved)
{
    double finalAmount;
    if (amountInvolved <= accBalance && amountInvolved >= 0)
    {
        accBalance -= amountInvolved;
        cout << amountInvolved << " withdrawn successfully" <<endl<<endl;
    }else if (amountInvolved < 0)
    {
        cout << -(amountInvolved) << endl<<endl;
        finalAmount = -(amountInvolved);
        if (finalAmount <= accBalance)
        {
            accBalance -= finalAmount;
            cout << finalAmount << " withdrawn successfully" <<endl<<endl;
        }else{
        cout << "I Think You May Need A Loan" << endl<<endl;
        }
    }
    else
    {
        cout << "I Think You May Need A Loan" << endl<<endl;
    }
}

int main()
{
    int activity;
    int amount;

    do
    {
        cout << "**************************************************" << endl;
        cout << "********  What Do You Want To Do Today ***********" << endl;
        cout << "**************************************************" << endl;
        cout << "1. Show Balance" << endl;
        cout << "2. Deposit" << endl;
        cout << "3. Withdraw" << endl;
        cout << "4. Exit" << endl;

        cout<< "What Do You Wish To Do: "<<endl;
        cin >> activity;

        cin.clear();
        fflush(stdin);

        switch(activity)
        {
        case 1:
            balance();
            break;
        case 2:
            cout << "How much do you want to deposit: ";
            cin >> amount;
            deposit(amount);
            break;
        case 3:
            cout << "How much do you want to withdraw: ";
            cin >> amount;
            withdraw(amount);
            break;
        case 4:
            cout << "Exiting...." << endl;
            break;
        default:
            cout << "Check Your Options"<< endl<<endl;
        }
    }while(activity != 4);

    return 0;
}
