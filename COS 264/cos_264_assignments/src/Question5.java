//Write a program with Java using if statements that increase pay by 3%,
//if hour worked is greater than 8 hours, and by 1% if otherwise
import java.util.Scanner;

public class Question5
{
    public static void main(String[] args)
    {
        Scanner input = new Scanner(System.in);
        int basic_salary ;
        double raised_salary;
        String employee_name;
        int hours_worked;
        System.out.print("Employee Name: ");
        employee_name = input.nextLine().toUpperCase();

        System.out.print("Hours Worked: ");
        hours_worked = input.nextInt();

        System.out.print("Basic Salary: ");
        basic_salary = input.nextInt();

        if (8 < hours_worked){
            raised_salary = basic_salary + (basic_salary * 0.03);
            System.out.println(employee_name + " : Salary -> " + raised_salary);
        } else {
            raised_salary = basic_salary + (basic_salary * 0.01);
            System.out.println(employee_name + " : Salary -> " + raised_salary);
        }
    }
}