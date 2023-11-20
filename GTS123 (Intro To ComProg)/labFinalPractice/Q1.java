package labFinalPractice;
import java.util.Scanner;

public class Q1 { //file name and class name must be the same.

    public static void main(String[] args) {
      int money, num;
      String act;
      String[] line;
      Scanner inp = new Scanner(System.in);
      
      System.out.print("Enter the initial balance: ");
      money = inp.nextInt();
      inp.nextLine();

      while (true) {
        System.out.print("Transaction type and amount (\"done 0\" to exit): ");
        line = (inp.nextLine()).split(" ");
        
        act = line[0];
        //System.out.println("Line is "+act+" "+line[1]);
        if (act.equals("done")) break; //== is simply checks for address equal

        try {
            num=Integer.parseInt(line[1]);
        } catch (Exception e) {
            System.out.println("> Invalid transaction");
            continue;
        }

        if (act.equals("D")){
            money+=num;
            System.out.println("> Deposit = "+num+" THB, Current balance = "+money);
        }
        else if (act.equals("W")){
            if (money<num) System.out.println("> Invalid transaction");
            else {
                money-=num;
                System.out.println("> Withdrawal = "+num+" THB, Current balance = "+money);
            }
        }
        else {
            System.out.println("> Invalid transaction");
        }
      }

      inp.close();
      System.out.println("> Current balance = "+money);
    }
}