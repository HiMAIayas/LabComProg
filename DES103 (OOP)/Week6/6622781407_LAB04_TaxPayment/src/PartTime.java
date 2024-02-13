
//Define PartTime to be the subclass of Employee and TaxPayer
public class PartTime extends Employee implements TaxPayer {
	String workPlace;
	int numHrPerWeek;
	double hourlyRate;

	PartTime(String name, String position, String workPlace, int numHrPerWeek, double hourlyRate) { 
		super(name,position);
		this.workPlace = workPlace;
		this.numHrPerWeek = numHrPerWeek;
		this.hourlyRate = hourlyRate;

	}


	public void printInfo() {
		super.printInfo();
		this.printWorkPlace();
		System.out.println("Yearly income is "+calculateYearlyIncome());
		this.payTax();
		System.out.println("--------------------");


	}

	@Override
	public double calculateYearlyIncome() {
		return 12*calculateMonthlyIncome();
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
		return numHrPerWeek*hourlyRate*4;
	}

	@Override
	void printWorkPlace() {
		System.out.println("Work at "+workPlace);
		
	}
}