
import java.util.Scanner;


public class Question3
{
    public static void main(String [] args)
    {
        Scanner inputs = new Scanner(System.in);
        String course;
        String course_code;
        String name;
        String reg_no;
        float score;
        char grade = ' ';
        System.out.print("Student Name: ");
        name = inputs.nextLine().toUpperCase();
        System.out.println(name);

        System.out.print("Reg. No: ");
        reg_no = inputs.nextLine();

        System.out.print("Course Code: ");
        course_code = inputs.nextLine().toUpperCase();

        System.out.print("Score: ");
        score = inputs.nextFloat();

        if (0 <= score && score <= 39)
        {
            grade = 'F';
        } else if (40 <= score && score <= 44)
        {
            grade = 'E';
        } else if (45 <= score && score <= 49) {
            grade = 'D';
        } else if (50 <= score && score <= 59) {
            grade = 'C';
        } else if (60 <= score && score <= 69) {
            grade = 'B';
        } else if (70 <= score && score <= 100) {
            grade = 'A';
        }else {
            System.out.println("Check Your Record!!! No student can have this Record");
        }
        System.out.println(name + "(" + reg_no + "): " + "(" + course_code + ") -> " + grade);
    }
}
