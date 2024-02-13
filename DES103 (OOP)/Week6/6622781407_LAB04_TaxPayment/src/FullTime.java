//Define class full time to be a subclass of Employee and TaxPayer
public class FullTime extends Employee implements TaxPayer{
	double salary;
	String workPlace;

	FullTime(String name, String position, String workPlace, double salary) { 
		super(name,position);
		this.workPlace = workPlace;
		this.salary = salary;
	}

	// Write by yourself all overridden methods from its parents

	public void printInfo() {
		super.printInfo();
		this.printWorkPlace();
		System.out.println("Yearly income is "+calculateYearlyIncome());
		this.payTax();
		System.out.println("--------------------");
		
	}

	@Override
	public double calculateYearlyIncome() {
		return salary*12;
	}

	@Override
	public double calculateTax() {
		return super.calculateTaxRate(calculateYearlyIncome())*calculateYearlyIncome();
	}

	@Override
	public void payTax() {
		System.out.println("Pay tax "+calculateTax());
	}

	@Override
	double calculateMonthlyIncome() {
		return salary;
	}

	@Override
	void printWorkPlace() {
		System.out.println("Work at "+workPlace);
	}

}