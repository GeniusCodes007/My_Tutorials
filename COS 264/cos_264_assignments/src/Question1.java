//Write a Java program to accept your name and age and print

import java.util.Scanner;

public class Question1 {
    public static void main(String []args)
    {
        Scanner input = new Scanner(System.in);

        System.out.print("Your name: ");
        String name = input.nextLine().toUpperCase();

        System.out.print("Age: ");
        int age = input.nextInt();

        System.out.println(name + ", you are " + age + " years old.");

        if (age >= 16)
        {
            System.out.println(name + ", you are an Adult!!!");
        }else
        {
            System.out.println(name + ", you're still a child!!!");
        }
    }
}
