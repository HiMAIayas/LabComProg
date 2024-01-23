
public class BankAccount {
	Person person;
	String accountNumber;
	double balance;
	
	BankAccount(String name, String surname, String sex, String occupation, String organization, String accountNumber, double balance){
		this.person = new Person(name,surname,sex,occupation,organization);
		this.accountNumber = accountNumber;
		this.balance = balance;
	}
	
	void deposit(double x) {
		balance+=x;
	}
	
	void withdraw(double x) {
		if (balance>=x) balance-=x;
		else System.out.println("Not enough money to withdraw");
	}
	void printInfo() {
		this.person.printInfo();
		System.out.println("Account Number: "+accountNumber);
		System.out.println("Balance: "+balance);
	}
	void printBalance() {
		System.out.println("Balance = "+balance+" million USD");
	}
	double convertBalanceToTHB() {
		return balance*35.68;
	}
}
