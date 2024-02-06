
public class Employee extends Person {
	String workplace;
	String position;
	double salary;
	
	Employee(String firstname, String lastname, int day, int month, int year, String workplace, String position, double salary){
		super(firstname,lastname,day,month,year);
		this.workplace = workplace;
		this.position = position; 
		this.salary = salary;
	}
	
	void printInfo() {
		super.printInfo();
		System.out.println("Workplace: "+this.workplace);
		System.out.println("Position: "+this.position);
		System.out.println("Salary: "+this.salary);
	}
	
	void followRule(String rule) {
		System.out.println(this.position+": "+super.name.firstname+" "+super.name.lastname);
		System.out.println("Followed: "+rule);
	}
}
