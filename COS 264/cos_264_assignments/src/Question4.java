import java.util.Scanner;

//Write a Java program to calculate the factorial of a number
public class Question4 {

    public Question4()
    {

    }
    public int factorial(int number)
    {
        int product = 1;
        for (int x = 1; x <= number; x++)
        {
            product *= x;
        }
        return product;
    }
    public static void main (String[]args)
    {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter your number: ");
        int number = input.nextInt();
        Question4 fact = new Question4();
        System.out.println("the factorial of "+ number + " is: "+ fact.factorial(number));
    }
}
