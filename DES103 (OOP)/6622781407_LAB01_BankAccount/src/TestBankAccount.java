
public class TestBankAccount {
	public static void main(String[] args) {
		//1 and 2
		BankAccount obj = new BankAccount("Wang","TaLu","Male","Actor","SIIT","000-000-0000",10);
		obj.printInfo();
		
		//3
		obj.person.name = "Phumipas";
		obj.person.surname = "Namjaidee";
		obj.person.sex = "Male";
		//4
		obj.printInfo();
		
		//5 and 6
		obj.deposit(15);
		obj.printBalance();
		
		//7 and 8
		obj.withdraw(5);
		obj.printBalance();
		
		//9
		System.out.println("Balance = "+obj.convertBalanceToTHB()+" million THB");
	}
}
