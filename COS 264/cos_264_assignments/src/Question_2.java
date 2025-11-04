//Write a structured Java program to read in a set of numbers, n, and print the summary at each iteration

import java.util.Scanner;

public class Question_2 {
    public static void main(String[] args)
    {
        Scanner input = new Scanner(System.in);
        int num;
        int number;
        int sum = 0;
        System.out.print("Enter the 'n' number of inputs you like: ");
        num = input.nextInt();
        System.out.println(num);
        int [] numbers_array = new int[num];
        for (int x = 1; x <= num; x++)
        {
            System.out.println(x);
            System.out.print("Enter your numbers: ");
            number = input.nextInt();
            System.out.println(number);
            sum += number;
            numbers_array[x-1] = number;
            System.out.println("number_array[" + (x-1) + "] is " + numbers_array[x-1]);
        }
        for (int m : numbers_array)
        {
            System.out.println(m);
        }
        int average = sum / num;
        System.out.println("Summary after computing " + num + " numbers: ");
        System.out.println("Sum of inputs = " + sum);
        System.out.println("Average of inputs = " + average);
        /*System.out.println("Maximum of inputs = " + max);
        System.out.println("Minimum of inputs = " + min);*/
    }
}
