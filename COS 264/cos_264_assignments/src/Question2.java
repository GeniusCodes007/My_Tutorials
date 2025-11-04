import java.util.Scanner;

public class Question2
{
    public static void main(String[]args)
    {
        Scanner input = new Scanner(System.in);
        int count = 1;
        double sum = 0;
        double min = Double.MAX_VALUE;
        double max = Double.MIN_VALUE;

        System.out.print("Enter your number of inputs: ");
        int loop_num = input.nextInt();



        while (count <= loop_num)
        //The loop will iterate if the input is can be translated to a double character
            // and count is less than or equal to loop_num
        {
            System.out.print("Enter your number: ");
            double num = input.nextDouble();
            System.out.println("count: " + count);
            sum += num;
            min = Math.min(min, num);
            max = Math.max(max, num);

            System.out.println("Summary after " + count + " numbers: ");
            System.out.println("Sum: " + sum);
            System.out.println("Mean: " + (sum / count));
            System.out.println("Min: " + min);
            System.out.println("Max: " + max);
            count ++;
        }
        //input.close();
    }
}
