
public class Executive extends Employee{
	double bonus;
	
	Executive(String firstname, String lastname, int day, int month, int year, String workplace, String position, double salary,double bonus){
		super(firstname,lastname,day,month,year,workplace,position,salary);
		this.bonus=bonus;
	}
	
	void printInfo() {
		super.printInfo();
		System.out.println("Bonus: "+this.bonus);
	}
	
	void announceRule(String rule) {
		System.out.println(super.position+": "+super.name.firstname+" "+super.name.lastname);
		System.out.println("Announces rule: "+rule);
	}
}
