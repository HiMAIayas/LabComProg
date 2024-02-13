abstract public class Employee {
	String name;
	String position;

	Employee(String name, String position) {
		this.name = name;
		this.position = position;
	}

	// define all abstract methods according to UML
	abstract double calculateMonthlyIncome();
	abstract void printWorkPlace();

	void printInfo() {
		// Print info of an Employee in the format of [name] is a [position]
		System.out.println(name+" is a "+position);
	}

	// This method is provided. No need to add anything.
	double calculateTaxRate(double salary_year) {
		if (salary_year<=200000) return 0.0;	
		else if (salary_year<=400000) 	return 0.05;
		else if (salary_year<=600000)	return 0.1;	
		else if (salary_year<=800000)	return 0.15;
		else return 0.2;
	}

}